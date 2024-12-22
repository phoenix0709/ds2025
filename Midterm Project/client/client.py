from mpi4py import MPI
import requests
import os

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

def send_file(file_path):
    try:
        with open(file_path, "rb") as f:
            response = requests.post("http://<PROXY_IP>:5000/upload", files={"file": f})
        print(f"Server response from rank {rank}: {response.text}")
    except Exception as e:
        print(f"Error from rank {rank}: {e}")

if __name__ == "__main__":
    if rank == 0:  
        print(f"Welcome to the Client! Total MPI processes: {size}")
        while True:
            command = input("\nEnter a command (upload <file_path> / quit): ").strip()
            if command.startswith("upload "):
                _, file_path = command.split(" ", 1)
                if os.path.exists(file_path):
                    for i in range(1, size):
                        comm.send(file_path, dest=i, tag=11)
                    send_file(file_path) 
                else:
                    print(f"File not found: {file_path}")
            elif command == "quit":
                print("Exiting Client.")
                for i in range(1, size):
                    comm.send("QUIT", dest=i, tag=11)
                break
            else:
                print("Invalid command. Try 'upload <file_path>' or 'quit'.")
    else:  
        while True:
            file_path = comm.recv(source=0, tag=11)
            if file_path == "QUIT":
                print(f"Rank {rank} exiting.")
                break
            send_file(file_path)

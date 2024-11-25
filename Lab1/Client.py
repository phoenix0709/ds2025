import socket

def send_file(server_host, server_port, file_path):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_host, server_port))
    print(f"Connected to {server_host}:{server_port}")
    
    with open(file_path, 'rb') as file:
        while chunk := file.read(1024):
            client_socket.send(chunk)
    
    print("File sent successfully!")
    client_socket.close()

if __name__ == "__main__":
    send_file("192.168.12.253", 6969, "transferfile.txt")

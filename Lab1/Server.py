import socket

def start_server(host='0.0.0.0', port=6969):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Server listening on {host}:{port}...")
    
    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")
    
    with open("received_file.txt", 'wb') as file:
        while chunk := conn.recv(1024):
            file.write(chunk)
    
    print("File received successfully!")
    conn.close()
    server_socket.close()

if __name__ == "__main__":
    start_server()

import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

host = "127.0.0.1"
port = 12346

server_socket.bind((host, port))
server_socket.listen(1)
print("Server waiting for connection...")

conn, addr = server_socket.accept()
print("Connected with", addr)

data = conn.recv(1024).decode()
print("Client says:", data)

conn.sendall("Hello from Server!".encode())

# keep connection alive a bit
conn.recv(1024)

conn.close()
server_socket.close()
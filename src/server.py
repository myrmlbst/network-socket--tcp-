import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = socket.gethostbyname(socket.gethostname())
PORT = 1020

# bind the socket to a host and port
server.bind((HOST, PORT))

# listen for incoming connections connections
server.listen(5) # 5 unaccepted connections are allowed before rejecting new ones

while True:
    communication_socket, address = server.accept()
    print(f"Connected to {address}")
    message = communication_socket.recv(1024).decode('utf-8')
    print(f"Client message: {message}")

    # inform the other client that their message was sent
    communication_socket.send(f"Message recieved.".encode('utf-8'))

    communication_socket.close()
    print(f"Connection with {address} has ended.")

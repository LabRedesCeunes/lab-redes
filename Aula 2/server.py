import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)
print('waiting for a connection')
connection, client_address = sock.accept()
print('connected!', client_address)
print('Waiting for a message...')
while True:
    # Wait for a connection
    
        # Receive the data in small chunks and retransmit it
    data = connection.recv(32)
    print("Message received from client: ", data.decode())

    message = input("Write your answer to the client: ")
    message = str.encode(message)
    connection.sendall(message)

    print("Waiting for new messages...")


import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)
print('connected!')
while True:
    
    # Send data
    message = input("Write your message to the server: ")
    message = str.encode(message)
    sock.sendall(message)

    print("Waiting for an answer...")

    data = sock.recv(32)
    print("Message received from server: ", data.decode())
    

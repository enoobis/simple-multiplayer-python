import socket

# Server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 8000))
server.listen(5)

while True:
    client, address = server.accept()
    print(f'Connected by {address}')
    client.send(b'Welcome to the Multiplayer')
    client.close()

# Client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('server_ip', 8000))
print(client.recv(1024).decode())
client.close()
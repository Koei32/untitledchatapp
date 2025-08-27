import socket


host = "https://crispy-goldfish-jjx4r5xv5rwfqvpr-4169.app.github.dev/"
port = 14169
c = socket.socket()
c.connect((host, port))
message = c.recv(1024)
print(message.decode())

nickname = "Koei"


def connect():




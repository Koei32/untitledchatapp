import socket

def greet(nick: str, c: socket.socket):
    c.send(nick.encode())

nick = input("Nickname: ")


host = "127.0.0.1"
port = 14169
c = socket.socket()
c.connect((host,port))
greet(nick, c)
message = c.recv(1024)
print(message.decode())





import socket

c = socket.socket()


c.connect(("localhost", 4169))

def send_msg(msg: str):
    c.send(msg.encode())

while True:
    msg = input("message: ")
    send_msg(msg)



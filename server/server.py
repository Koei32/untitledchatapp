import socket

s = socket.socket()

s.bind(("localhost", 4169))
s.listen(1)

while True:
    c_socket, c_addr = s.accept()
    print(f"{c_addr} has connected")
    x = c_socket.recv(1024)
    print(x)
    c_socket.close()
    s.close()


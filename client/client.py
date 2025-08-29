import socket
import pickle

def greet(nick: str, c: socket.socket):
    c.send(nick.encode())

def send_reg_msg(user: str, pwd: str, c: socket.socket):
    print("sending REG to server")
    c.send("REG".encode())
    response = c.recv(1024).decode()
    if response == "OK":
        print("server responded OK, sending user and pwd")
        c.send(pickle.dumps((user, pwd)))
        print(c.recv(1024).decode())
        #login
    else:
        return False


try:
    host = "koei.hackclub.app"
    port = 14169
    c = socket.socket()
    c.connect((host,port))
    user = input("User: ")
    password = input("Password: ")
    # greet(nick, c)
    send_reg_msg(user, password, c)
    message = c.recv(1024)
    print(message.decode())
except KeyboardInterrupt:
    c.close()




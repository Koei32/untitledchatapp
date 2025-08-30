from PySide6.QtWidgets import QApplication, QMainWindow
import socket
import pickle
import sys

from login_form import LoginForm

host = "koei.hackclub.app"
port = 14169
c = socket.socket()
# c.connect((host,port))

def greet(nick: str, c: socket.socket):
    c.send(nick.encode())

def send_reg_msg(user: str, pwd: str, c: socket.socket):
    c.connect((host, port))
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


app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle("Untitled Chat App")
login = LoginForm(c)
login.setFixedHeight(260)
window.setCentralWidget(login)
window.show()


app.exec()

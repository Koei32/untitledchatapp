from PySide6.QtWidgets import QWidget, QPushButton, QCheckBox, QLineEdit, QVBoxLayout
import pickle
import socket
from util_functions import VALID_CHARS


host = "koei.hackclub.app"
port = 14169

class LoginForm(QWidget):
    def __init__(self, client: socket.socket):
        super().__init__()
        self.client = client
        self.user_field = QLineEdit(placeholderText="Username")
        self.user_field.textChanged.connect(self.set_creds)

        self.pass_field = QLineEdit(placeholderText="Password")
        self.pass_field.setEchoMode(QLineEdit.EchoMode.Password)

        self.pass_field.textChanged.connect(self.set_creds)
        

        self.pass_field.textChanged.connect(self.check_password_validity)

        self.submit_button = QPushButton("Login")
        self.submit_button.setFixedWidth(100)
        # self.submit_button.clicked.connect(self.send_reg_msg)
        self.submit_button.clicked.connect(self.send_login_msg)

        layout = QVBoxLayout()
        layout.addWidget(self.user_field)
        layout.addWidget(self.pass_field)
        layout.addWidget(self.submit_button)
        self.setLayout(layout)

    def send_reg_msg(self):
        self.client.connect((host, port))
        print("sending REG to server")
        self.client.send("REG".encode())
        self.submit_button.setDisabled(True)
        response = self.client.recv(1024).decode()
        if response == "OK":
            print("server responded OK, sending user and pwd")
            self.client.send(pickle.dumps((self.username, self.password)))
            print(self.client.recv(1024).decode())
            #login
        else:
            return False
    
    def send_login_msg(self):
        self.client.connect((host, port))
        print("sending LOG to server")
        self.client.send("LOG".encode())
        self.submit_button.setDisabled(True)
        response = self.client.recv(1024).decode()
        if response == "OK":
            print("server responded OK, sending user and pwd")
            self.client.send(pickle.dumps((self.username, self.password)))
            print(self.client.recv(1024).decode())
            #login
        else:
            return False
    
    def check_password_validity(self) -> int:
        print(self.username, self.password)
        if len(self.password) < 8:
            return 1
        for chr in self.password:
            if chr not in VALID_CHARS:
                return 2
        return 0
    
    def set_creds(self):
        self.username = self.user_field.text()
        self.password = self.pass_field.text()



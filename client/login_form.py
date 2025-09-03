from PySide6.QtWidgets import QWidget, QPushButton, QCheckBox, QLineEdit, QVBoxLayout, QHBoxLayout, QLabel, QSizePolicy
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt, QSize
import pickle
import socket
from fonts import warning_font, default_font
from util_functions import VALID_CHARS
from config import ConfigManager

cfgmgr = ConfigManager()
host = cfgmgr.host
port = cfgmgr.port

class LoginForm(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def send_reg_msg(self):
        self.c = socket.socket()
        self.c.connect((host, port))
        self.c.send("REG".encode())
        print("sending REG to server")
        self.c.send("REG".encode())
        self.submit_button.setDisabled(True)
        response = self.c.recv(1024).decode()
        if response == "OK":
            print("server responded OK, sending user and pwd")
            self.c.send(pickle.dumps((self.username, self.password)))
            auth = self.c.recv(1024).decode()
            if auth == "USER_EXISTS":
                print("user already exists on the server")
                self.c.close()
                self.submit_button.setEnabled(True)
            else:
                print("We have successfully logged into the server")
        else:
            return False
    
    def send_login_msg(self):
        self.c = socket.socket()
        self.c.connect((host, port))
        self.c.send("LOG".encode())
        print("sent LOG, waiting for OK")
        
        self.submit_button.setEnabled(False)

        response = self.c.recv(1024).decode()
        if response == "OK":
            print("server responded OK, sending user and pwd")
            self.c.send(pickle.dumps((self.username, self.password)))
            auth = self.c.recv(1024).decode()
            print(auth)
            #login
            if auth == "INV_USR":
                print("user doesnt exist on server")
                self.c.close()
                self.submit_button.setEnabled(True)
            elif auth == "INV_PWD":
                print("password is wrong for user")
                self.c.close()
                self.submit_button.setEnabled(True)
            else:
                print("We have successfully logged into the server")
    
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
        if self.username == "kill":
            self.c.close()
    
    def init_ui(self):
        
        # SPLASH IMAGE
        self.hero_image = QLabel(self)
        hero = QPixmap("./images/hero.png").scaled(260, 300, Qt.AspectRatioMode.KeepAspectRatio)
        self.hero_image.setPixmap(hero)

        # WARNINGS
        self.invalid_creds = QLabel("Username or password is invalid!")
        self.invalid_creds.setFont(warning_font)
        self.invalid_creds.setStyleSheet("color: red")
        self.invalid_creds.setVisible(False)


        # USER FIELDS
        self.user_label = QLabel("Screen Name")
        self.user_label.setFont(default_font)
        self.user_field = QLineEdit()
        self.user_field.setMaxLength(16)
        self.user_field.setFixedWidth(110)
        self.user_field.textChanged.connect(self.set_creds)


        # PASSWORD FIELD
        self.pass_label = QLabel("Password")
        self.pass_label.setFont(default_font)
        self.pass_field = QLineEdit()
        self.pass_field.setFixedWidth(110)
        self.pass_field.setEchoMode(QLineEdit.EchoMode.Password)
        self.pass_field.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        self.pass_field.textChanged.connect(self.set_creds)
        self.pass_field.textChanged.connect(self.check_password_validity)

        # GENERATING H LAYOUTS
        self.screen_name = QWidget()
        screen_name_lo = QHBoxLayout()
        screen_name_lo.setSpacing(0)
        screen_name_lo.addWidget(self.user_label)
        screen_name_lo.addStretch()
        screen_name_lo.addWidget(self.user_field)
        screen_name_lo.setContentsMargins(0, 0, 0, 0)
        self.screen_name.setLayout(screen_name_lo)

        self.pwd_group = QWidget()
        password_lo = QHBoxLayout()
        password_lo.setSpacing(0)
        password_lo.addWidget(self.pass_label)
        password_lo.addStretch()
        password_lo.addWidget(self.pass_field)
        password_lo.setContentsMargins(0, 0, 0, 0)
        self.pwd_group.setLayout(password_lo)

        # LOGIN BUTTON
        self.submit_button = QPushButton()
        sign_on = QPixmap("./images/sign_on.png").scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio)
        self.submit_button.setFixedWidth(50)
        self.submit_button.setFixedHeight(50)
        self.submit_button.setFlat(True)
        self.submit_button.clicked.connect(self.send_login_msg)
        self.submit_button.setIcon(sign_on)
        self.submit_button.setIconSize(QSize(50, 50))

        # SETTING LAYOUTS
        layout = QVBoxLayout()
        layout.addWidget(self.hero_image)
        fields = QWidget()
        fields_layout = QVBoxLayout()
        fields_layout.addWidget(self.screen_name)
        fields_layout.addSpacing(10)
        fields_layout.addWidget(self.pwd_group)
        fields_layout.addSpacing(5)
        fields_layout.addWidget(self.invalid_creds)
        fields_layout.addStretch(1)
        fields_layout.addWidget(self.submit_button) 
        fields_layout.setSpacing(0)
        fields.setLayout(fields_layout)
        layout.addWidget(fields)
        layout.setSpacing(5)
        self.setLayout(layout)



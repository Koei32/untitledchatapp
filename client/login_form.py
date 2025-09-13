from PySide6.QtWidgets import (
    QWidget,
    QPushButton,
    QLineEdit,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QSizePolicy,
    QMainWindow,
    QFrame
)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt, QSize
import pickle
import socket
from fonts import warning_font, default_font
from util_functions import VALID_CHARS, VALID_USR_CHARS
from config import ConfigManager

cfgmgr = ConfigManager()
host = cfgmgr.host
port = cfgmgr.port


class LoginForm(QMainWindow):
    def __init__(self, client):
        super().__init__()
        self.client = client
        self.init_ui()

    def send_reg_msg(self):
        match self.check_cred_validity():
            case 1:
                self.set_and_show_info("Screen Name cannot be empty!", "orange")
                return
            case 2:
                self.set_and_show_info("Password must be atleast 8 characters!", "orange")
                return
            case 3:
                self.set_and_show_info("Password contains invalid characters!", "orange")
                return
            case 4:
                self.set_and_show_info("Screen Name contains special characters!", "orange")
                return
        
        try:
            self.client.c = socket.socket()
            self.client.c.connect((host, port))
            self.client.c.send("REG".encode())
            print("sending REG to server, waiting for OK")

            self.set_ui_interactable(False)

            response = self.client.c.recv(1024).decode()
            if response == "OK":
                print("server responded OK, sending user and pwd")
                self.client.c.send(pickle.dumps((self.username, self.password)))
                auth = self.client.c.recv(1024).decode()
                if auth == "USER_EXISTS":
                    print("user already exists on the server")
                    self.set_and_show_info("User already exists", "red")
                    self.client.c.close()
                    self.set_ui_interactable(True)
                else:
                    self.set_and_show_info("Successfully created account!", "green")
                    print("Successfully created account!")
                    self.client.user = self.username

                    self.client.c.send("GET_USERS".encode())
                    user_list = self.client.c.recv(1024)
                    self.client.user_list = pickle.loads(user_list)

                    self.client.show_buddylist()
                    self.client.start_listener_thread()
        except ConnectionRefusedError or ConnectionAbortedError or TimeoutError:
            self.set_and_show_info("Could not connect to server.", "red")

    def send_login_msg(self):
        match self.check_cred_validity():
            case 1:
                self.set_and_show_info("Screen Name cannot be empty!", "orange")
                return
            case 2:
                self.set_and_show_info("Password must be atleast 8 characters!", "orange")
                return
            case 3:
                self.set_and_show_info("Password contains invalid characters!", "orange")
                return
            case 4:
                self.set_and_show_info("Screen Name contains special characters!", "orange")
                return
        
        try:
            self.client.c = socket.socket()
            self.client.c.connect((host, port))
            self.client.c.send("LOG".encode())
            print("sent LOG, waiting for OK")

            self.set_ui_interactable(False)

            response = self.client.c.recv(1024).decode()
            if response == "OK":
                print("server responded OK, sending user and pwd")
                self.client.c.send(pickle.dumps((self.username, self.password)))
                auth = self.client.c.recv(1024).decode()
                print(auth)
                # login
                if auth == "INV_USR":
                    print("user doesnt exist on server")
                    self.set_and_show_info("Invalid user or password", "red")
                    self.client.c.close()
                    self.set_ui_interactable(True)
                elif auth == "INV_PWD":
                    print("password is wrong for user")
                    self.set_and_show_info("Invalid user or password", "red")
                    self.client.c.close()
                    self.set_ui_interactable(True)
                else:
                    print("We have successfully logged into the server")
                    self.set_and_show_info("Logged in!", "green")
                    self.client.user = self.username
                    
                    self.client.c.send("GET_USERS".encode())
                    user_list = self.client.c.recv(1024)
                    self.client.user_list = pickle.loads(user_list)
                    
                    # self.client.show_messenger_window("mito") #temp: should be buddy list
                    self.client.show_buddylist()
                    self.client.start_listener_thread()
        except ConnectionRefusedError or ConnectionAbortedError or TimeoutError:
            self.set_and_show_info("Could not connect to server.", "red")

    def check_cred_validity(self) -> int:
        if len(self.username) == 0:
            self.set_ui_interactable(False)
            return 1
        if len(self.password) < 4:
            self.set_ui_interactable(False)
            return 2
        for chr in self.username:
            if chr not in VALID_USR_CHARS:
                return 4
        for chr in self.password:
            if chr not in VALID_CHARS:
                self.set_ui_interactable(False)
                return 3
        self.set_ui_interactable(True)
        return 0

    def set_creds(self):
        # self.invalid_creds.setVisible(False)
        self.password = self.pass_field.text()
        self.username = self.user_field.text()
        if self.username == "kill":
            self.client.c.close()
        self.check_cred_validity()
    
    def set_and_show_info(self, message: str, color: str):
        self.invalid_creds.setText(message)
        self.invalid_creds.setStyleSheet(f"color: {color}")
        self.invalid_creds.setVisible(True)

    def set_ui_interactable(self, state: bool):
        self.login_button.setEnabled(state)
        self.register_button.setEnabled(state)

    def init_ui(self):
        self.setWindowTitle("Sign On")
        self.setFixedSize(200, 300)
        # SPLASH IMAGE
        self.hero_image = QLabel(self)
        hero = QPixmap("./images/hero.png").scaled(
            180, 200, Qt.AspectRatioMode.KeepAspectRatio
        )
        self.hero_image.setPixmap(hero)
        self.setContentsMargins(0,0,0,0)

        # SEPARATOR
        separator = QFrame()
        separator.setFrameShape(QFrame.Shape.HLine)
        separator.setFrameShadow(QFrame.Shadow.Sunken)

        # WARNINGS
        self.invalid_creds = QLabel("Username or password is invalid!")
        self.invalid_creds.setFont(warning_font)
        self.invalid_creds.setStyleSheet("color: red")
        self.invalid_creds.setVisible(False)

        # USER FIELDS
        self.user_label = QLabel("Screen Name")
        self.user_label.setFont(default_font)
        self.user_field = QLineEdit()
        self.user_field.returnPressed.connect(self.send_login_msg)
        self.user_field.setMaxLength(16)
        self.user_field.setFixedWidth(110)
        self.user_field.textChanged.connect(self.set_creds)
        self.username = self.user_field.text()

        
        # PASSWORD FIELD
        self.pass_label = QLabel("Password")
        self.pass_label.setFont(default_font)
        self.pass_field = QLineEdit()
        self.pass_field.returnPressed.connect(self.send_login_msg)
        self.pass_field.setFixedWidth(110)
        self.pass_field.setEchoMode(QLineEdit.EchoMode.Password)
        self.pass_field.setSizePolicy(
            QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed
        )
        self.pass_field.textChanged.connect(self.set_creds)
        self.password = self.pass_field.text()


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
        self.login_button = QPushButton()
        sign_on = QPixmap("./images/signon.png")
        self.login_button.setFixedSize(48, 38)
        self.login_button.setFlat(True)
        self.login_button.clicked.connect(self.send_login_msg)
        self.login_button.setIcon(sign_on)
        self.login_button.setIconSize(QSize(48, 38))

        # REGISTER BUTTON
        # sign_on = QPixmap("./images/sign_on.png").scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio)
        self.register_button = QPushButton("Register")
        self.register_button.setFixedWidth(50)
        self.register_button.setFixedHeight(50)
        self.register_button.setFlat(True)
        self.register_button.clicked.connect(self.send_reg_msg)
        self.register_button.setIconSize(QSize(50, 50))

        # SETTING LAYOUTS
        layout = QVBoxLayout()
        layout.addWidget(self.hero_image)
        layout.addWidget(separator)
        fields = QWidget()
        fields_layout = QVBoxLayout()
        fields_layout.addWidget(self.screen_name)
        fields_layout.addSpacing(10)
        fields_layout.addWidget(self.pwd_group)
        fields_layout.addSpacing(5)
        fields_layout.addWidget(self.invalid_creds)
        fields_layout.addStretch(1)
        fields_layout.setContentsMargins(0,0,0,0)

        buttons = QWidget()
        buttons_layout = QHBoxLayout()
        buttons_layout.setContentsMargins(0, 0, 0, 0)
        buttons_layout.addWidget(self.register_button)
        buttons_layout.addStretch()
        buttons_layout.addWidget(self.login_button)
        buttons.setLayout(buttons_layout)

        fields_layout.addWidget(buttons)
        fields_layout.setSpacing(0)
        fields.setLayout(fields_layout)
        layout.addWidget(fields)
        layout.setSpacing(5)
        wrapper = QWidget()
        wrapper.setLayout(layout)
        self.setCentralWidget(wrapper)


    

  
from PySide6.QtWidgets import QApplication, QStyleFactory
from PySide6.QtGui import QFont
import sys
from config import ConfigManager
from login_form import LoginForm
from message import MessengerWindow
import socket


#
#
# TODO: CHECK PASSWORD VALIDITY
# TODO: STORE HASHED PASSWORDS and CHECK WITH HASH (salt and all)
# TODO: ADD TAB SWITCHING FOR REG/LOGIN
#
#



class Client():
    def __init__(self, client: socket.socket):
        self.c = client
        cfg_mgr = ConfigManager()
        self.style = cfg_mgr.style

        app = QApplication(sys.argv)
        app.setStyleSheet(self.style)

        self.show_login_window()
        app.exec()


    def show_login_window(self):
        self.login_window = LoginForm(self)
        self.login_window.show()
    
    def show_messenger_window(self):
        self.login_window.close()
        self.msg_window = MessengerWindow(self)
        self.msg_window.show()
        

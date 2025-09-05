from PySide6.QtWidgets import QApplication, QStyleFactory
from PySide6.QtGui import QFont
import sys
from config import ConfigManager
from login_form import LoginForm
from message import MessengerWindow
import socket
import threading
from util_functions import parse_msg


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
        self.msg_window = MessengerWindow(self, "mito")
        self.msg_window.show()
    
    def received_message(self, sender, receiver, content):
        print(f"{sender} is sending you '{content}'")

    def start_listener_thread(self):
        listener = threading.Thread(target=listen, args=(self,), daemon=True)
        listener.start()

def listen(client: Client):
    while True:
        try:
            while True:
                message = client.c.recv(1024)
                sender, receiver, content = parse_msg(message)
                client.received_message(sender, receiver, content)
        except:
            pass



from PySide6.QtWidgets import QApplication, QStyleFactory
from PySide6.QtGui import QFont, QPalette, QColor
from PySide6.QtCore import QObject, Signal
from PySide6 import QtCore
import sys
import socket
import threading
from util_functions import parse_msg
from fonts import main_pallete

from config import ConfigManager
from login_form import LoginForm
from messenger import MessengerWindow
from buddy_list import BuddyList

#
#
# TODO: CHECK PASSWORD VALIDITY
# TODO: STORE HASHED PASSWORDS and CHECK WITH HASH (salt and all)
#
#


class Client():
    signal_start_msg_listener = Signal(str)
    def __init__(self, client: socket.socket):
        self.c = client
        self.user = None
        self.user_list = []
        cfg_mgr = ConfigManager()

        self.msg_mgr = MessageManager()

        self.msg_windows = {}

        self.msg_listener = MessageListener(self)
        self.msg_listener_thread = QtCore.QThread()
        self.msg_listener.moveToThread(self.msg_listener_thread)
        
        self.msg_mgr.signal_start_listener.connect(self.msg_listener.listen)
        self.msg_mgr.signal_message_received.connect(self.on_received_message)

        app = QApplication(sys.argv)
        app.setDesktopSettingsAware(False)
        app.setStyle(QStyleFactory.create("Windows"))
        app.setPalette(main_pallete())

        self.show_login_window()
        app.exec()

    def show_login_window(self):
        self.login_window = LoginForm(self)
        self.login_window.show()

    def show_buddylist(self):
        self.login_window.close()
        self.buddylist = BuddyList(self)
        self.buddylist.show()

    def show_messenger_window(self, buddy):
        self.login_window.close()
        self.msg_windows[buddy] = MessengerWindow(self, buddy)
        self.msg_windows[buddy].show()

    @QtCore.Slot()
    def on_received_message(self, data: tuple):
        print(f"{data[0]} is sending you '{data[2]}'")
        self.msg_windows[data[0]].add_message_entry(data[0], data[2])

    def start_listener_thread(self):
        self.msg_listener_thread.start()
        self.msg_mgr.signal_start_listener.emit()

# qthread implementation

class MessageListener(QObject):

    def __init__(self, client: Client):
        super().__init__()
        self.client = client
        self.msg_manager = self.client.msg_mgr

    @QtCore.Slot()
    def listen(self):
        print("listener thread started")
        while True:
            try:
                while True:
                    message = self.client.c.recv(1024)
                    sender, receiver, content = parse_msg(message)
                    print(f"{sender}: {content}")
                    self.msg_manager.signal_message_received.emit((sender, receiver, content))
            except Exception as e:
                print(e)

class MessageManager(QObject):
    signal_message_received = Signal(tuple)
    signal_start_listener = Signal()
    def __init__(self):
        super().__init__()


from PySide6.QtWidgets import (
    QWidget,
    QPushButton,
    QLineEdit,
    QTextEdit,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QSizePolicy,
    QMainWindow,
)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt, QSize, QUrl
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput, QSoundEffect
import pickle
import socket
from fonts import warning_font, default_font
from config import ConfigManager


cfgmgr = ConfigManager()


class MessengerWindow(QMainWindow):
    def __init__(self, client, receiver: str):
        super().__init__()
        self.setWindowTitle(receiver)
        self.client = client
        self.user = client.user
        self.receiver = receiver
        
        self.init_ui()
      
    def send_msg(self):
        header = self.user + "-" + self.receiver + ";"
        message = header + self.chat_field.text()
        self.client.c.send(message.encode())
        self.chat_field.clear()
    
    def init_ui(self):
        self.wrapper = QWidget()

        chat = QWidget()
        self.chat_field = QLineEdit()
        self.chat_field.returnPressed.connect(self.send_msg)
        send_btn = QPushButton("Send")
        send_btn.clicked.connect(self.send_msg)
        layout = QHBoxLayout()
        layout.addWidget(self.chat_field)
        layout.addWidget(send_btn)
        chat.setLayout(layout)

        self.wrapper_layout = QVBoxLayout()
        self.wrapper_layout.addWidget(chat)
        self.wrapper.setLayout(self.wrapper_layout)
        self.setCentralWidget(self.wrapper)
    
    def add_message_entry(self, sender, content):
        self.wrapper_layout.addWidget(MessageEntry(sender, content, ""))
        self.wrapper.setLayout(self.wrapper_layout)
        self.setLayout(self.wrapper_layout)
    

class MessageEntry(QWidget):
    def __init__(self, user, message, time):
        super().__init__()
        layout = QHBoxLayout()
        user_label = QLabel(user)
        message_text = QLabel(message)
        layout.addWidget(user_label)
        # layout.addStretch(1)
        layout.addWidget(message_text)
        self.setLayout(layout)


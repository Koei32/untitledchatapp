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
from PySide6.QtCore import Qt, QSize
import pickle
import socket
from fonts import warning_font, default_font
from config import ConfigManager


class MessengerWindow(QMainWindow):
    def __init__(self, client, receiver: str):
        super().__init__()
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
        chat = QWidget()
        self.chat_field = QLineEdit()
        self.chat_field.returnPressed.connect(self.send_msg)
        send_btn = QPushButton("Send")
        send_btn.clicked.connect(self.send_msg)
        layout = QHBoxLayout()
        layout.addWidget(self.chat_field)
        layout.addWidget(send_btn)
        chat.setLayout(layout)
        self.setCentralWidget(chat)
    

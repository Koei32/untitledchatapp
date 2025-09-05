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
    def __init__(self, client):
        super().__init__()
        self.client = client
        chat = QWidget()
        self.chat_field = QLineEdit()
        send_btn = QPushButton("Send")
        send_btn.clicked.connect(self.send_msg)
        layout = QHBoxLayout()
        layout.addWidget(self.chat_field)
        layout.addWidget(send_btn)
        chat.setLayout(layout)
        self.setCentralWidget(chat)
    
    def send_msg(self):
        self.client.c.send(self.chat_field.text().encode())

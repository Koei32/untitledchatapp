from PySide6.QtWidgets import (
    QWidget,
    QPushButton,
    QLineEdit,
    QVBoxLayout,
    QHBoxLayout,
    QListView,
    QStackedLayout,
    QTreeWidget,
    QLabel,
    QSizePolicy,
    QLayout,
    QTreeWidgetItem,
    QMainWindow,
)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt, QSize
import pickle
import socket
from fonts import warning_font, default_font
from util_functions import VALID_CHARS
from config import ConfigManager



class BuddyList(QMainWindow):
    def __init__(self, client):
        super().__init__()
        self.client = client
        self.init_ui()
    
    def init_ui(self):
        self.setWindowTitle(f"{self.client.user}'s Buddy List")
        self.setFixedSize(180, 400)
        self.setMaximumSize(180, 400)
        self.setContentsMargins(0, 0, 0, 0)


        wrapper = QWidget()
        wrapper_layout = QVBoxLayout()
        wrapper_layout.setContentsMargins(0, 0, 0, 0)
        wrapper_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        wrapper.setLayout(wrapper_layout)


        # HERO IMAGE
        hero_image = QLabel()
        hero = QPixmap("./images/hero.png").scaled(
            90, 200, Qt.AspectRatioMode.KeepAspectRatio
        )
        hero_image.setPixmap(hero)
        wrapper_layout.addWidget(hero_image)


        # ONLINE LIST
        online_list_wrapper = QWidget()
        online_list_wrapper_layout = QStackedLayout()
        online_list_wrapper.setLayout(online_list_wrapper_layout)
        online_list = QTreeWidget()
        online_list.setHeaderHidden(True)
        buddies = QTreeWidgetItem(online_list, ["Buddies"])
        for user in self.client.user_list:
            x = QTreeWidgetItem(buddies, [user])

        online_list.itemDoubleClicked.connect(self.open_msg_window)

        online_list_wrapper_layout.addWidget(online_list)
        wrapper_layout.addWidget(online_list_wrapper)
        self.setCentralWidget(wrapper)
    
    def open_msg_window(self, listitem):
        self.client.show_messenger_window(listitem.text(0))


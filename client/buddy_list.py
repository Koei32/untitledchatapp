from PySide6.QtWidgets import (
    QWidget,
    QPushButton,
    QLineEdit,
    QVBoxLayout,
    QHBoxLayout,
    QListView,
    QStackedLayout,
    QLabel,
    QSizePolicy,
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

    def init_ui(self):
        self.setWindowTitle(f"{self.client.user}'s Buddy List")
        self.setFixedSize(180, 400)
        self.setContentsMargins(0, 0, 0, 0)

        # HERO IMAGE
        hero_image = QLabel(self)
        hero = QPixmap("./images/hero.png").scaled(
            180, 200, Qt.AspectRatioMode.KeepAspectRatio
        )
        hero_image.setPixmap(hero)

        # ONLINE LIST
        online_list_wrapper_layout = QStackedLayout()
        online_list = QWidget()
        online_list_layout = QVBoxLayout()

        online_list_wrapper_layout.addWidget(online_list)


        





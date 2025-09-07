from PySide6.QtWidgets import (
    QWidget,
    QPushButton,
    QLineEdit,
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
from util_functions import VALID_CHARS
from config import ConfigManager


class BuddyList(QMainWindow):
    def __init__(self):
        super().__init__()
        


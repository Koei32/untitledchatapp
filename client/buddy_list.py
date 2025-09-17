from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QStackedLayout,
    QTreeWidget,
    QLabel,
    QFrame,
    QTreeWidgetItem,
    QMainWindow,
)
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtCore import Qt
from config import ConfigManager

cfg_mgr = ConfigManager()

class BuddyList(QMainWindow):
    def __init__(self, client):
        super().__init__()
        self.client = client
        self.client.play_sound(cfg_mgr.sounds_path + "buddyin.wav", 0.5)
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle(f"{self.client.user}'s Buddy List")
        self.setWindowIcon(QIcon(cfg_mgr.img_path + "buddylist.ico"))
        self.setFixedSize(200, 400)
        self.setMaximumSize(200, 400)
        self.setContentsMargins(0, 0, 0, 0)

        wrapper = QWidget()
        wrapper_layout = QVBoxLayout()
        wrapper_layout.setContentsMargins(5, 5, 5, 5)
        wrapper.setLayout(wrapper_layout)

        # HERO IMAGE
        hero_image = QLabel()
        hero = QPixmap(cfg_mgr.img_path + "hero.png").scaled(
            100, 100, Qt.AspectRatioMode.KeepAspectRatio
        )
        hero_image.setPixmap(hero)
        hero_image.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        wrapper_layout.addWidget(hero_image)

        separator = QFrame()
        separator.setFrameShape(QFrame.Shape.HLine)
        separator.setFrameShadow(QFrame.Shadow.Sunken)
        wrapper_layout.addWidget(separator)

        # ONLINE LIST
        online_list_wrapper = QWidget()
        online_list_wrapper_layout = QStackedLayout()
        online_list_wrapper.setLayout(online_list_wrapper_layout)
        online_list = QTreeWidget()
        online_list.setHeaderHidden(True)
        buddies = QTreeWidgetItem(online_list, ["Buddies"])
        buddies.setExpanded(True)
        for user in self.client.user_list:
            x = QTreeWidgetItem(buddies, [user])

        online_list.itemDoubleClicked.connect(self.open_msg_window)
        online_list_wrapper_layout.addWidget(online_list)

        wrapper_layout.addWidget(online_list_wrapper)
        self.setCentralWidget(wrapper)

    def open_msg_window(self, listitem):
        if listitem.text(0) == "Buddies":
            return
        self.client.show_messenger_window(listitem.text(0))
    


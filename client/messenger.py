from PySide6.QtGui import QCloseEvent
from PySide6.QtWidgets import (
    QWidget,
    QPushButton,
    QLineEdit,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QTextEdit,
    QListWidget,
    QSizePolicy,
    QScrollArea,
    QFrame,
)
from config import ConfigManager
from PySide6.QtCore import Qt, QEvent

cfgmgr = ConfigManager()


class MessengerWindow(QMainWindow):
    def __init__(self, client, receiver: str):
        super().__init__()
        self.client = client
        self.user = client.user
        self.receiver = receiver

        self.init_ui()

    def send_msg(self):
        if len(self.chat_field.toPlainText().strip()) == 0:
            return
        header = self.user + "-" + self.receiver + ";"
        message = header + self.chat_field.toPlainText()
        self.client.c.send(message.encode())
        self.add_message_entry(self.user, self.chat_field.toPlainText())
        self.chat_field.clear()

    def init_ui(self):
        self.setWindowTitle(self.receiver)
        self.setFixedSize(600, 350)
        self.wrapper = QWidget()

        self.chat_log_frame = QTextEdit()
        self.chat_log_frame.setAcceptRichText(True)
        self.chat_log_frame.setReadOnly(True)
        self.chat_log_frame.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.chat_log_frame.resize(600, 300)

        # chat controls
        self.chat_controls = QWidget()
        self.chat_field = QTextEdit()
        self.chat_field.installEventFilter(self)
        send_btn = QPushButton("Send")
        send_btn.clicked.connect(self.send_msg)
        self.chat_controls_layout = QHBoxLayout()
        self.chat_controls_layout.addWidget(self.chat_field)
        self.chat_controls_layout.addWidget(send_btn)
        self.chat_controls.setLayout(self.chat_controls_layout)

        self.wrapper_layout = QVBoxLayout()
        self.wrapper_layout.addWidget(self.chat_log_frame)
        self.wrapper_layout.addWidget(self.chat_controls)
        self.wrapper.setLayout(self.wrapper_layout)
        self.setCentralWidget(self.wrapper)

    def closeEvent(self, event: QCloseEvent) -> None:
        self.client.msg_windows.pop(self.receiver)

    def add_message_entry(self, sender: str, content: str):
        user_msg_style = "color: red; font-family: 'Times New Roman'"
        msg_style = "color: blue; font-family: 'Times New Roman'"
        if sender == self.client.user:
            self.chat_log_frame.append(
                f'<b style="{user_msg_style}">{sender}</b>: {content}'
            )
        else:
            self.chat_log_frame.append(
                f'<b style="{msg_style}">{sender}</b>: {content}'
            )
        # self.chat_log.setLayout(self.chat_log_layout)
        # self.chat_log_frame.setWidget(self.chat_log)

    def eventFilter(self, obj, event):
        if event.type() == QEvent.Type.KeyPress and obj is self.chat_field:
            if event.key() == Qt.Key.Key_Return and self.chat_field.hasFocus():
                self.send_msg()
                return True
        return False


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
        self.setFixedHeight(12)

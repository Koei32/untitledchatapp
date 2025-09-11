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
    QFrame
)
from config import ConfigManager
from PySide6.QtCore import Qt

cfgmgr = ConfigManager()

class MessengerWindow(QMainWindow):
    def __init__(self, client, receiver: str):
        super().__init__()
        self.client = client
        self.user = client.user
        self.receiver = receiver

        self.init_ui()
      
    def send_msg(self):
        if len(self.chat_field.text().strip()) == 0:
            return
        header = self.user + "-" + self.receiver + ";"
        message = header + self.chat_field.text()
        self.client.c.send(message.encode())
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
        self.chat_field = QLineEdit()
        self.chat_field.returnPressed.connect(self.send_msg)
        send_btn = QPushButton("Send")
        send_btn.clicked.connect(self.send_msg)
        self.chat_controls_layout = QHBoxLayout()
        self.chat_controls_layout.addWidget(self.chat_field)
        self.chat_controls_layout.addWidget(send_btn)
        self.chat_controls.setLayout(self.chat_controls_layout)


        self.wrapper_layout = QVBoxLayout()
        self.wrapper_layout.addWidget(self.chat_log_frame)
        self.wrapper_layout.addWidget(self.chat_controls)
        message = MessageEntry("system", "Welcome", "")
        self.wrapper_layout.addWidget(message)
        self.wrapper.setLayout(self.wrapper_layout)
        self.setCentralWidget(self.wrapper)
    
    def add_message_entry(self, sender, content):
        '''
        message = QWidget()
        layout = QHBoxLayout()
        user_label = QLabel(sender)
        message_text = QLabel(content)
        layout.addWidget(user_label)
        layout.addWidget(message_text)
        message.setLayout(layout)
        message.setFixedHeight(12)

        label = QLabel(f"{sender}: {content}")
        label.setFixedWidth(450)

        self.chat_log_layout.addWidget(label)
        self.chat_log.resize(450 ,len(self.chat_log.children()) * 14)
        print(self.chat_log.size())
        print(self.chat_log_frame.size())
        print(label.size())
        '''
        user_msg_style = "color: red; font-family: 'Times New Roman'"
        msg_style = "color: blue; font-family: 'Times New Roman'"
        if sender == self.client.user:
            self.chat_log_frame.append(f'<b style="{user_msg_style}">{sender}</b>: {content}')
        else:
            self.chat_log_frame.append(f'<b style="{msg_style}">{sender}</b>: {content}')
        # self.chat_log.setLayout(self.chat_log_layout)
        # self.chat_log_frame.setWidget(self.chat_log)
    

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


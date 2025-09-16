from PySide6.QtGui import QCloseEvent
from PySide6.QtWidgets import (
    QWidget,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QMainWindow,
    QTextEdit,
    QFrame,
)
from config import ConfigManager
from PySide6.QtCore import Qt, QEvent, QSize
from PySide6.QtGui import QPixmap

cfgmgr = ConfigManager()

# device = QAudioDevice()
# imrcv.setAudioDevice(device)
# imsend = QSoundEffect(cfgmgr.sounds_path + "imsend.wav")



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
        self.client.play_sound("./sounds/imsend.wav")
        self.chat_field.clear()

    def init_ui(self):
        self.setWindowTitle(f"{self.receiver} - Instant Message")
        self.setFixedSize(600, 350)
        self.wrapper = QWidget()

        self.chat_log_frame = QTextEdit()
        self.chat_log_frame.setAcceptRichText(True)
        self.chat_log_frame.setReadOnly(True)
        self.chat_log_frame.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.chat_log_frame.setStyleSheet("font-size: 12pt; font-family: 'Times New Roman'")
        # self.chat_log_frame.setStyleSheet("font-family: 'Times New Roman'")

        self.chat_log_frame.resize(600, 300)

        # chat controls
        self.chat_controls = QWidget()
        self.chat_controls.setFixedHeight(150)
        self.chat_field = QTextEdit()
        self.chat_field.installEventFilter(self)

        #separator
        separator = QFrame()
        separator.setFrameShape(QFrame.Shape.HLine)
        separator.setFrameShadow(QFrame.Shadow.Sunken)

        #buttons
        buttons = QWidget()
        buttons_layout = QHBoxLayout()
        exit_btn = QPushButton("Exit")
        exit_btn.clicked.connect(self.close)
        send_btn = QPushButton()
        exit = QPixmap("./images/send.png")
        send_btn.setFixedSize(48, 40)
        send_btn.setIcon(exit)
        send_btn.setIconSize(QSize(60, 50))
        buttons_layout.addWidget(exit_btn)
        buttons_layout.addStretch()
        buttons_layout.addWidget(send_btn)
        buttons.setLayout(buttons_layout)

        send_btn.clicked.connect(self.send_msg)
        self.chat_controls_layout = QVBoxLayout()
        self.chat_controls_layout.addWidget(self.chat_field)
        self.chat_controls_layout.addWidget(buttons)
        self.chat_controls_layout.setContentsMargins(0, 0, 0, 0)
        self.chat_controls.setLayout(self.chat_controls_layout)

        self.wrapper_layout = QVBoxLayout()
        self.wrapper_layout.addWidget(self.chat_log_frame)
        self.wrapper_layout.addWidget(separator)
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
    

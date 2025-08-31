from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QFont
import socket
import pickle
import sys

from login_form import LoginForm

font = QFont("Trebuchet MS", 10)
font.setStyleStrategy(QFont.StyleStrategy.NoAntialias)
font.setBold(True)

host = "koei.hackclub.app"
port = 14169
c = socket.socket()


#
#
# TODO: CHECK PASSWORD VALIDITY
# TODO: STORE HASHED PASSWORDS and CHECK WITH HASH (salt and all)
# TODO: ADD TAB SWITCHING FOR REG/LOGIN
#
#


app = QApplication(sys.argv)
app.setFont(font)
window = QMainWindow()
window.setWindowTitle("Untitled Chat App")
login = LoginForm(c)
login.setFixedHeight(260)
window.setCentralWidget(login)
window.show()


app.exec()

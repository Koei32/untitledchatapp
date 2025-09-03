from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QFont
import sys

from login_form import LoginForm

font = QFont("Trebuchet MS", 10)
font.setStyleStrategy(QFont.StyleStrategy.NoAntialias)
# font.setBold(True)


#
#
# TODO: CHECK PASSWORD VALIDITY
# TODO: STORE HASHED PASSWORDS and CHECK WITH HASH (salt and all)
# TODO: ADD TAB SWITCHING FOR REG/LOGIN
#
#


app = QApplication(sys.argv)
# app.setFont(font)
window = QMainWindow()
window.setWindowTitle("Untitled Chat App")
window.setFixedSize(280, 380)
login = LoginForm()
window.setCentralWidget(login)
window.show()


app.exec()

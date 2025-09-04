from PySide6.QtWidgets import QApplication, QStyleFactory
from PySide6.QtGui import QFont
import sys
from config import ConfigManager
from login_form import LoginForm


#
#
# TODO: CHECK PASSWORD VALIDITY
# TODO: STORE HASHED PASSWORDS and CHECK WITH HASH (salt and all)
# TODO: ADD TAB SWITCHING FOR REG/LOGIN
#
#

cfg_mgr = ConfigManager()

with open(cfg_mgr.style_path + "client.qss") as qss:
    style = qss.read()

app = QApplication(sys.argv)
app.setStyleSheet(style)
# app.setFont(font)
login_window = LoginForm()
login_window.show()


app.exec()

from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

import sys

app = QApplication(sys.argv)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("This Godforsaken Chat App")
        button = QPushButton("Press Me!")
        self.setCentralWidget(button)

window = MainWindow()
window.show()

app.exec()

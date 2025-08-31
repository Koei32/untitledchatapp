# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_form.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class LoginForm(QWidget):
    def __init__(self):
        super().__init__()
        self.login_form = QWidget()
        if not self.login_form.objectName():
            self.login_form.setObjectName(u"login_form")
        self.login_form.resize(300, 480)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.login_form.sizePolicy().hasHeightForWidth())
        self.login_form.setSizePolicy(sizePolicy)
        self.pushButton = QPushButton(self.login_form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(210, 370, 80, 80))
        self.pushButton.setFlat(True)
        self.widget = QWidget(self.login_form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 10, 282, 346))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u"../images/hero.png"))

        self.verticalLayout.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer)

        self.screen_name_layout = QHBoxLayout()
        self.screen_name_layout.setObjectName(u"screen_name_layout")
        self.sn_label = QLabel(self.widget)
        self.sn_label.setObjectName(u"sn_label")

        self.screen_name_layout.addWidget(self.sn_label)

        self.user_field = QLineEdit(self.widget)
        self.user_field.setObjectName(u"user_field")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.user_field.sizePolicy().hasHeightForWidth())
        self.user_field.setSizePolicy(sizePolicy1)

        self.screen_name_layout.addWidget(self.user_field)


        self.verticalLayout.addLayout(self.screen_name_layout)

        self.pass_layout = QHBoxLayout()
        self.pass_layout.setObjectName(u"pass_layout")
        self.pass_label = QLabel(self.widget)
        self.pass_label.setObjectName(u"pass_label")

        self.pass_layout.addWidget(self.pass_label)

        self.pass_field = QLineEdit(self.widget)
        self.pass_field.setObjectName(u"pass_field")
        sizePolicy1.setHeightForWidth(self.pass_field.sizePolicy().hasHeightForWidth())
        self.pass_field.setSizePolicy(sizePolicy1)
        self.pass_field.setEchoMode(QLineEdit.EchoMode.Password)

        self.pass_layout.addWidget(self.pass_field)


        self.verticalLayout.addLayout(self.pass_layout)


        self.retranslateUi(self.login_form)

        QMetaObject.connectSlotsByName(self.login_form)
    # setupUi

    def retranslateUi(self, login_form):
        login_form.setWindowTitle(QCoreApplication.translate("login_form", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("login_form", u"Sign On", None))
        self.label.setText("")
        self.sn_label.setText(QCoreApplication.translate("login_form", u"Screen Name", None))
        self.pass_label.setText(QCoreApplication.translate("login_form", u"Password", None))
    # retranslateUi


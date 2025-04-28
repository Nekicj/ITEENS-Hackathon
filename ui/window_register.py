# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'register.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QFrame,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(461, 361)
        Dialog.setStyleSheet(u"background-color:#0a2d4d;")
        self.login = QFrame(Dialog)
        self.login.setObjectName(u"login")
        self.login.setGeometry(QRect(10, 10, 441, 341))
        self.login.setStyleSheet(u"background-color:#0a2d4d;\n"
"color: white;\n"
"border-radius: 10px;\n"
"border: 2px solid rgb(135, 135, 135);  \n"
"padding: 5px 10px;\n"
"border-color: rgb(120, 120, 120); ")
        self.login.setFrameShape(QFrame.StyledPanel)
        self.login.setFrameShadow(QFrame.Raised)
        self.register_title = QLabel(self.login)
        self.register_title.setObjectName(u"register_title")
        self.register_title.setGeometry(QRect(10, 10, 111, 31))
        font = QFont()
        font.setFamilies([u"Courier New"])
        self.register_title.setFont(font)
        self.register_title.setStyleSheet(u"background-color:#0a2d4d;\n"
"color: white;\n"
"border-radius: 0px;\n"
"border: 0px solid rgb(135, 135, 135);  \n"
"padding: 5px 10px;\n"
"border-color: rgb(120, 120, 120); ")
        self.username_register = QLineEdit(self.login)
        self.username_register.setObjectName(u"username_register")
        self.username_register.setGeometry(QRect(92, 170, 241, 31))
        self.username_register.setFont(font)
        self.username_register.setStyleSheet(u"background-color:rgba(255, 255, 255,30);\n"
"")
        self.password_register = QLineEdit(self.login)
        self.password_register.setObjectName(u"password_register")
        self.password_register.setGeometry(QRect(92, 220, 241, 31))
        self.password_register.setFont(font)
        self.password_register.setStyleSheet(u"background-color:rgba(255, 255, 255,30);\n"
"")
        self.password_register.setEchoMode(QLineEdit.Password)
        self.register_button = QPushButton(self.login)
        self.register_button.setObjectName(u"register_button")
        self.register_button.setGeometry(QRect(140, 290, 161, 31))
        self.register_button.setFont(font)
        self.see_password_cb_register = QCheckBox(self.login)
        self.see_password_cb_register.setObjectName(u"see_password_cb_register")
        self.see_password_cb_register.setGeometry(QRect(130, 260, 161, 21))
        self.see_password_cb_register.setFont(font)
        self.see_password_cb_register.setStyleSheet(u"border:0px")
        self.name_register = QLineEdit(self.login)
        self.name_register.setObjectName(u"name_register")
        self.name_register.setGeometry(QRect(92, 120, 241, 31))
        self.name_register.setFont(font)
        self.name_register.setStyleSheet(u"background-color:rgba(255, 255, 255,30);\n"
"")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.register_title.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:14pt;\">register</span></p><p><br/></p></body></html>", None))
        self.username_register.setText("")
        self.username_register.setPlaceholderText(QCoreApplication.translate("Dialog", u"Login", None))
        self.password_register.setText("")
        self.password_register.setPlaceholderText(QCoreApplication.translate("Dialog", u"Password", None))
        self.register_button.setText(QCoreApplication.translate("Dialog", u"register", None))
        self.see_password_cb_register.setText(QCoreApplication.translate("Dialog", u"\u041f\u043e\u043a\u0430\u0437\u044b\u0432\u0430\u0442\u044c \u043f\u0430\u0440\u043e\u043b\u044c", None))
        self.name_register.setText("")
        self.name_register.setPlaceholderText(QCoreApplication.translate("Dialog", u"Name", None))
    # retranslateUi


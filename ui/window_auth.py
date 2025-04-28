# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'auth.ui'
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

class Ui_User(object):
    def setupUi(self, User):
        if not User.objectName():
            User.setObjectName(u"User")
        User.resize(400, 310)
        User.setStyleSheet(u"background-color:#0a2d4d")
        self.login = QFrame(User)
        self.login.setObjectName(u"login")
        self.login.setGeometry(QRect(10, 10, 381, 291))
        self.login.setStyleSheet(u"background-color:#0a2d4d;\n"
"color: white;\n"
"border-radius: 10px;\n"
"border: 2px solid rgb(135, 135, 135);  \n"
"padding: 5px 10px;\n"
"border-color: rgb(120, 120, 120); ")
        self.login.setFrameShape(QFrame.StyledPanel)
        self.login.setFrameShadow(QFrame.Raised)
        self.login_title = QLabel(self.login)
        self.login_title.setObjectName(u"login_title")
        self.login_title.setGeometry(QRect(10, 10, 111, 31))
        font = QFont()
        font.setFamilies([u"Courier New"])
        self.login_title.setFont(font)
        self.login_title.setStyleSheet(u"background-color:#0a2d4d;\n"
"color: white;\n"
"border-radius: 0px;\n"
"border: 0px solid rgb(135, 135, 135);  \n"
"padding: 5px 10px;\n"
"border-color: rgb(120, 120, 120); ")
        self.username_login = QLineEdit(self.login)
        self.username_login.setObjectName(u"username_login")
        self.username_login.setGeometry(QRect(62, 111, 241, 31))
        self.username_login.setFont(font)
        self.username_login.setStyleSheet(u"background-color:rgba(255, 255, 255,30);\n"
"")
        self.password_login = QLineEdit(self.login)
        self.password_login.setObjectName(u"password_login")
        self.password_login.setGeometry(QRect(62, 160, 241, 31))
        self.password_login.setFont(font)
        self.password_login.setStyleSheet(u"background-color:rgba(255, 255, 255,30);\n"
"")
        self.password_login.setEchoMode(QLineEdit.Password)
        self.login_button = QPushButton(self.login)
        self.login_button.setObjectName(u"login_button")
        self.login_button.setGeometry(QRect(100, 225, 161, 31))
        self.login_button.setFont(font)
        self.see_password_cb = QCheckBox(self.login)
        self.see_password_cb.setObjectName(u"see_password_cb")
        self.see_password_cb.setGeometry(QRect(100, 200, 161, 21))
        self.see_password_cb.setFont(font)
        self.see_password_cb.setStyleSheet(u"border:0px")
        self.no_account = QPushButton(self.login)
        self.no_account.setObjectName(u"no_account")
        self.no_account.setGeometry(QRect(127, 260, 111, 26))
        font1 = QFont()
        font1.setFamilies([u"Courier New"])
        font1.setUnderline(True)
        self.no_account.setFont(font1)
        self.no_account.setStyleSheet(u"QPushButton{\n"
"	border:opx;\n"
"	text-decoration: underline; \n"
"	color: #0572ec;\n"
"	background-color: transparent; \n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"        color: #065fc7; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        color: #034ea6;\n"
"    }")

        self.retranslateUi(User)

        QMetaObject.connectSlotsByName(User)
    # setupUi

    def retranslateUi(self, User):
        User.setWindowTitle(QCoreApplication.translate("User", u"Dialog", None))
        self.login_title.setText(QCoreApplication.translate("User", u"<html><head/><body><p><span style=\" font-size:14pt;\">login</span></p></body></html>", None))
        self.username_login.setText("")
        self.username_login.setPlaceholderText(QCoreApplication.translate("User", u"Login", None))
        self.password_login.setText("")
        self.password_login.setPlaceholderText(QCoreApplication.translate("User", u"Password", None))
        self.login_button.setText(QCoreApplication.translate("User", u"Login", None))
        self.see_password_cb.setText(QCoreApplication.translate("User", u"\u041f\u043e\u043a\u0430\u0437\u044b\u0432\u0430\u0442\u044c \u043f\u0430\u0440\u043e\u043b\u044c", None))
        self.no_account.setText(QCoreApplication.translate("User", u"\u041d\u0435\u0442 \u0430\u043a\u043a\u0430\u0443\u043d\u0442\u0430?", None))
    # retranslateUi


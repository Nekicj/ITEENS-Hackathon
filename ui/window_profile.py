# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'profile.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QLabel,
    QPushButton, QSizePolicy, QTextBrowser, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(461, 360)
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
        self.profile_title = QLabel(self.login)
        self.profile_title.setObjectName(u"profile_title")
        self.profile_title.setGeometry(QRect(10, 10, 111, 31))
        font = QFont()
        font.setFamilies([u"Courier New"])
        self.profile_title.setFont(font)
        self.profile_title.setStyleSheet(u"background-color:#0a2d4d;\n"
"color: white;\n"
"border-radius: 0px;\n"
"border: 0px solid rgb(135, 135, 135);  \n"
"padding: 5px 10px;\n"
"border-color: rgb(120, 120, 120); ")
        self.profile_button = QPushButton(self.login)
        self.profile_button.setObjectName(u"profile_button")
        self.profile_button.setGeometry(QRect(140, 290, 161, 31))
        self.profile_button.setFont(font)
        self.Name_profile = QTextBrowser(self.login)
        self.Name_profile.setObjectName(u"Name_profile")
        self.Name_profile.setGeometry(QRect(80, 140, 256, 71))
        font1 = QFont()
        font1.setFamilies([u"Courier New"])
        font1.setPointSize(10)
        self.Name_profile.setFont(font1)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.profile_title.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:14pt;\">profile</span></p></body></html>", None))
        self.profile_button.setText(QCoreApplication.translate("Dialog", u"exit account", None))
        self.Name_profile.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Courier New'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Name:</p></body></html>", None))
    # retranslateUi


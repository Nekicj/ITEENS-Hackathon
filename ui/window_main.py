# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QSlider, QTextBrowser, QTextEdit, QWidget)
import ui.icons_q_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(912, 592)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.centralwidget.setStyleSheet(u"")
        self.leftMenu = QWidget(self.centralwidget)
        self.leftMenu.setObjectName(u"leftMenu")
        self.leftMenu.setGeometry(QRect(0, 0, 51, 601))
        self.leftMenu.setStyleSheet(u"background:#011f3b")
        self.first = QPushButton(self.leftMenu)
        self.first.setObjectName(u"first")
        self.first.setGeometry(QRect(10, 10, 31, 31))
        self.first.setStyleSheet(u"background:rgba(255, 255, 255,0)")
        icon = QIcon()
        icon.addFile(u"icons/home_normal.png", QSize(), QIcon.Normal, QIcon.Off)
        self.first.setIcon(icon)
        self.first.setIconSize(QSize(32, 32))
        self.third = QPushButton(self.leftMenu)
        self.third.setObjectName(u"third")
        self.third.setGeometry(QRect(10, 105, 31, 41))
        self.third.setStyleSheet(u"background-color: rgba(255,255,255,0);\n"
"\n"
"")
        icon1 = QIcon()
        icon1.addFile(u"icons/key_normal.png", QSize(), QIcon.Normal, QIcon.Off)
        self.third.setIcon(icon1)
        self.third.setIconSize(QSize(32, 32))
        self.second = QPushButton(self.leftMenu)
        self.second.setObjectName(u"second")
        self.second.setGeometry(QRect(10, 60, 31, 31))
        self.second.setStyleSheet(u"background:rgba(255, 255, 255,0)")
        icon2 = QIcon()
        icon2.addFile(u"icons/book_normal.png", QSize(), QIcon.Normal, QIcon.Off)
        self.second.setIcon(icon2)
        self.second.setIconSize(QSize(32, 32))
        self.login_button = QPushButton(self.leftMenu)
        self.login_button.setObjectName(u"login_button")
        self.login_button.setGeometry(QRect(10, 550, 31, 41))
        self.login_button.setStyleSheet(u"background-color: rgba(255,255,255,0);\n"
"\n"
"")
        icon3 = QIcon()
        icon3.addFile(u"icons/user_normal.png", QSize(), QIcon.Normal, QIcon.Off)
        self.login_button.setIcon(icon3)
        self.login_button.setIconSize(QSize(32, 32))
        self.third.raise_()
        self.second.raise_()
        self.first.raise_()
        self.login_button.raise_()
        self.menu1 = QWidget(self.centralwidget)
        self.menu1.setObjectName(u"menu1")
        self.menu1.setEnabled(True)
        self.menu1.setGeometry(QRect(50, 0, 871, 601))
        self.menu1.setStyleSheet(u"background-color:#0a2d4d")
        self.internet_security_label = QLabel(self.menu1)
        self.internet_security_label.setObjectName(u"internet_security_label")
        self.internet_security_label.setGeometry(QRect(60, 10, 741, 31))
        font = QFont()
        font.setFamilies([u"Courier New"])
        font.setPointSize(18)
        self.internet_security_label.setFont(font)
        self.internet_security_label.setStyleSheet(u"color :white\n"
"")
        self.internet_info_label = QTextBrowser(self.menu1)
        self.internet_info_label.setObjectName(u"internet_info_label")
        self.internet_info_label.setGeometry(QRect(30, 50, 421, 281))
        font1 = QFont()
        font1.setFamilies([u"Courier New"])
        font1.setPointSize(15)
        self.internet_info_label.setFont(font1)
        self.internet_info_label.setStyleSheet(u"border:2px;\n"
"color:white;\n"
"")
        self.cybersec_image_label = QLabel(self.menu1)
        self.cybersec_image_label.setObjectName(u"cybersec_image_label")
        self.cybersec_image_label.setGeometry(QRect(490, 20, 371, 341))
        self.cybersec_image_label.setStyleSheet(u"background-color:rgba(0,0,0,0);")
        self.cybersec_image_label.setPixmap(QPixmap(u":/images/images/cybersec.png"))
        self.advice_cybersec = QLabel(self.menu1)
        self.advice_cybersec.setObjectName(u"advice_cybersec")
        self.advice_cybersec.setGeometry(QRect(170, 340, 531, 21))
        font2 = QFont()
        font2.setFamilies([u"Courier New"])
        font2.setPointSize(20)
        self.advice_cybersec.setFont(font2)
        self.advice_cybersec.setStyleSheet(u"color :white;")
        self.first_advice = QTextBrowser(self.menu1)
        self.first_advice.setObjectName(u"first_advice")
        self.first_advice.setGeometry(QRect(20, 390, 201, 192))
        font3 = QFont()
        font3.setFamilies([u"Courier New"])
        self.first_advice.setFont(font3)
        self.first_advice.setStyleSheet(u"border:2px;\n"
"color:white;\n"
"")
        self.second_advice = QTextBrowser(self.menu1)
        self.second_advice.setObjectName(u"second_advice")
        self.second_advice.setGeometry(QRect(240, 390, 181, 192))
        self.second_advice.setFont(font3)
        self.second_advice.setStyleSheet(u"border:2px;\n"
"color:white;\n"
"")
        self.third_advice = QTextBrowser(self.menu1)
        self.third_advice.setObjectName(u"third_advice")
        self.third_advice.setGeometry(QRect(440, 390, 171, 192))
        self.third_advice.setFont(font3)
        self.third_advice.setStyleSheet(u"border:2px;\n"
"color:white;\n"
"")
        self.fourth_advice = QTextBrowser(self.menu1)
        self.fourth_advice.setObjectName(u"fourth_advice")
        self.fourth_advice.setGeometry(QRect(630, 390, 211, 192))
        self.fourth_advice.setFont(font3)
        self.fourth_advice.setStyleSheet(u"border:2px;\n"
"color:white;\n"
"")
        self.enum_1_label = QLabel(self.menu1)
        self.enum_1_label.setObjectName(u"enum_1_label")
        self.enum_1_label.setGeometry(QRect(70, 370, 61, 16))
        self.enum_1_label.setFont(font3)
        self.enum_1_label.setStyleSheet(u"color:white;")
        self.enum_2_label = QLabel(self.menu1)
        self.enum_2_label.setObjectName(u"enum_2_label")
        self.enum_2_label.setGeometry(QRect(270, 370, 61, 16))
        self.enum_2_label.setFont(font3)
        self.enum_2_label.setStyleSheet(u"color:white;")
        self.enum_3_label = QLabel(self.menu1)
        self.enum_3_label.setObjectName(u"enum_3_label")
        self.enum_3_label.setGeometry(QRect(460, 370, 61, 16))
        self.enum_3_label.setFont(font3)
        self.enum_3_label.setStyleSheet(u"color:white;")
        self.enum_4_label = QLabel(self.menu1)
        self.enum_4_label.setObjectName(u"enum_4_label")
        self.enum_4_label.setGeometry(QRect(650, 370, 61, 16))
        self.enum_4_label.setFont(font3)
        self.enum_4_label.setStyleSheet(u"color:white;")
        self.internet_info_label_frame = QFrame(self.menu1)
        self.internet_info_label_frame.setObjectName(u"internet_info_label_frame")
        self.internet_info_label_frame.setGeometry(QRect(30, 50, 421, 261))
        self.internet_info_label_frame.setStyleSheet(u"background-color:rgba(255,255,255,30);\n"
"border-radius:10px;")
        self.internet_info_label_frame.setFrameShape(QFrame.StyledPanel)
        self.internet_info_label_frame.setFrameShadow(QFrame.Raised)
        self.internet_security_label_frame = QFrame(self.menu1)
        self.internet_security_label_frame.setObjectName(u"internet_security_label_frame")
        self.internet_security_label_frame.setGeometry(QRect(50, 10, 751, 31))
        self.internet_security_label_frame.setStyleSheet(u"background-color:rgba(255,255,255,30);\n"
"border-radius:10px;")
        self.internet_security_label_frame.setFrameShape(QFrame.StyledPanel)
        self.internet_security_label_frame.setFrameShadow(QFrame.Raised)
        self.first_advice_frame = QFrame(self.menu1)
        self.first_advice_frame.setObjectName(u"first_advice_frame")
        self.first_advice_frame.setGeometry(QRect(20, 390, 201, 181))
        self.first_advice_frame.setStyleSheet(u"background-color:rgba(255,255,255,30);\n"
"border-radius:10px;")
        self.first_advice_frame.setFrameShape(QFrame.StyledPanel)
        self.first_advice_frame.setFrameShadow(QFrame.Raised)
        self.second_advice_frame = QFrame(self.menu1)
        self.second_advice_frame.setObjectName(u"second_advice_frame")
        self.second_advice_frame.setGeometry(QRect(240, 390, 181, 181))
        self.second_advice_frame.setStyleSheet(u"background-color:rgba(255,255,255,30);\n"
"border-radius:10px;")
        self.second_advice_frame.setFrameShape(QFrame.StyledPanel)
        self.second_advice_frame.setFrameShadow(QFrame.Raised)
        self.third_advice_frame = QFrame(self.menu1)
        self.third_advice_frame.setObjectName(u"third_advice_frame")
        self.third_advice_frame.setGeometry(QRect(440, 390, 161, 181))
        self.third_advice_frame.setStyleSheet(u"background-color:rgba(255,255,255,30);\n"
"border-radius:10px;")
        self.third_advice_frame.setFrameShape(QFrame.StyledPanel)
        self.third_advice_frame.setFrameShadow(QFrame.Raised)
        self.fourth_advice_frame = QFrame(self.menu1)
        self.fourth_advice_frame.setObjectName(u"fourth_advice_frame")
        self.fourth_advice_frame.setGeometry(QRect(630, 390, 211, 181))
        self.fourth_advice_frame.setStyleSheet(u"background-color:rgba(255,255,255,30);\n"
"border-radius:10px;")
        self.fourth_advice_frame.setFrameShape(QFrame.StyledPanel)
        self.fourth_advice_frame.setFrameShadow(QFrame.Raised)
        self.advice_cybersec_frame = QFrame(self.menu1)
        self.advice_cybersec_frame.setObjectName(u"advice_cybersec_frame")
        self.advice_cybersec_frame.setGeometry(QRect(160, 340, 541, 21))
        self.advice_cybersec_frame.setStyleSheet(u"background-color:rgba(255,255,255,30);\n"
"border-radius:10px;")
        self.advice_cybersec_frame.setFrameShape(QFrame.StyledPanel)
        self.advice_cybersec_frame.setFrameShadow(QFrame.Raised)
        self.internet_security_label.raise_()
        self.internet_info_label.raise_()
        self.cybersec_image_label.raise_()
        self.advice_cybersec.raise_()
        self.first_advice.raise_()
        self.second_advice.raise_()
        self.third_advice.raise_()
        self.fourth_advice.raise_()
        self.enum_1_label.raise_()
        self.enum_2_label.raise_()
        self.enum_3_label.raise_()
        self.enum_4_label.raise_()
        self.internet_info_label_frame.raise_()
        self.internet_security_label_frame.raise_()
        self.first_advice_frame.raise_()
        self.second_advice_frame.raise_()
        self.third_advice_frame.raise_()
        self.advice_cybersec_frame.raise_()
        self.fourth_advice_frame.raise_()
        self.menu2 = QWidget(self.centralwidget)
        self.menu2.setObjectName(u"menu2")
        self.menu2.setEnabled(True)
        self.menu2.setGeometry(QRect(50, 0, 871, 601))
        self.menu2.setStyleSheet(u"background-color:#0a2d4d")
        self.cipher_info_label = QTextBrowser(self.menu2)
        self.cipher_info_label.setObjectName(u"cipher_info_label")
        self.cipher_info_label.setGeometry(QRect(10, 40, 381, 161))
        self.cipher_info_label.setFont(font3)
        self.cipher_info_label.setFocusPolicy(Qt.NoFocus)
        self.cipher_info_label.setStyleSheet(u"border:2px;\n"
"color:white;\n"
"color:white;")
        self.cipher_kinds_title_label = QLabel(self.menu2)
        self.cipher_kinds_title_label.setObjectName(u"cipher_kinds_title_label")
        self.cipher_kinds_title_label.setGeometry(QRect(80, 210, 241, 21))
        self.cipher_kinds_title_label.setFont(font3)
        self.cipher_kinds_title_label.setStyleSheet(u"\n"
"color:white;")
        self.cipher_kind_1 = QTextBrowser(self.menu2)
        self.cipher_kind_1.setObjectName(u"cipher_kind_1")
        self.cipher_kind_1.setGeometry(QRect(10, 240, 161, 171))
        self.cipher_kind_1.setFont(font3)
        self.cipher_kind_1.setStyleSheet(u"border:2px;\n"
"color:white;\n"
"")
        self.cipher_kind_2 = QTextBrowser(self.menu2)
        self.cipher_kind_2.setObjectName(u"cipher_kind_2")
        self.cipher_kind_2.setGeometry(QRect(180, 240, 211, 171))
        self.cipher_kind_2.setFont(font3)
        self.cipher_kind_2.setStyleSheet(u"border:2px;\n"
"color:white;\n"
"")
        self.cipher_kind_3 = QTextBrowser(self.menu2)
        self.cipher_kind_3.setObjectName(u"cipher_kind_3")
        self.cipher_kind_3.setGeometry(QRect(10, 420, 381, 101))
        self.cipher_kind_3.setFont(font3)
        self.cipher_kind_3.setStyleSheet(u"border:2px;\n"
"color:white;\n"
"")
        self.why_important_password = QLabel(self.menu2)
        self.why_important_password.setObjectName(u"why_important_password")
        self.why_important_password.setGeometry(QRect(400, 10, 391, 21))
        self.why_important_password.setFont(font3)
        self.why_important_password.setStyleSheet(u"color:white;")
        self.why_stable_password_kind_1 = QTextBrowser(self.menu2)
        self.why_stable_password_kind_1.setObjectName(u"why_stable_password_kind_1")
        self.why_stable_password_kind_1.setGeometry(QRect(400, 40, 201, 151))
        self.why_stable_password_kind_1.setFont(font3)
        self.why_stable_password_kind_1.setStyleSheet(u"border:2px;\n"
"color:white;\n"
"")
        self.why_stable_password_kind_2 = QTextBrowser(self.menu2)
        self.why_stable_password_kind_2.setObjectName(u"why_stable_password_kind_2")
        self.why_stable_password_kind_2.setGeometry(QRect(610, 40, 241, 151))
        self.why_stable_password_kind_2.setFont(font3)
        self.why_stable_password_kind_2.setStyleSheet(u"border:2px;\n"
"color:white;\n"
"")
        self.why_stable_password_kind_3 = QTextBrowser(self.menu2)
        self.why_stable_password_kind_3.setObjectName(u"why_stable_password_kind_3")
        self.why_stable_password_kind_3.setGeometry(QRect(400, 200, 451, 71))
        self.why_stable_password_kind_3.setFont(font3)
        self.why_stable_password_kind_3.setStyleSheet(u"border:2px;\n"
"color:white;\n"
"")
        self.how_hack_accounts = QLabel(self.menu2)
        self.how_hack_accounts.setObjectName(u"how_hack_accounts")
        self.how_hack_accounts.setGeometry(QRect(490, 280, 451, 21))
        self.how_hack_accounts.setFont(font3)
        self.how_hack_accounts.setStyleSheet(u"color:white;")
        self.password_hack_kind_1 = QTextBrowser(self.menu2)
        self.password_hack_kind_1.setObjectName(u"password_hack_kind_1")
        self.password_hack_kind_1.setGeometry(QRect(400, 310, 211, 131))
        self.password_hack_kind_1.setFont(font3)
        self.password_hack_kind_1.setStyleSheet(u"border:2px;\n"
"color:white;\n"
"")
        self.password_hack_kind_2 = QTextBrowser(self.menu2)
        self.password_hack_kind_2.setObjectName(u"password_hack_kind_2")
        self.password_hack_kind_2.setGeometry(QRect(620, 310, 231, 131))
        self.password_hack_kind_2.setFont(font3)
        self.password_hack_kind_2.setStyleSheet(u"border:2px;\n"
"color:white;\n"
"")
        self.password_hack_kind_3 = QTextBrowser(self.menu2)
        self.password_hack_kind_3.setObjectName(u"password_hack_kind_3")
        self.password_hack_kind_3.setGeometry(QRect(400, 450, 211, 131))
        self.password_hack_kind_3.setFont(font3)
        self.password_hack_kind_3.setStyleSheet(u"border:2px;\n"
"color:white;\n"
"")
        self.password_hack_kind_4 = QTextBrowser(self.menu2)
        self.password_hack_kind_4.setObjectName(u"password_hack_kind_4")
        self.password_hack_kind_4.setGeometry(QRect(620, 450, 231, 131))
        self.password_hack_kind_4.setFont(font3)
        self.password_hack_kind_4.setStyleSheet(u"border:2px;\n"
"color:white;\n"
"")
        self.cipher_title = QLabel(self.menu2)
        self.cipher_title.setObjectName(u"cipher_title")
        self.cipher_title.setGeometry(QRect(80, 10, 241, 21))
        self.cipher_title.setFont(font3)
        self.cipher_title.setStyleSheet(u"color:white;")
        self.second_advice_frame_2 = QFrame(self.menu2)
        self.second_advice_frame_2.setObjectName(u"second_advice_frame_2")
        self.second_advice_frame_2.setGeometry(QRect(10, 40, 381, 161))
        self.second_advice_frame_2.setStyleSheet(u"background-color:rgba(255,255,255,30);\n"
"border-radius:10px;")
        self.second_advice_frame_2.setFrameShape(QFrame.StyledPanel)
        self.second_advice_frame_2.setFrameShadow(QFrame.Raised)
        self.second_advice_frame_3 = QFrame(self.menu2)
        self.second_advice_frame_3.setObjectName(u"second_advice_frame_3")
        self.second_advice_frame_3.setGeometry(QRect(400, 40, 451, 231))
        self.second_advice_frame_3.setStyleSheet(u"background-color:rgba(255,255,255,30);\n"
"border-radius:10px;")
        self.second_advice_frame_3.setFrameShape(QFrame.StyledPanel)
        self.second_advice_frame_3.setFrameShadow(QFrame.Raised)
        self.second_advice_frame_4 = QFrame(self.menu2)
        self.second_advice_frame_4.setObjectName(u"second_advice_frame_4")
        self.second_advice_frame_4.setGeometry(QRect(10, 240, 381, 161))
        self.second_advice_frame_4.setStyleSheet(u"background-color:rgba(255,255,255,30);\n"
"border-radius:10px;")
        self.second_advice_frame_4.setFrameShape(QFrame.StyledPanel)
        self.second_advice_frame_4.setFrameShadow(QFrame.Raised)
        self.second_advice_frame_5 = QFrame(self.menu2)
        self.second_advice_frame_5.setObjectName(u"second_advice_frame_5")
        self.second_advice_frame_5.setGeometry(QRect(10, 420, 381, 111))
        self.second_advice_frame_5.setStyleSheet(u"background-color:rgba(255,255,255,30);\n"
"border-radius:10px;")
        self.second_advice_frame_5.setFrameShape(QFrame.StyledPanel)
        self.second_advice_frame_5.setFrameShadow(QFrame.Raised)
        self.second_advice_frame_6 = QFrame(self.menu2)
        self.second_advice_frame_6.setObjectName(u"second_advice_frame_6")
        self.second_advice_frame_6.setGeometry(QRect(400, 310, 451, 121))
        self.second_advice_frame_6.setStyleSheet(u"background-color:rgba(255,255,255,30);\n"
"border-radius:10px;")
        self.second_advice_frame_6.setFrameShape(QFrame.StyledPanel)
        self.second_advice_frame_6.setFrameShadow(QFrame.Raised)
        self.second_advice_frame_7 = QFrame(self.menu2)
        self.second_advice_frame_7.setObjectName(u"second_advice_frame_7")
        self.second_advice_frame_7.setGeometry(QRect(400, 440, 451, 141))
        self.second_advice_frame_7.setStyleSheet(u"background-color:rgba(255,255,255,30);\n"
"border-radius:10px;")
        self.second_advice_frame_7.setFrameShape(QFrame.StyledPanel)
        self.second_advice_frame_7.setFrameShadow(QFrame.Raised)
        self.menu3 = QWidget(self.centralwidget)
        self.menu3.setObjectName(u"menu3")
        self.menu3.setEnabled(True)
        self.menu3.setGeometry(QRect(49, -1, 871, 601))
        self.menu3.setStyleSheet(u"background:rgb(238, 238, 238)")
        self.cipher = QWidget(self.menu3)
        self.cipher.setObjectName(u"cipher")
        self.cipher.setEnabled(True)
        self.cipher.setGeometry(QRect(0, 0, 881, 601))
        self.cipher.setStyleSheet(u"background-color:#0a2d4d")
        self.cipher_button = QPushButton(self.cipher)
        self.cipher_button.setObjectName(u"cipher_button")
        self.cipher_button.setGeometry(QRect(270, 340, 271, 31))
        font4 = QFont()
        font4.setFamilies([u"Courier New"])
        font4.setBold(False)
        font4.setUnderline(False)
        self.cipher_button.setFont(font4)
        self.cipher_button.setStyleSheet(u"QPushButton {\n"
"        background-color: #0572ec;\n"
"        font-size: 20px;\n"
"        color: rgb(255, 255, 255);\n"
"        letter-spacing: 1px;\n"
"        border-radius: 10px;\n"
"    }\n"
"\n"
"    QPushButton:hover {\n"
"        background-color: #065fc7; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: #034ea6;\n"
"    }")
        self.comboBox = QComboBox(self.cipher)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(160, 340, 71, 29))
        font5 = QFont()
        font5.setFamilies([u"Courier New"])
        font5.setPointSize(9)
        self.comboBox.setFont(font5)
        self.comboBox.setStyleSheet(u"QComboBox::drop-down {\n"
"    image: none;\n"
"	width:0px;\n"
"}\n"
"QComboBox{\n"
"	letter-spacing: 1px;\n"
"	background-color:rgba(255, 255, 255, 0);\n"
"	border: 2px solid rgb(135, 135, 135);  \n"
"	border-radius:10px;\n"
"	color:white;\n"
"}\n"
"QComboBox:hover, QComboBox:pressed {\n"
"        border-color: rgb(120, 120, 120); \n"
"    }\n"
"\n"
"QComboBox::item {\n"
"        background-color: rgba(255,255,255,255); \n"
"        color: white; \n"
"    }")
        self.input = QTextEdit(self.cipher)
        self.input.setObjectName(u"input")
        self.input.setGeometry(QRect(130, 180, 571, 151))
        self.input.setFont(font1)
        self.input.setStyleSheet(u"background-color:rgb(203, 203, 203);\n"
"border-radius:10px;")
        self.PW_button = QPushButton(self.cipher)
        self.PW_button.setObjectName(u"PW_button")
        self.PW_button.setGeometry(QRect(560, 340, 111, 31))
        self.PW_button.setFont(font1)
        self.PW_button.setStyleSheet(u"QPushButton {\n"
"        background-color: rgba(255, 255, 255, 0);\n"
"        color: white;\n"
"        border-radius: 10px;\n"
"        border: 2px solid rgb(135, 135, 135);  \n"
"        padding: 5px 10px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"        border-color: rgb(120, 120, 120); \n"
"    }")
        self.output = QTextBrowser(self.cipher)
        self.output.setObjectName(u"output")
        self.output.setGeometry(QRect(240, 410, 331, 101))
        self.output.setFont(font3)
        self.output.setStyleSheet(u"QTextBrowser {\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    color: white;\n"
"    border-radius: 10px; \n"
"    border: 2px solid rgb(135, 135, 135);\n"
"    padding: 5px;\n"
"}")
        self.PW = QWidget(self.menu3)
        self.PW.setObjectName(u"PW")
        self.PW.setEnabled(True)
        self.PW.setGeometry(QRect(-1, -1, 871, 601))
        self.PW.setStyleSheet(u"background-color:#0a2d4d")
        self.Button_Cipher_change = QPushButton(self.PW)
        self.Button_Cipher_change.setObjectName(u"Button_Cipher_change")
        self.Button_Cipher_change.setEnabled(True)
        self.Button_Cipher_change.setGeometry(QRect(572, 340, 111, 31))
        self.Button_Cipher_change.setFont(font1)
        self.Button_Cipher_change.setStyleSheet(u"QPushButton {\n"
"        background-color: rgba(255, 255, 255, 0);\n"
"        color: white;\n"
"        border-radius: 10px;\n"
"        border: 2px solid rgb(135, 135, 135);  \n"
"        padding: 5px 10px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"        border-color: rgb(120, 120, 120); \n"
"    }")
        self.pw_button = QPushButton(self.PW)
        self.pw_button.setObjectName(u"pw_button")
        self.pw_button.setGeometry(QRect(382, 340, 51, 31))
        font6 = QFont()
        font6.setFamilies([u"Arial"])
        font6.setPointSize(15)
        font6.setBold(False)
        font6.setUnderline(False)
        self.pw_button.setFont(font6)
        self.pw_button.setStyleSheet(u"QPushButton {\n"
"        background-color: rgba(255, 255, 255, 0);\n"
"        color: white;\n"
"        border-radius: 10px;\n"
"        border: 2px solid rgb(135, 135, 135);  \n"
"        padding: 5px 10px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"        border-color: rgb(120, 120, 120);  \n"
"    }")
        self.password_length_slider = QSlider(self.PW)
        self.password_length_slider.setObjectName(u"password_length_slider")
        self.password_length_slider.setGeometry(QRect(202, 350, 141, 22))
        self.password_length_slider.setStyleSheet(u"background-color:rgba(255, 255, 255,0);")
        self.password_length_slider.setOrientation(Qt.Horizontal)
        self.Copy_password = QPushButton(self.PW)
        self.Copy_password.setObjectName(u"Copy_password")
        self.Copy_password.setGeometry(QRect(462, 340, 81, 31))
        self.Copy_password.setFont(font3)
        self.Copy_password.setStyleSheet(u"QPushButton {\n"
"        background-color: #0572ec;\n"
"        font-size: 20px;\n"
"        color: rgb(255, 255, 255);\n"
"        letter-spacing: 1px;\n"
"        border-radius: 10px;\n"
"    }\n"
"\n"
"    QPushButton:hover {\n"
"        background-color: #065fc7; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: #034ea6;\n"
"    }")
        self.Lendth = QLabel(self.PW)
        self.Lendth.setObjectName(u"Lendth")
        self.Lendth.setGeometry(QRect(130, 350, 61, 20))
        self.Lendth.setFont(font1)
        self.Lendth.setStyleSheet(u"color: white;\n"
"background-color:rgba(255, 255, 255,0);")
        self.password_lendth_label = QLabel(self.PW)
        self.password_lendth_label.setObjectName(u"password_lendth_label")
        self.password_lendth_label.setGeometry(QRect(352, 346, 27, 31))
        self.password_lendth_label.setFont(font1)
        self.password_lendth_label.setStyleSheet(u"background-color:rgba(255, 255, 255, 0);\n"
"color: white;")
        self.lower_case = QCheckBox(self.PW)
        self.lower_case.setObjectName(u"lower_case")
        self.lower_case.setGeometry(QRect(122, 390, 161, 20))
        font7 = QFont()
        font7.setFamilies([u"Courier New"])
        font7.setPointSize(12)
        self.lower_case.setFont(font7)
        self.lower_case.setStyleSheet(u"background-color:rgba(255, 255, 255,0);\n"
"color: white;\n"
"border-radius:10px;")
        self.numbers = QCheckBox(self.PW)
        self.numbers.setObjectName(u"numbers")
        self.numbers.setGeometry(QRect(312, 390, 76, 20))
        self.numbers.setFont(font7)
        self.numbers.setStyleSheet(u"background-color:rgba(255, 255, 255,0);\n"
"color: white;")
        self.symbols = QCheckBox(self.PW)
        self.symbols.setObjectName(u"symbols")
        self.symbols.setGeometry(QRect(432, 390, 111, 20))
        self.symbols.setFont(font7)
        self.symbols.setStyleSheet(u"color: white;\n"
"background-color:rgba(255, 255, 255,0);")
        self.upper_case = QCheckBox(self.PW)
        self.upper_case.setObjectName(u"upper_case")
        self.upper_case.setGeometry(QRect(552, 390, 181, 20))
        self.upper_case.setFont(font7)
        self.upper_case.setStyleSheet(u"background-color:rgba(255, 255, 255,0);\n"
"\n"
"color: white;")
        self.Password_labe = QTextBrowser(self.PW)
        self.Password_labe.setObjectName(u"Password_labe")
        self.Password_labe.setGeometry(QRect(142, 180, 531, 131))
        font8 = QFont()
        font8.setFamilies([u"Courier New"])
        font8.setPointSize(13)
        self.Password_labe.setFont(font8)
        self.Password_labe.setStyleSheet(u"background-color:rgb(203, 203, 203);\n"
"border-radius:10px;")
        self.PW.raise_()
        self.cipher.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.leftMenu.raise_()
        self.menu2.raise_()
        self.menu1.raise_()
        self.menu3.raise_()

        self.retranslateUi(MainWindow)
        self.password_length_slider.valueChanged.connect(self.password_lendth_label.setNum)

        self.comboBox.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.first.setText("")
        self.third.setText("")
        self.second.setText("")
        self.login_button.setText("")
        self.internet_security_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt;\">\u041e\u0441\u043d\u043e\u0432\u043d\u0430\u044f \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e \u0431\u0435\u0437\u043e\u043f\u0430\u0441\u043d\u043e\u0441\u0442\u0438 \u0432 \u0438\u043d\u0442\u0435\u0440\u043d\u0435\u0442\u0435</span></p></body></html>", None))
        self.internet_info_label.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Courier New'; font-size:15pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; -qt-user-state:65537;\"><span style=\" font-size:16pt;\">\u0412 \u043c\u0438\u0440\u0435, \u0433\u0434\u0435 \u0442\u0435\u0445\u043d\u043e\u043b\u043e\u0433\u0438\u0438 \u0438\u0433\u0440\u0430\u044e\u0442 \u043a\u043b\u044e\u0447\u0435\u0432\u0443\u044e \u0440\u043e\u043b\u044c \u0432 \u043d\u0430\u0448\u0435\u0439 \u043f\u043e\u0432\u0441\u0435\u0434\u043d\u0435\u0432\u043d\u043e\u0439 \u0436\u0438"
                        "\u0437\u043d\u0438, \u043e\u0431\u0435\u0441\u043f\u0435\u0447\u0435\u043d\u0438\u0435 \u0431\u0435\u0437\u043e\u043f\u0430\u0441\u043d\u043e\u0441\u0442\u0438 \u0432 \u0438\u043d\u0442\u0435\u0440\u043d\u0435\u0442\u0435 \u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u0441\u044f \u0432\u0441\u0435 \u0431\u043e\u043b\u0435\u0435 \u0432\u0430\u0436\u043d\u044b\u043c. \u0418\u043d\u0442\u0435\u0440\u043d\u0435\u0442 \u043f\u0440\u0435\u0434\u043e\u0441\u0442\u0430\u0432\u043b\u044f\u0435\u0442 \u043d\u0430\u043c \u043e\u0433\u0440\u043e\u043c\u043d\u044b\u0435 \u0432\u043e\u0437\u043c\u043e\u0436\u043d\u043e\u0441\u0442\u0438, \u043d\u043e \u043f\u0440\u0438 \u044d\u0442\u043e\u043c \u0441\u043e\u043f\u0440\u044f\u0436\u0435\u043d \u0441 \u0440\u0430\u0437\u043b\u0438\u0447\u043d\u044b\u043c\u0438 \u0443\u0433\u0440\u043e\u0437\u0430\u043c\u0438 \u0434\u043b\u044f \u043d\u0430\u0448\u0435\u0439 \u043b\u0438\u0447\u043d\u043e\u0439 \u0431\u0435\u0437\u043e\u043f\u0430\u0441\u043d\u043e\u0441\u0442\u0438 \u0438 "
                        "\u043a\u043e\u043d\u0444\u0438\u0434\u0435\u043d\u0446\u0438\u0430\u043b\u044c\u043d\u043e\u0441\u0442\u0438.</span></p></body></html>", None))
        self.cybersec_image_label.setText("")
        self.advice_cybersec.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">\u0421\u043e\u0432\u0435\u0442\u044b \u043f\u043e \u043e\u0431\u0435\u0441\u043f\u0435\u0447\u0435\u043d\u0438\u044e \u0431\u0435\u0437\u043e\u043f\u0430\u0441\u043d\u043e\u0441\u0442\u0438 \u0432 \u0438\u043d\u0442\u0435\u0440\u043d\u0435\u0442\u0435:</span></p></body></html>", None))
        self.first_advice.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Courier New'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:700;\">\u0421\u043b\u043e\u0436\u043d\u044b\u0435 \u043f\u0430\u0440\u043e\u043b\u0438</span><span style=\" font-size:10pt;\">: \u0418\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u0439\u0442\u0435 \u0434\u043b\u0438\u043d\u043d\u044b\u0435 \u0438 \u0441\u043b\u043e\u0436\u043d\u044b\u0435 \u043f\u0430\u0440\u043e\u043b\u0438, \u0441\u043e\u0441\u0442\u043e\u044f"
                        "\u0449\u0438\u0435 \u0438\u0437 \u0431\u0443\u043a\u0432, \u0446\u0438\u0444\u0440 \u0438 \u0441\u043f\u0435\u0446\u0438\u0430\u043b\u044c\u043d\u044b\u0445 \u0441\u0438\u043c\u0432\u043e\u043b\u043e\u0432. \u041d\u0438\u043a\u043e\u0433\u0434\u0430 \u043d\u0435 \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u0439\u0442\u0435 \u043e\u0434\u0438\u043d \u0438 \u0442\u043e\u0442 \u0436\u0435 \u043f\u0430\u0440\u043e\u043b\u044c \u0434\u043b\u044f \u043d\u0435\u0441\u043a\u043e\u043b\u044c\u043a\u0438\u0445 \u0430\u043a\u043a\u0430\u0443\u043d\u0442\u043e\u0432.</span></p></body></html>", None))
        self.second_advice.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Courier New'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:700;\">\u041e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u0435 \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u043d\u043e\u0433\u043e \u043e\u0431\u0435\u0441\u043f\u0435\u0447\u0435\u043d\u0438\u044f</span><span style=\" font-size:10pt;\">: \u0420\u0435\u0433\u0443\u043b\u044f\u0440\u043d\u043e \u043e\u0431\u043d\u043e\u0432\u043b\u044f\u0439\u0442"
                        "\u0435 \u0432\u0441\u0435 \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u044b \u0438 \u043e\u043f\u0435\u0440\u0430\u0446\u0438\u043e\u043d\u043d\u044b\u0435 \u0441\u0438\u0441\u0442\u0435\u043c\u044b \u043d\u0430 \u0432\u0430\u0448\u0438\u0445 \u0443\u0441\u0442\u0440\u043e\u0439\u0441\u0442\u0432\u0430\u0445. \u041e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u044f \u0447\u0430\u0441\u0442\u043e \u0441\u043e\u0434\u0435\u0440\u0436\u0430\u0442 \u0438\u0441\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u044f \u0443\u044f\u0437\u0432\u0438\u043c\u043e\u0441\u0442\u0435\u0439 \u0431\u0435\u0437\u043e\u043f\u0430\u0441\u043d\u043e\u0441\u0442\u0438.</span></p></body></html>", None))
        self.third_advice.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Courier New'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:700;\">\u0418\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u0439\u0442\u0435 \u0434\u0432\u0443\u0445\u0444\u0430\u043a\u0442\u043e\u0440\u043d\u0443\u044e \u0430\u0443\u0442\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0446\u0438\u044e</span><span style=\" font-size:10pt;\">: \u0412\u043a\u043b\u044e\u0447\u0438\u0442\u0435 \u043d\u0430\u0441\u0442\u0440"
                        "\u043e\u0439\u043a\u0438 \u0434\u0432\u0443\u0445\u0444\u0430\u043a\u0442\u043e\u0440\u043d\u043e\u0439 \u0430\u0443\u0442\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0446\u0438\u0438 \u0434\u043b\u044f \u0434\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0433\u043e \u0443\u0440\u043e\u0432\u043d\u044f \u0431\u0435\u0437\u043e\u043f\u0430\u0441\u043d\u043e\u0441\u0442\u0438 \u0432\u0430\u0448\u0435\u0433\u043e \u0430\u043a\u043a\u0430\u0443\u043d\u0442\u0430.</span></p></body></html>", None))
        self.fourth_advice.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Courier New'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:700;\">\u0418\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u0439\u0442\u0435 \u0437\u0430\u0449\u0438\u0449\u0435\u043d\u043d\u044b\u0435 \u0441\u043e\u0435\u0434\u0438\u043d\u0435\u043d\u0438\u044f</span><span style=\" font-size:10pt;\">: \u041f\u0440\u0438 \u0434\u043e\u0441\u0442\u0443\u043f\u0435 \u043a \u0441\u0430\u0439\u0442\u0430\u043c, \u043e\u0441\u043e"
                        "\u0431\u0435\u043d\u043d\u043e \u043f\u0440\u0438 \u0432\u0432\u043e\u0434\u0435 \u043b\u0438\u0447\u043d\u043e\u0439 \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u0438 \u0438\u043b\u0438 \u043f\u0430\u0440\u043e\u043b\u0435\u0439, \u0443\u0431\u0435\u0434\u0438\u0442\u0435\u0441\u044c, \u0447\u0442\u043e \u0441\u043e\u0435\u0434\u0438\u043d\u0435\u043d\u0438\u0435 \u0437\u0430\u0448\u0438\u0444\u0440\u043e\u0432\u0430\u043d\u043e (\u043f\u0440\u043e\u0432\u0435\u0440\u044f\u0439\u0442\u0435 \u043d\u0430\u043b\u0438\u0447\u0438\u0435 \u0437\u0430\u043c\u043a\u0430 \u0432 \u0430\u0434\u0440\u0435\u0441\u043d\u043e\u0439 \u0441\u0442\u0440\u043e\u043a\u0435 \u0431\u0440\u0430\u0443\u0437\u0435\u0440\u0430).</span></p></body></html>", None))
        self.enum_1_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">1</span></p></body></html>", None))
        self.enum_2_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">2</span></p></body></html>", None))
        self.enum_3_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">3</span></p></body></html>", None))
        self.enum_4_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">4</span></p></body></html>", None))
        self.cipher_info_label.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Courier New'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">\u0428\u0438\u0444\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u044f\u0432\u043b\u044f\u0435\u0442\u0441\u044f \u043f\u0440\u043e\u0446\u0435\u0441\u0441\u043e\u043c \u043f\u0440\u0435\u043e\u0431\u0440\u0430\u0437\u043e\u0432\u0430\u043d\u0438\u044f \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u0438 \u0432 \u043d\u0435\u0447\u0438\u0442\u0430\u0435\u043c\u044b"
                        "\u0439 \u0432\u0438\u0434 \u0441 \u0446\u0435\u043b\u044c\u044e \u043e\u0431\u0435\u0441\u043f\u0435\u0447\u0435\u043d\u0438\u044f \u043a\u043e\u043d\u0444\u0438\u0434\u0435\u043d\u0446\u0438\u0430\u043b\u044c\u043d\u043e\u0441\u0442\u0438 \u0434\u0430\u043d\u043d\u044b\u0445. \u041e\u043d\u043e \u0448\u0438\u0440\u043e\u043a\u043e \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u0435\u0442\u0441\u044f \u0432 \u0440\u0430\u0437\u043b\u0438\u0447\u043d\u044b\u0445 \u043e\u0431\u043b\u0430\u0441\u0442\u044f\u0445, \u0432\u043a\u043b\u044e\u0447\u0430\u044f \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u043e\u043d\u043d\u0443\u044e \u0431\u0435\u0437\u043e\u043f\u0430\u0441\u043d\u043e\u0441\u0442\u044c, \u0437\u0430\u0449\u0438\u0442\u0443 \u043f\u0435\u0440\u0441\u043e\u043d\u0430\u043b\u044c\u043d\u044b\u0445 \u0434\u0430\u043d\u043d\u044b\u0445, \u043a\u043e\u043c\u043c\u0443\u043d\u0438\u043a\u0430\u0446\u0438\u0438 \u0438 \u0431\u0430\u043d\u043a\u043e\u0432\u0441\u043a\u0438\u0435 \u043e\u043f\u0435"
                        "\u0440\u0430\u0446\u0438\u0438.</span></p></body></html>", None))
        self.cipher_kinds_title_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">\u0412\u0438\u0434\u044b \u0428\u0438\u0444\u0440\u043e\u0432\u0430\u043d\u0438\u0439</span></p></body></html>", None))
        self.cipher_kind_1.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Courier New'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">\u0421\u0438\u043c\u043c\u0435\u0442\u0440\u0438\u0447\u043d\u043e\u0435 \u0448\u0438\u0444\u0440\u043e\u0432\u0430\u043d\u0438\u0435</span>: \u0412 \u044d\u0442\u043e\u043c \u0432\u0438\u0434\u0435 \u0448\u0438\u0444\u0440\u043e\u0432\u0430\u043d\u0438\u044f \u043e\u0434\u0438\u043d \u043a\u043b\u044e\u0447 \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u0435\u0442"
                        "\u0441\u044f \u043a\u0430\u043a \u0434\u043b\u044f \u0448\u0438\u0444\u0440\u043e\u0432\u0430\u043d\u0438\u044f, \u0442\u0430\u043a \u0438 \u0434\u043b\u044f \u0440\u0430\u0441\u0448\u0438\u0444\u0440\u043e\u0432\u043a\u0438 \u0434\u0430\u043d\u043d\u044b\u0445. </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u041f\u0440\u0438\u043c\u0435\u0440\u044b: AES, DES, 3DES.</p></body></html>", None))
        self.cipher_kind_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Courier New'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">\u0410\u0441\u0438\u043c\u043c\u0435\u0442\u0440\u0438\u0447\u043d\u043e\u0435 \u0448\u0438\u0444\u0440\u043e\u0432\u0430\u043d\u0438\u0435</span>: \u0412 \u0430\u0441\u0438\u043c\u043c\u0435\u0442\u0440\u0438\u0447\u043d\u043e\u043c \u0448\u0438\u0444\u0440\u043e\u0432\u0430\u043d\u0438\u0438 \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u044e\u0442\u0441\u044f"
                        " \u0434\u0432\u0430 \u043a\u043b\u044e\u0447\u0430: \u043f\u0443\u0431\u043b\u0438\u0447\u043d\u044b\u0439 \u0438 \u043f\u0440\u0438\u0432\u0430\u0442\u043d\u044b\u0439. \u041f\u0443\u0431\u043b\u0438\u0447\u043d\u044b\u0439 \u043a\u043b\u044e\u0447 \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u0435\u0442\u0441\u044f \u0434\u043b\u044f \u0448\u0438\u0444\u0440\u043e\u0432\u0430\u043d\u0438\u044f, \u0430 \u043f\u0440\u0438\u0432\u0430\u0442\u043d\u044b\u0439 - \u0434\u043b\u044f \u0440\u0430\u0441\u0448\u0438\u0444\u0440\u043e\u0432\u043a\u0438. </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u041f\u0440\u0438\u043c\u0435\u0440\u044b: RSA, ECC.</p></body></html>", None))
        self.cipher_kind_3.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Courier New'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">\u0425\u044d\u0448\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435</span>: \u042d\u0442\u043e\u0442 \u043c\u0435\u0442\u043e\u0434 \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u0435\u0442\u0441\u044f \u0434\u043b\u044f \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f \u0443\u043d\u0438\u043a\u0430\u043b\u044c\u043d\u043e\u0433\u043e \u0444\u0438\u043a\u0441\u0438"
                        "\u0440\u043e\u0432\u0430\u043d\u043d\u043e\u0433\u043e \u0440\u0430\u0437\u043c\u0435\u0440\u0430 \u0434\u043b\u044f \u043b\u044e\u0431\u043e\u0433\u043e \u0432\u0445\u043e\u0434\u043d\u043e\u0433\u043e \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u044f. \u041e\u043d \u043d\u0435 \u043e\u0431\u0440\u0430\u0442\u0438\u043c \u0438 \u043d\u0435 \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u0435\u0442 \u043a\u043b\u044e\u0447. </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u041f\u0440\u0438\u043c\u0435\u0440\u044b: MD5, SHA-256, SHA-1, SHA-512, SHA-384.</p></body></html>", None))
        self.why_important_password.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">\u041f\u043e\u0447\u0435\u043c\u0443 \u0432\u0430\u0436\u043d\u043e \u0438\u043c\u0435\u0442\u044c \u043d\u0430\u0434\u0435\u0436\u043d\u044b\u0439 \u043f\u0430\u0440\u043e\u043b\u044c?</span></p></body></html>", None))
        self.why_stable_password_kind_1.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Courier New'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">\u0417\u0430\u0449\u0438\u0442\u0430 \u043b\u0438\u0447\u043d\u043e\u0439 \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u0438:</span> \u041d\u0430\u0434\u0435\u0436\u043d\u044b\u0435 \u043f\u0430\u0440\u043e\u043b\u0438 \u043f\u043e\u043c\u043e\u0433\u0430\u044e\u0442 \u043f\u0440\u0435\u0434\u043e\u0442\u0432\u0440\u0430\u0442\u0438\u0442\u044c \u043d\u0435"
                        "\u0441\u0430\u043d\u043a\u0446\u0438\u043e\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0439 \u0434\u043e\u0441\u0442\u0443\u043f \u043a \u0432\u0430\u0448\u0438\u043c \u043b\u0438\u0447\u043d\u044b\u043c \u0434\u0430\u043d\u043d\u044b\u043c, \u0432\u043a\u043b\u044e\u0447\u0430\u044f \u0444\u0438\u043d\u0430\u043d\u0441\u043e\u0432\u044b\u0435 \u0441\u0432\u0435\u0434\u0435\u043d\u0438\u044f, \u043b\u0438\u0447\u043d\u0443\u044e \u043f\u0435\u0440\u0435\u043f\u0438\u0441\u043a\u0443, \u0444\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u0438 \u0438 \u0434\u0440\u0443\u0433\u0438\u0435 \u043a\u043e\u043d\u0444\u0438\u0434\u0435\u043d\u0446\u0438\u0430\u043b\u044c\u043d\u044b\u0435 \u0441\u0432\u0435\u0434\u0435\u043d\u0438\u044f.</p></body></html>", None))
        self.why_stable_password_kind_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Courier New'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">\u0411\u0435\u0437\u043e\u043f\u0430\u0441\u043d\u043e\u0441\u0442\u044c \u043e\u043d\u043b\u0430\u0439\u043d-\u0430\u043a\u043a\u0430\u0443\u043d\u0442\u043e\u0432:</span> \u041d\u0430\u0434\u0435\u0436\u043d\u044b\u0435 \u043f\u0430\u0440\u043e\u043b\u0438 \u043e\u0431\u0435\u0441\u043f\u0435\u0447\u0438\u0432\u0430\u044e\u0442 \u0431\u0435\u0437\u043e\u043f\u0430"
                        "\u0441\u043d\u043e\u0441\u0442\u044c \u0432\u0430\u0448\u0438\u0445 \u043e\u043d\u043b\u0430\u0439\u043d-\u0430\u043a\u043a\u0430\u0443\u043d\u0442\u043e\u0432, \u0442\u0430\u043a\u0438\u0445 \u043a\u0430\u043a \u044d\u043b\u0435\u043a\u0442\u0440\u043e\u043d\u043d\u0430\u044f \u043f\u043e\u0447\u0442\u0430, \u0441\u043e\u0446\u0438\u0430\u043b\u044c\u043d\u044b\u0435 \u0441\u0435\u0442\u0438, \u0438\u043d\u0442\u0435\u0440\u043d\u0435\u0442-\u0431\u0430\u043d\u043a\u0438\u043d\u0433 \u0438 \u0434\u0440\u0443\u0433\u0438\u0435 \u0441\u0435\u0440\u0432\u0438\u0441\u044b, \u043f\u0440\u0435\u0434\u043e\u0442\u0432\u0440\u0430\u0449\u0430\u044f \u043d\u0435\u0441\u0430\u043d\u043a\u0446\u0438\u043e\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0439 \u0434\u043e\u0441\u0442\u0443\u043f \u0438 \u043f\u043e\u0442\u0435\u043d\u0446\u0438\u0430\u043b\u044c\u043d\u044b\u0435 \u043a\u0438\u0431\u0435\u0440\u0430\u0442\u0430\u043a\u0438.</p></body></html>", None))
        self.why_stable_password_kind_3.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Courier New'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">\u041f\u0440\u0435\u0434\u043e\u0442\u0432\u0440\u0430\u0449\u0435\u043d\u0438\u0435 \u043a\u0440\u0430\u0436\u0438 \u043b\u0438\u0447\u043d\u043e\u0441\u0442\u0438:</span> \u0421\u0438\u043b\u044c\u043d\u044b\u0435 \u043f\u0430\u0440\u043e\u043b\u0438 \u043f\u043e\u043c\u043e\u0433\u0430\u044e\u0442 \u043f\u0440\u0435\u0434\u043e\u0442\u0432\u0440\u0430\u0442\u0438"
                        "\u0442\u044c \u043a\u0440\u0430\u0436\u0443 \u043b\u0438\u0447\u043d\u043e\u0441\u0442\u0438, \u043a\u043e\u0442\u043e\u0440\u0430\u044f \u043c\u043e\u0436\u0435\u0442 \u043f\u0440\u0438\u0432\u0435\u0441\u0442\u0438 \u043a \u0444\u0438\u043d\u0430\u043d\u0441\u043e\u0432\u044b\u043c \u043f\u043e\u0442\u0435\u0440\u044f\u043c, \u0443\u0433\u0440\u043e\u0437\u0430\u043c \u0431\u0435\u0437\u043e\u043f\u0430\u0441\u043d\u043e\u0441\u0442\u0438 \u0438 \u0434\u0440\u0443\u0433\u0438\u043c \u043d\u0435\u0433\u0430\u0442\u0438\u0432\u043d\u044b\u043c \u043f\u043e\u0441\u043b\u0435\u0434\u0441\u0442\u0432\u0438\u044f\u043c.</p></body></html>", None))
        self.how_hack_accounts.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">\u041a\u0430\u043a \u0432\u0437\u043b\u0430\u043c\u044b\u0432\u0430\u044e\u0442 \u0430\u043a\u043a\u0430\u0443\u043d\u0442\u044b</span></p></body></html>", None))
        self.password_hack_kind_1.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Courier New'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">\u0421\u043b\u043e\u0432\u0430\u0440\u043d\u044b\u0435 \u0430\u0442\u0430\u043a\u0438:</span> \u0410\u0442\u0430\u043a\u0443\u044e\u0449\u0438\u0435 \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u044e\u0442 \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u043d\u043e\u0435 \u043e\u0431\u0435\u0441\u043f\u0435\u0447\u0435\u043d\u0438\u0435, \u043a\u043e\u0442\u043e"
                        "\u0440\u043e\u0435 \u043f\u0435\u0440\u0435\u0431\u0438\u0440\u0430\u0435\u0442 \u043c\u0438\u043b\u043b\u0438\u043e\u043d\u044b \u043a\u043e\u043c\u0431\u0438\u043d\u0430\u0446\u0438\u0439 \u0441\u043b\u043e\u0432 \u0438 \u0444\u0440\u0430\u0437 \u0438\u0437 \u0441\u043b\u043e\u0432\u0430\u0440\u044f \u0432 \u043f\u043e\u043f\u044b\u0442\u043a\u0435 \u0443\u0433\u0430\u0434\u0430\u0442\u044c \u0432\u0430\u0448 \u043f\u0430\u0440\u043e\u043b\u044c.</p></body></html>", None))
        self.password_hack_kind_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Courier New'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">\u0411\u0440\u0443\u0442\u0444\u043e\u0440\u0441 \u0430\u0442\u0430\u043a\u0438:</span> \u0410\u0442\u0430\u043a\u0443\u044e\u0449\u0438\u0435 \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u044e\u0442 \u0441\u043f\u0435\u0446\u0438\u0430\u043b\u044c\u043d\u043e\u0435 \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u043d\u043e\u0435 \u043e\u0431\u0435\u0441\u043f"
                        "\u0435\u0447\u0435\u043d\u0438\u0435 \u0434\u043b\u044f \u0430\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u043e\u0433\u043e \u043f\u0435\u0440\u0435\u0431\u043e\u0440\u0430 \u0432\u0441\u0435\u0445 \u0432\u043e\u0437\u043c\u043e\u0436\u043d\u044b\u0445 \u043a\u043e\u043c\u0431\u0438\u043d\u0430\u0446\u0438\u0439 \u0441\u0438\u043c\u0432\u043e\u043b\u043e\u0432, \u0447\u0442\u043e\u0431\u044b \u043d\u0430\u0439\u0442\u0438 \u0432\u0435\u0440\u043d\u044b\u0439 \u043f\u0430\u0440\u043e\u043b\u044c.</p></body></html>", None))
        self.password_hack_kind_3.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Courier New'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">\u0424\u0438\u0448\u0438\u043d\u0433:</span> \u0410\u0442\u0430\u043a\u0443\u044e\u0449\u0438\u0435 \u043c\u043e\u0433\u0443\u0442 \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u044c \u0444\u0438\u0448\u0438\u043d\u0433\u043e\u0432\u044b\u0435 \u043c\u0435\u0442\u043e\u0434\u044b, \u043e\u0442\u043f\u0440\u0430\u0432\u043b\u044f\u044f \u0432\u0430"
                        "\u043c \u043f\u043e\u0434\u0434\u0435\u043b\u044c\u043d\u044b\u0435 \u044d\u043b\u0435\u043a\u0442\u0440\u043e\u043d\u043d\u044b\u0435 \u043f\u0438\u0441\u044c\u043c\u0430 \u0438\u043b\u0438 \u0441\u043e\u0437\u0434\u0430\u0432\u0430\u044f \u043f\u043e\u0434\u0434\u0435\u043b\u044c\u043d\u044b\u0435 \u0432\u0435\u0431-\u0441\u0442\u0440\u0430\u043d\u0438\u0446\u044b, \u0447\u0442\u043e\u0431\u044b \u0437\u0430\u0441\u0442\u0430\u0432\u0438\u0442\u044c \u0432\u0430\u0441 \u0440\u0430\u0441\u043a\u0440\u044b\u0442\u044c \u0441\u0432\u043e\u0439 \u043f\u0430\u0440\u043e\u043b\u044c.</p></body></html>", None))
        self.password_hack_kind_4.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Courier New'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">\u041f\u043e\u0434\u0431\u043e\u0440 \u043f\u043e \u0443\u0442\u0435\u0447\u043a\u0435 \u0434\u0430\u043d\u043d\u044b\u0445:</span> \u0410\u0442\u0430\u043a\u0443\u044e\u0449\u0438\u0435 \u043c\u043e\u0433\u0443\u0442 \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u044c \u0431\u0430\u0437\u044b \u0434\u0430\u043d\u043d\u044b\u0445 \u0443\u043a\u0440"
                        "\u0430\u0434\u0435\u043d\u043d\u044b\u0445 \u043f\u0430\u0440\u043e\u043b\u0435\u0439, \u043a\u043e\u0442\u043e\u0440\u044b\u0435 \u0431\u044b\u043b\u0438 \u0441\u043a\u043e\u043c\u043f\u0440\u043e\u043c\u0435\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u044b \u0432 \u043f\u0440\u0435\u0434\u044b\u0434\u0443\u0449\u0438\u0445 \u043a\u0438\u0431\u0435\u0440\u0430\u0442\u0430\u043a\u0430\u0445, \u0447\u0442\u043e\u0431\u044b \u043f\u043e\u043f\u0440\u043e\u0431\u043e\u0432\u0430\u0442\u044c \u0432\u043e\u0439\u0442\u0438 \u0432 \u0432\u0430\u0448\u0438 \u0430\u043a\u043a\u0430\u0443\u043d\u0442\u044b \u0441 \u043f\u043e\u043c\u043e\u0449\u044c\u044e \u0442\u0435\u0445 \u0436\u0435 \u0443\u0447\u0435\u0442\u043d\u044b\u0445 \u0434\u0430\u043d\u043d\u044b\u0445.</p></body></html>", None))
        self.cipher_title.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">\u0427\u0442\u043e \u0442\u0430\u043a\u043e\u0435 \u0428\u0438\u0444\u0440\u043e\u0432\u0430\u043d\u0438\u0435?</span></p></body></html>", None))
        self.cipher_button.setText(QCoreApplication.translate("MainWindow", u"\u0428\u0438\u0444\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"sha256", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"sha512", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"sha1", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"sha384", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"BumBar", None))

        self.comboBox.setPlaceholderText("")
        self.PW_button.setText(QCoreApplication.translate("MainWindow", u"PW", None))
        self.output.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Courier New'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0428\u0438\u0444\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0439 \u0442\u0435\u043a\u0441\u0442</p></body></html>", None))
        self.Button_Cipher_change.setText(QCoreApplication.translate("MainWindow", u"Cipher", None))
        self.pw_button.setText(QCoreApplication.translate("MainWindow", u"\u21ba", None))
        self.Copy_password.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
        self.Lendth.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043b\u0438\u043d\u0430", None))
        self.password_lendth_label.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lower_case.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0438\u0436\u043d\u0438\u0439 \u0440\u0435\u0433\u0438\u0441\u0442\u0440", None))
        self.numbers.setText(QCoreApplication.translate("MainWindow", u"\u0426\u0438\u0444\u0440\u044b", None))
        self.symbols.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0438\u043c\u0432\u043e\u043b\u044b", None))
        self.upper_case.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0435\u0440\u0445\u043d\u0438\u0439 \u0440\u0435\u0433\u0438\u0441\u0442\u0440", None))
        self.Password_labe.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Courier New'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
    # retranslateUi


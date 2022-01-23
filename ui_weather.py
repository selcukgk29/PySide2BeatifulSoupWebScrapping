# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_weatherPEIfRg.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import subimages_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1147, 646)
        MainWindow.setLayoutDirection(Qt.LeftToRight)
        MainWindow.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setEnabled(True)
        self.frame.setGeometry(QRect(10, 10, 1131, 631))
        self.frame.setStyleSheet(u"QFrame{\n"
"background-color: rgb(38, 45, 53);\n"
"border-radius:25px;\n"
"\n"
"\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(680, 250, 110, 180))
        self.frame_3.setStyleSheet(u"QFrame{\n"
"background-color:rgb(30,40,56);\n"
"}\n"
"QFrame:hover{\n"
"\n"
"background-color:rgb(48,57,66);\n"
"\n"
"\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(130, 0, 110, 180))
        self.frame_4.setStyleSheet(u"QFrame{\n"
"background-color:rgb(30,40,56);\n"
"}\n"
"QFrame:hover{\n"
"\n"
"background-color:rgb(48,57,66);\n"
"\n"
"\n"
"}")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(300, 0, 110, 180))
        self.frame_5.setStyleSheet(u"QFrame{\n"
"background-color:rgb(30,40,56);\n"
"}\n"
"QFrame:hover{\n"
"\n"
"background-color:rgb(48,57,66);\n"
"\n"
"\n"
"}")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.frame_11 = QFrame(self.frame_3)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setGeometry(QRect(0, 0, 110, 180))
        self.frame_11.setStyleSheet(u"QFrame{\n"
"background-color:rgb(30,40,56);\n"
"}\n"
"QFrame:hover{\n"
"\n"
"background-color:rgb(48,57,66);\n"
"\n"
"\n"
"}")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.submenuicon1_2 = QLabel(self.frame_11)
        self.submenuicon1_2.setObjectName(u"submenuicon1_2")
        self.submenuicon1_2.setGeometry(QRect(20, 10, 61, 71))
        self.submenuicon1_2.setStyleSheet(u"background-color:none;")
        self.submenuicon1_2.setPixmap(QPixmap(u":/weather/picdir/weather/64x64/day/113.png"))
        self.submenuicon1_2.setScaledContents(True)
        self.submenuicon1_2.setAlignment(Qt.AlignCenter)
        self.submenu_day_2 = QLabel(self.frame_11)
        self.submenu_day_2.setObjectName(u"submenu_day_2")
        self.submenu_day_2.setGeometry(QRect(10, 60, 81, 71))
        font = QFont()
        font.setFamily(u"Montserrat")
        font.setBold(True)
        font.setWeight(87)
        self.submenu_day_2.setFont(font)
        self.submenu_day_2.setStyleSheet(u"background-color:none;\n"
"font-family: 'Montserrat', sans-serif;\n"
"font-weight:700;\n"
"font-size:20px;\n"
"color:#FFF")
        self.submenu_day_2.setAlignment(Qt.AlignCenter)
        self.submenu_temp_2 = QLabel(self.frame_11)
        self.submenu_temp_2.setObjectName(u"submenu_temp_2")
        self.submenu_temp_2.setGeometry(QRect(10, 100, 101, 81))
        self.submenu_temp_2.setFont(font)
        self.submenu_temp_2.setStyleSheet(u"background-color:none;\n"
"font-family: 'Montserrat', sans-serif;\n"
"font-weight:700;\n"
"font-size:20px;\n"
"color:#FFF")
        self.submenu_temp_2.setAlignment(Qt.AlignCenter)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(560, 70, 251, 51))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(75)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color:#FFF;\n"
"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 76), stop:1 rgba(255, 255, 255, 255));\n"
"background-color: qlineargradient(spread:pad, x1:0.895522, y1:0.432, x2:1, y2:0.426, stop:1 rgba(0, 0, 0, 94));")
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(560, 160, 251, 51))
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.895522, y1:0.432, x2:1, y2:0.426, stop:1 rgba(0, 0, 0, 94));\n"
"color:#FFF;")
        self.wind_label = QLabel(self.frame)
        self.wind_label.setObjectName(u"wind_label")
        self.wind_label.setGeometry(QRect(730, 160, 251, 51))
        self.wind_label.setFont(font1)
        self.wind_label.setStyleSheet(u"QFrame{\n"
"color:#FFF;\n"
"\n"
"}\n"
"QFrame:Hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:1 rgba(0, 0, 0, 84));\n"
"}")
        self.wind_label.setAlignment(Qt.AlignCenter)
        self.temp_label = QLabel(self.frame)
        self.temp_label.setObjectName(u"temp_label")
        self.temp_label.setGeometry(QRect(110, 330, 281, 121))
        self.temp_label.setFont(font)
        self.temp_label.setStyleSheet(u"background-color:none;\n"
"font-family: 'Montserrat', sans-serif;\n"
"font-weight:700;\n"
"font-size:90px;\n"
"color:#FFF")
        self.temp_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.temp_sttring = QLabel(self.frame)
        self.temp_sttring.setObjectName(u"temp_sttring")
        self.temp_sttring.setGeometry(QRect(90, 460, 361, 91))
        self.temp_sttring.setFont(font)
        self.temp_sttring.setStyleSheet(u"background-color:none;\n"
"font-family: 'Montserrat', sans-serif;\n"
"font-weight:700;\n"
"font-size:40px;\n"
"color:#FFF")
        self.temp_sttring.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.day_label = QLabel(self.frame)
        self.day_label.setObjectName(u"day_label")
        self.day_label.setGeometry(QRect(80, 60, 361, 71))
        self.day_label.setFont(font)
        self.day_label.setStyleSheet(u"background-color:none;\n"
"font-family: 'Montserrat', sans-serif;\n"
"font-weight:700;\n"
"font-size:40px;\n"
"color:#FFF")
        self.day_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.day_dmy = QLabel(self.frame)
        self.day_dmy.setObjectName(u"day_dmy")
        self.day_dmy.setGeometry(QRect(100, 120, 331, 51))
        self.day_dmy.setFont(font)
        self.day_dmy.setStyleSheet(u"background-color:none;\n"
"font-family: 'Montserrat', sans-serif;\n"
"font-weight:700;\n"
"font-size:20px;\n"
"color:#FFF")
        self.day_dmy.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(110, 170, 16, 21))
        self.label_6.setStyleSheet(u"background-color: none;")
        self.label_6.setPixmap(QPixmap(u":/newPrefix/F:/lifeboxyedek/white-location-icon-plectrum-light-stencil-hand-transparent-png-1510888.png"))
        self.label_6.setScaledContents(True)
        self.icon_label = QLabel(self.frame)
        self.icon_label.setObjectName(u"icon_label")
        self.icon_label.setGeometry(QRect(100, 210, 141, 131))
        self.icon_label.setStyleSheet(u"background-color:none;")
        self.icon_label.setPixmap(QPixmap(u":/weather/picdir/weather/64x64/day/113.png"))
        self.icon_label.setScaledContents(True)
        self.icon_label.setAlignment(Qt.AlignCenter)
        self.frame_8 = QFrame(self.frame)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setGeometry(QRect(800, 160, 251, 51))
        font2 = QFont()
        font2.setPointSize(10)
        self.frame_8.setFont(font2)
        self.frame_8.setStyleSheet(u"QFrame{\n"
"background-color: none;\n"
"}\n"
"QFrame:hover{\n"
"background-color:rgb(48,57,66);\n"
"}")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(70, 50, 391, 531))
        self.label_3.setStyleSheet(u"border-radius:45px;\n"
"background-color:qlineargradient(spread:pad, x1:0.01, y1:0, x2:1, y2:1, stop:0.0696517 rgba(0, 80, 219, 99), stop:0.835821 rgba(0, 240, 255, 199))\n"
"")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(70, 50, 391, 531))
        self.label_2.setStyleSheet(u"background-image: url(:/newPrefix/picdir/background/photo-1559963110-71b394e7494d.jpeg);\n"
"\n"
"border-radius:45px")
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(1070, 10, 41, 31))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"\n"
"color:#FFF;\n"
"border-radius:20px ;\n"
"	background-color: rgb(24, 28, 33);\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"\n"
"background-color:rgb(48,57,66);\n"
"\n"
"\n"
"}")
        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(1020, 10, 41, 31))
        font3 = QFont()
        font3.setFamily(u"Segoe UI Symbol")
        font3.setPointSize(15)
        self.pushButton_2.setFont(font3)
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"\n"
"color:#FFF;\n"
"border-radius:20px ;\n"
"	background-color: rgb(24, 28, 33);\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"\n"
"background-color:rgb(48,57,66);\n"
"\n"
"\n"
"}")
        self.wind_label_2 = QLabel(self.frame)
        self.wind_label_2.setObjectName(u"wind_label_2")
        self.wind_label_2.setGeometry(QRect(730, 70, 251, 51))
        self.wind_label_2.setFont(font1)
        self.wind_label_2.setStyleSheet(u"QFrame{\n"
"color:#FFF;\n"
"\n"
"}\n"
"QFrame:Hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:1 rgba(0, 0, 0, 84));\n"
"}")
        self.wind_label_2.setAlignment(Qt.AlignCenter)
        self.lowtemp = QLabel(self.frame)
        self.lowtemp.setObjectName(u"lowtemp")
        self.lowtemp.setGeometry(QRect(250, 420, 201, 71))
        font4 = QFont()
        font4.setBold(True)
        font4.setWeight(87)
        self.lowtemp.setFont(font4)
        self.lowtemp.setStyleSheet(u"background-color:none;\n"
"\n"
"font-weight:700;\n"
"font-size:40px;\n"
"color: rgb(80, 80, 80);")
        self.lowtemp.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.day_dmy_2 = QLabel(self.frame)
        self.day_dmy_2.setObjectName(u"day_dmy_2")
        self.day_dmy_2.setGeometry(QRect(100, 160, 321, 51))
        self.day_dmy_2.setFont(font)
        self.day_dmy_2.setStyleSheet(u"background-color:none;\n"
"font-family: 'Montserrat', sans-serif;\n"
"font-weight:700;\n"
"font-size:20px;\n"
"color:#FFF")
        self.day_dmy_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.frame_10 = QFrame(self.frame)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setGeometry(QRect(560, 250, 110, 180))
        self.frame_10.setStyleSheet(u"QFrame{\n"
"background-color:rgb(30,40,56);\n"
"}\n"
"QFrame:hover{\n"
"\n"
"background-color:rgb(48,57,66);\n"
"\n"
"\n"
"}")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.submenuicon1_1 = QLabel(self.frame_10)
        self.submenuicon1_1.setObjectName(u"submenuicon1_1")
        self.submenuicon1_1.setGeometry(QRect(20, 10, 61, 71))
        self.submenuicon1_1.setStyleSheet(u"background-color:none;")
        self.submenuicon1_1.setPixmap(QPixmap(u":/weather/picdir/weather/64x64/day/113.png"))
        self.submenuicon1_1.setScaledContents(True)
        self.submenuicon1_1.setAlignment(Qt.AlignCenter)
        self.submenu_day_1 = QLabel(self.frame_10)
        self.submenu_day_1.setObjectName(u"submenu_day_1")
        self.submenu_day_1.setGeometry(QRect(10, 60, 81, 71))
        self.submenu_day_1.setFont(font)
        self.submenu_day_1.setStyleSheet(u"background-color:none;\n"
"font-family: 'Montserrat', sans-serif;\n"
"font-weight:700;\n"
"font-size:20px;\n"
"color:#FFF")
        self.submenu_day_1.setAlignment(Qt.AlignCenter)
        self.submenu_temp_1 = QLabel(self.frame_10)
        self.submenu_temp_1.setObjectName(u"submenu_temp_1")
        self.submenu_temp_1.setGeometry(QRect(10, 100, 101, 81))
        self.submenu_temp_1.setFont(font)
        self.submenu_temp_1.setStyleSheet(u"background-color:none;\n"
"font-family: 'Montserrat', sans-serif;\n"
"font-weight:700;\n"
"font-size:20px;\n"
"color:#FFF")
        self.submenu_temp_1.setAlignment(Qt.AlignCenter)
        self.submenu_temp_4 = QLabel(self.frame_10)
        self.submenu_temp_4.setObjectName(u"submenu_temp_4")
        self.submenu_temp_4.setGeometry(QRect(140, 130, 81, 81))
        self.submenu_temp_4.setFont(font)
        self.submenu_temp_4.setStyleSheet(u"background-color:none;\n"
"font-family: 'Montserrat', sans-serif;\n"
"font-weight:700;\n"
"font-size:24px;\n"
"color:#FFF")
        self.submenu_temp_4.setAlignment(Qt.AlignCenter)
        self.abel_6 = QLabel(self.frame_10)
        self.abel_6.setObjectName(u"abel_6")
        self.abel_6.setGeometry(QRect(190, 150, 41, 41))
        self.abel_6.setFont(font)
        self.abel_6.setStyleSheet(u"background-color:none;\n"
"font-family: 'Montserrat', sans-serif;\n"
"font-weight:700;\n"
"font-size:24px;\n"
"color:#FFF")
        self.abel_6.setAlignment(Qt.AlignCenter)
        self.submenu_day_4 = QLabel(self.frame_10)
        self.submenu_day_4.setObjectName(u"submenu_day_4")
        self.submenu_day_4.setGeometry(QRect(150, 90, 81, 71))
        self.submenu_day_4.setFont(font)
        self.submenu_day_4.setStyleSheet(u"background-color:none;\n"
"font-family: 'Montserrat', sans-serif;\n"
"font-weight:700;\n"
"font-size:20px;\n"
"color:#FFF")
        self.submenu_day_4.setAlignment(Qt.AlignCenter)
        self.frame_12 = QFrame(self.frame)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setGeometry(QRect(800, 250, 110, 180))
        self.frame_12.setStyleSheet(u"QFrame{\n"
"background-color:rgb(30,40,56);\n"
"}\n"
"QFrame:hover{\n"
"\n"
"background-color:rgb(48,57,66);\n"
"\n"
"\n"
"}")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.submenuicon1_3 = QLabel(self.frame_12)
        self.submenuicon1_3.setObjectName(u"submenuicon1_3")
        self.submenuicon1_3.setGeometry(QRect(20, 10, 61, 71))
        self.submenuicon1_3.setStyleSheet(u"background-color:none;")
        self.submenuicon1_3.setPixmap(QPixmap(u":/weather/picdir/weather/64x64/day/113.png"))
        self.submenuicon1_3.setScaledContents(True)
        self.submenuicon1_3.setAlignment(Qt.AlignCenter)
        self.submenu_day_3 = QLabel(self.frame_12)
        self.submenu_day_3.setObjectName(u"submenu_day_3")
        self.submenu_day_3.setGeometry(QRect(10, 60, 81, 71))
        self.submenu_day_3.setFont(font)
        self.submenu_day_3.setStyleSheet(u"background-color:none;\n"
"font-family: 'Montserrat', sans-serif;\n"
"font-weight:700;\n"
"font-size:20px;\n"
"color:#FFF")
        self.submenu_day_3.setAlignment(Qt.AlignCenter)
        self.submenu_temp_3 = QLabel(self.frame_12)
        self.submenu_temp_3.setObjectName(u"submenu_temp_3")
        self.submenu_temp_3.setGeometry(QRect(10, 100, 101, 81))
        self.submenu_temp_3.setFont(font)
        self.submenu_temp_3.setStyleSheet(u"background-color:none;\n"
"font-family: 'Montserrat', sans-serif;\n"
"font-weight:700;\n"
"font-size:20px;\n"
"color:#FFF")
        self.submenu_temp_3.setAlignment(Qt.AlignCenter)
        self.frame_13 = QFrame(self.frame)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setGeometry(QRect(920, 250, 110, 180))
        self.frame_13.setStyleSheet(u"QFrame{\n"
"background-color:rgb(30,40,56);\n"
"}\n"
"QFrame:hover{\n"
"\n"
"background-color:rgb(48,57,66);\n"
"\n"
"\n"
"}")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.submenuicon1_4 = QLabel(self.frame_13)
        self.submenuicon1_4.setObjectName(u"submenuicon1_4")
        self.submenuicon1_4.setGeometry(QRect(20, 10, 61, 71))
        self.submenuicon1_4.setStyleSheet(u"background-color:none;")
        self.submenuicon1_4.setPixmap(QPixmap(u":/weather/picdir/weather/64x64/day/113.png"))
        self.submenuicon1_4.setScaledContents(True)
        self.submenuicon1_4.setAlignment(Qt.AlignCenter)
        self.submenu_day_5 = QLabel(self.frame_13)
        self.submenu_day_5.setObjectName(u"submenu_day_5")
        self.submenu_day_5.setGeometry(QRect(10, 60, 81, 71))
        self.submenu_day_5.setFont(font)
        self.submenu_day_5.setStyleSheet(u"background-color:none;\n"
"font-family: 'Montserrat', sans-serif;\n"
"font-weight:700;\n"
"font-size:20px;\n"
"color:#FFF")
        self.submenu_day_5.setAlignment(Qt.AlignCenter)
        self.submenu_temp_7 = QLabel(self.frame_13)
        self.submenu_temp_7.setObjectName(u"submenu_temp_7")
        self.submenu_temp_7.setGeometry(QRect(0, 100, 101, 81))
        self.submenu_temp_7.setFont(font)
        self.submenu_temp_7.setStyleSheet(u"background-color:none;\n"
"font-family: 'Montserrat', sans-serif;\n"
"font-weight:700;\n"
"font-size:20px;\n"
"color:#FFF")
        self.submenu_temp_7.setAlignment(Qt.AlignCenter)
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(410, 50, 641, 531))
        self.label_4.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.895522, y1:0.432, x2:1, y2:0.426, stop:1 rgba(0, 0, 0, 94));\n"
"\n"
"border-radius:45px;")
        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(590, 480, 411, 51))
        font5 = QFont()
        font5.setFamily(u"Segoe UI Semibold")
        font5.setPointSize(18)
        font5.setBold(True)
        font5.setWeight(75)
        self.lineEdit.setFont(font5)
        self.lineEdit.setCursor(QCursor(Qt.IBeamCursor))
        self.lineEdit.setMouseTracking(True)
        self.lineEdit.setFocusPolicy(Qt.ClickFocus)
        self.lineEdit.setStyleSheet(u"color:#FFF;\n"
"border-radius:25px;\n"
"background-color: qlineargradient(spread:pad, x1:0.01, y1:0, x2:1, y2:1, stop:0.0696517 rgba(0, 80, 219, 99), stop:0.835821 rgba(0, 240, 255, 199));\n"
"")
        self.lineEdit.setMaxLength(50)
        self.lineEdit.setFrame(True)
        self.lineEdit.setAlignment(Qt.AlignCenter)
        self.lineEdit.setDragEnabled(True)
        self.lineEdit.setCursorMoveStyle(Qt.VisualMoveStyle)
        self.lineEdit.setClearButtonEnabled(True)
        self.pushButton_3 = QPushButton(self.frame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(590, 480, 411, 51))
        self.pushButton_3.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/newPrefix/F:/lifeboxyedek/white-location-icon-plectrum-light-stencil-hand-transparent-png-1510888.png);\n"
"border-radius:20px;\n"
"}\n"
"QPushButton:hover{\n"
"\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.975124, y2:0.563, stop:0 rgba(0, 59, 255, 148), stop:1 rgba(76, 76, 76, 151));\n"
"\n"
"\n"
"}")
        icon = QIcon()
        icon.addFile(u":/newPrefix/picdir/white-location-icon-plectrum-light-stencil-hand-transparent-png-1510888.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setIconSize(QSize(35, 35))
        self.label_4.raise_()
        self.label.raise_()
        self.label_5.raise_()
        self.frame_8.raise_()
        self.label_2.raise_()
        self.frame_3.raise_()
        self.label_6.raise_()
        self.label_3.raise_()
        self.temp_sttring.raise_()
        self.day_label.raise_()
        self.day_dmy.raise_()
        self.temp_label.raise_()
        self.icon_label.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.wind_label.raise_()
        self.wind_label_2.raise_()
        self.lowtemp.raise_()
        self.day_dmy_2.raise_()
        self.frame_10.raise_()
        self.frame_12.raise_()
        self.frame_13.raise_()
        self.lineEdit.raise_()
        self.pushButton_3.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.submenuicon1_2.setText("")
        self.submenu_day_2.setText(QCoreApplication.translate("MainWindow", u"Tue", None))
        self.submenu_temp_2.setText(QCoreApplication.translate("MainWindow", u"29 ", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>    HUMIDITY</p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<strong>WIND</strong>", None))
        self.wind_label.setText("")
        self.temp_label.setText(QCoreApplication.translate("MainWindow", u"21", None))
        self.temp_sttring.setText(QCoreApplication.translate("MainWindow", u"Sunny", None))
        self.day_label.setText(QCoreApplication.translate("MainWindow", u"Day", None))
        self.day_dmy.setText(QCoreApplication.translate("MainWindow", u"15 JAN 2022", None))
        self.label_6.setText("")
        self.icon_label.setText("")
        self.label_3.setText("")
        self.label_2.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"_", None))
        self.wind_label_2.setText("")
        self.lowtemp.setText(QCoreApplication.translate("MainWindow", u"10 C", None))
        self.day_dmy_2.setText(QCoreApplication.translate("MainWindow", u"15 JAN 2022", None))
        self.submenuicon1_1.setText("")
        self.submenu_day_1.setText(QCoreApplication.translate("MainWindow", u"Tue", None))
        self.submenu_temp_1.setText(QCoreApplication.translate("MainWindow", u"29 ", None))
        self.submenu_temp_4.setText(QCoreApplication.translate("MainWindow", u"29 ", None))
        self.abel_6.setText(QCoreApplication.translate("MainWindow", u"\u00b0C", None))
        self.submenu_day_4.setText(QCoreApplication.translate("MainWindow", u"Tue", None))
        self.submenuicon1_3.setText("")
        self.submenu_day_3.setText(QCoreApplication.translate("MainWindow", u"Tue", None))
        self.submenu_temp_3.setText(QCoreApplication.translate("MainWindow", u"29 ", None))
        self.submenuicon1_4.setText("")
        self.submenu_day_5.setText(QCoreApplication.translate("MainWindow", u"Tue", None))
        self.submenu_temp_7.setText(QCoreApplication.translate("MainWindow", u"29 ", None))
        self.label_4.setText("")
        self.lineEdit.setText("")
        self.pushButton_3.setText("")
    # retranslateUi


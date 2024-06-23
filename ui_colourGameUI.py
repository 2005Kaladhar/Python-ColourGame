# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'colourGameUIYFVlPq.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, 
    QMetaObject,  QRect,
    QSize, Qt)
from PySide6.QtWidgets import ( QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton,
    QRadioButton, QSizePolicy, QSlider, QSpacerItem,
    QSpinBox, QStackedWidget, QVBoxLayout, QWidget)

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(650, 450)
        MainWindow.setStyleSheet(u"QMainWindow{\n"
"\n"
"	background-image: url(:/newPrefix/images/HomeScreen.png);\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(0, 450))
        self.centralwidget.setStyleSheet(u"QWidget{\n"
"	border-radius:10px;\n"
"	background-image: url(:/newPrefix/images/HomeScreen.png);\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.windowFrame = QFrame(self.centralwidget)
        self.windowFrame.setObjectName(u"windowFrame")
        self.windowFrame.setMinimumSize(QSize(0, 25))
        self.windowFrame.setMaximumSize(QSize(16777215, 25))
        self.windowFrame.setStyleSheet(u"QFrame{\n"
"background:none;\n"
"	background-color: rgb(255, 186, 33);\n"
"border-radius:10px;;\n"
"}")
        self.windowFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_2 = QHBoxLayout(self.windowFrame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 6, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.windowButtonFrame = QFrame(self.windowFrame)
        self.windowButtonFrame.setObjectName(u"windowButtonFrame")
        self.windowButtonFrame.setMaximumSize(QSize(62, 16777215))
        self.windowButtonFrame.setStyleSheet(u"QFrame{\n"
"background:none;\n"
"\n"
"border-radius:0px;;\n"
"}")
        self.windowButtonFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout = QHBoxLayout(self.windowButtonFrame)
        self.horizontalLayout.setSpacing(24)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.minimiseButton = QPushButton(self.windowButtonFrame)
        self.minimiseButton.setObjectName(u"minimiseButton")
        self.minimiseButton.setMinimumSize(QSize(17, 17))
        self.minimiseButton.setMaximumSize(QSize(17, 17))
        self.minimiseButton.setStyleSheet(u"QPushButton{\n"
"background:none;\n"
"background-position:centre;\n"
"background-repeat:none;\n"
"border-radius:0px;\n"
"\n"
"\n"
"	background-image: url(:/newPrefix/images/minimiseButton.png);\n"
"\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-image: url(:/newPrefix/images/minimiseButtonHover.png);\n"
"}")

        self.horizontalLayout.addWidget(self.minimiseButton)

        self.closeButton = QPushButton(self.windowButtonFrame)
        self.closeButton.setObjectName(u"closeButton")
        self.closeButton.setMinimumSize(QSize(18, 19))
        self.closeButton.setMaximumSize(QSize(17, 17))
        self.closeButton.setStyleSheet(u"QPushButton{\n"
"background:none;\n"
"background-position:centre;\n"
"background-repeat:none;\n"
"border-radius:0px;\n"
"\n"
"\n"
"\n"
"	background-image: url(:/newPrefix/images/closeButton.png);\n"
"\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-image: url(:/newPrefix/images/closeButtonHover.png);\n"
"}")

        self.horizontalLayout.addWidget(self.closeButton)


        self.horizontalLayout_2.addWidget(self.windowButtonFrame)


        self.verticalLayout.addWidget(self.windowFrame)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame{\n"
"background:none;\n"
"\n"
"border-radius:0px;\n"
"}")
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 65)
        self.horizontalSpacer_2 = QSpacerItem(72, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 0, 1, 1)

        self.settingsButton = QPushButton(self.frame)
        self.settingsButton.setObjectName(u"settingsButton")
        self.settingsButton.setMinimumSize(QSize(26, 22))
        self.settingsButton.setMaximumSize(QSize(30, 19))
        self.settingsButton.setStyleSheet(u"QPushButton{\n"
"background:none;\n"
"background-position:centre;\n"
"background-repeat:none;\n"
"border-radius:0px;\n"
"\n"
"\n"
"	background-image: url(:/newPrefix/images/settingButton.png);\n"
"\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-image: url(:/newPrefix/images/settingButtonHover.png);\n"
"\n"
"}")

        self.gridLayout.addWidget(self.settingsButton, 0, 3, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(72, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.horizontalSpacer_3, 1, 2, 1, 2)

        self.horizontalSpacer_4 = QSpacerItem(36, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.horizontalSpacer_4, 0, 0, 1, 3)

        self.stackedWidget = QStackedWidget(self.frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(500, 300))
        self.stackedWidget.setMaximumSize(QSize(500, 300))
        self.stackedWidget.setStyleSheet(u"\n"
"\n"
"background:none;\n"
"border-radius:0px;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"background-color: rgba(169, 169, 169, 000);\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_2 = QVBoxLayout(self.page)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer = QSpacerItem(20, 206, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.frame_2 = QFrame(self.page)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"")
        self.frame_2.setFrameShape(QFrame.Shape.NoFrame)
        self.gridLayout_2 = QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.playButton = QPushButton(self.frame_2)
        self.playButton.setObjectName(u"playButton")
        self.playButton.setMinimumSize(QSize(130, 63))
        self.playButton.setMaximumSize(QSize(129, 61))
        self.playButton.setStyleSheet(u"QPushButton{\n"
"background:none;\n"
"background-position:centre;\n"
"background-repeat:none;\n"
"border-radius:0px;\n"
"\n"
"margin-top:10px;\n"
"	background-image: url(:/newPrefix/images/playButton.png);\n"
"\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"\n"
"	background-image: url(:/newPrefix/images/playButtonHover.png);\n"
"}")

        self.gridLayout_2.addWidget(self.playButton, 0, 1, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(158, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.horizontalSpacer_5, 0, 0, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(178, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.horizontalSpacer_6, 0, 2, 1, 1)

        self.playButton.raise_()

        self.verticalLayout_2.addWidget(self.frame_2)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.horizontalLayout_3 = QHBoxLayout(self.page_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame_3 = QFrame(self.page_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"QFrame{\n"
"background-image: url(:/newPrefix/images/introFrame.png);\n"
"\n"
"\n"
"background-repeat:none;\n"
"background-position:centre;\n"
"\n"
"}")
        self.frame_3.setFrameShape(QFrame.Shape.NoFrame)
        self.gridLayout_3 = QGridLayout(self.frame_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalSpacer_2 = QSpacerItem(20, 213, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 0, 1, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(179, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.horizontalSpacer_7, 1, 0, 1, 1)

        self.startButton = QPushButton(self.frame_3)
        self.startButton.setObjectName(u"startButton")
        self.startButton.setMinimumSize(QSize(104, 56))
        self.startButton.setMaximumSize(QSize(104, 56))
        self.startButton.setStyleSheet(u"QPushButton{\n"
"background:none;\n"
"background-position:centre;\n"
"background-repeat:none;\n"
"border-radius:0px;\n"
"\n"
"margin-top:10px;\n"
"	background-image: url(:/newPrefix/images/startButton.png);\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-image: url(:/newPrefix/images/startButtonHover.png);\n"
"}")

        self.gridLayout_3.addWidget(self.startButton, 1, 1, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(179, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.horizontalSpacer_8, 1, 2, 1, 1)


        self.horizontalLayout_3.addWidget(self.frame_3)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.gridLayout_5 = QGridLayout(self.page_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(-1, 2, -1, 6)
        self.verticalSpacer_5 = QSpacerItem(20, 44, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_5, 4, 1, 1, 1)

        self.horizontalSpacer_12 = QSpacerItem(67, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.horizontalSpacer_12, 1, 2, 1, 1)

        self.horizontalSpacer_14 = QSpacerItem(68, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.horizontalSpacer_14, 1, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 3, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_3, 0, 1, 1, 1)

        self.frame_5 = QFrame(self.page_3)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setMinimumSize(QSize(339, 171))
        self.frame_5.setMaximumSize(QSize(341, 171))
        self.frame_5.setStyleSheet(u"QFrame{\n"
"background-image: url(:/newPrefix/images/SettingsBackground.png);\n"
"\n"
"background-repeat:none;\n"
"background-position:centre;\n"
"background-color:none;\n"
"\n"
"}")
        self.frame_5.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_7 = QFrame(self.frame_5)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(131, 9, 201, 151))
        self.frame_7.setStyleSheet(u"QFrame{\n"
"background:none;\n"
"\n"
"\n"
"\n"
"}")
        self.frame_7.setFrameShape(QFrame.Shape.NoFrame)
        self.gridLayout_4 = QGridLayout(self.frame_7)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.volumeSlider = QSlider(self.frame_7)
        self.volumeSlider.setObjectName(u"volumeSlider")
        self.volumeSlider.setMinimumSize(QSize(132, 0))
        self.volumeSlider.setStyleSheet(u"QSlider::groove:horizontal {\n"
"  \n"
"    height: 5px; /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */\n"
"	border-radius:2px;\n"
"	background-color: rgb(170, 170, 170);\n"
"    margin: 2px 0;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    border:1px  solid grey;\n"
"	background-color: rgb(251, 178, 94);\n"
"    width: 16px;\n"
"height:10px;\n"
"border-radius:3px;\n"
"    margin: -2px 0; /* handle is placed by default on the contents rect of the groove. Expand outside the groove */\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.volumeSlider.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_4.addWidget(self.volumeSlider, 0, 0, 1, 1)

        self.timeout = QSpinBox(self.frame_7)
        self.timeout.setObjectName(u"timeout")
        self.timeout.setStyleSheet(u"QSpinBox\n"
"{\n"
"    border: none;\n"
"	\n"
"	font: 10pt \"Segoe UI\";\n"
"	\n"
"	color: rgb(90, 90, 90);\n"
"   background-color: rgba(0, 0, 0, 0);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"}\n"
"\n"
"QSpinBox::up-button\n"
"{\n"
"    min-width: 23px;\n"
"    min-height: 20px;\n"
"	bottom:6px;\n"
"    subcontrol-position: top left; /* position at the top right corner */\n"
"}\n"
"\n"
"\n"
"QSpinBox::down-button\n"
"{\n"
"  min-width: 23px;\n"
"    min-height: 20px;\n"
"	top:8px;\n"
"\n"
"    subcontrol-position: bottom  left; /* position at the top right corner */\n"
"\n"
"}\n"
"\n"
"\n"
"")

        self.gridLayout_4.addWidget(self.timeout, 2, 0, 1, 1)

        self.spellCheck = QRadioButton(self.frame_7)
        self.spellCheck.setObjectName(u"spellCheck")
        self.spellCheck.setStyleSheet(u"QRadioButton{\n"
"\n"
"	font: 8.5pt \"Segoe UI\";\n"
"	\n"
"	color: rgb(90, 90, 90);\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"width: 11px;\n"
"height: 11px;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QRadioButton::indicator::unchecked{ \n"
"border: 1px solid; \n"
"border-color: rgb(132,132,132);\n"
"border-radius: 5px;\n"
"background-color: white; \n"
"width: 11px; \n"
"height: 11px; \n"
"}\n"
"\n"
"QRadioButton::indicator::checked{ \n"
"border: 3px solid; \n"
"border-color: white;\n"
"border-radius: 6px;\n"
"	background-color: rgb(255, 132, 25);\n"
"width: 7px; \n"
"height: 7px; \n"
"}")
        self.spellCheck.setAutoExclusive(False)

        self.gridLayout_4.addWidget(self.spellCheck, 3, 0, 1, 1)

        self.volumeLabel = QLabel(self.frame_7)
        self.volumeLabel.setObjectName(u"volumeLabel")
        self.volumeLabel.setStyleSheet(u"QLabel{\n"
"font: 10.5pt \"Segoe UI\";\n"
"	margin-right:5px;\n"
"	color: rgb(90, 90, 90);\n"
"}")

        self.gridLayout_4.addWidget(self.volumeLabel, 0, 3, 1, 1)

        self.bgmOnly = QRadioButton(self.frame_7)
        self.bgmOnly.setObjectName(u"bgmOnly")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.bgmOnly.sizePolicy().hasHeightForWidth())
        self.bgmOnly.setSizePolicy(sizePolicy1)
        self.bgmOnly.setStyleSheet(u"QRadioButton{\n"
"\n"
"	font: 7.5pt \"Segoe UI\";\n"
"	margin-right:5px;\n"
"	color: rgb(90, 90, 90);\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"width: 11px;\n"
"height: 11px;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QRadioButton::indicator::unchecked{ \n"
"border: 1px solid; \n"
"border-color: rgb(132,132,132);\n"
"border-radius: 5px;\n"
"background-color: white; \n"
"width: 11px; \n"
"height: 11px; \n"
"}\n"
"\n"
"QRadioButton::indicator::checked{ \n"
"border: 3px solid; \n"
"border-color: white;\n"
"border-radius: 6px;\n"
"	background-color: rgb(255, 132, 25);\n"
"width: 7px; \n"
"height: 7px; \n"
"}")

        self.gridLayout_4.addWidget(self.bgmOnly, 1, 0, 1, 1)

        self.noBgm = QRadioButton(self.frame_7)
        self.noBgm.setObjectName(u"noBgm")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.noBgm.sizePolicy().hasHeightForWidth())
        self.noBgm.setSizePolicy(sizePolicy2)
        self.noBgm.setMinimumSize(QSize(95, 0))
        self.noBgm.setStyleSheet(u"\n"
"QRadioButton{\n"
"\n"
"	font: 7.5pt \"Segoe UI\";\n"
"	\n"
"	color: rgb(90, 90, 90);\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"width: 11px;\n"
"height: 11px;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QRadioButton::indicator::unchecked{ \n"
"border: 1px solid; \n"
"border-color: rgb(132,132,132);\n"
"border-radius: 5px;\n"
"background-color: white; \n"
"width: 11px; \n"
"height: 11px; \n"
"}\n"
"\n"
"QRadioButton::indicator::checked{ \n"
"border: 3px solid; \n"
"border-color: white;\n"
"border-radius: 6px;\n"
"	background-color: rgb(255, 132, 25);\n"
"width: 7px; \n"
"height: 7px; \n"
"}")

        self.gridLayout_4.addWidget(self.noBgm, 1, 1, 1, 1)


        self.gridLayout_5.addWidget(self.frame_5, 2, 1, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 3, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_4, 5, 1, 1, 1)

        self.frame_4 = QFrame(self.page_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"background-color:none;")
        self.frame_4.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(-1, -1, 6, -1)
        self.frame_6 = QFrame(self.frame_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"")
        self.frame_6.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.backtoHome = QPushButton(self.frame_6)
        self.backtoHome.setObjectName(u"backtoHome")
        self.backtoHome.setMinimumSize(QSize(23, 23))
        self.backtoHome.setMaximumSize(QSize(23, 23))
        self.backtoHome.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/newPrefix/images/triangleIcon.png);\n"
"background-repeat:none;\n"
"background-position:centre;\n"
"\n"
"}\n"
"QPushButton::hover{\n"
"background-image: url(:/newPrefix/images/triangleIconHover.png);\n"
"}")

        self.horizontalLayout_5.addWidget(self.backtoHome)

        self.label_4 = QLabel(self.frame_6)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(40, 0))
        self.label_4.setStyleSheet(u"QLabel{\n"
"font: 11pt \"Segoe UI\";\n"
"\n"
"	color: rgb(134, 134, 134);\n"
"}")

        self.horizontalLayout_5.addWidget(self.label_4)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_16)


        self.horizontalLayout_7.addWidget(self.frame_6)

        self.frame_8 = QFrame(self.frame_4)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"background-color:none;\n"
"")
        self.frame_8.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, -1, 0, -1)
        self.label_3 = QLabel(self.frame_8)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(47, 39))
        self.label_3.setMaximumSize(QSize(50, 16777215))
        self.label_3.setStyleSheet(u"QLabel{\n"
"\n"
"	background-image: url(:/newPrefix/images/settingsLargeIcon.png);\n"
"background-repeat:none;\n"
"background-position:centre;\n"
"background-color:none;\n"
"}")

        self.horizontalLayout_6.addWidget(self.label_3)

        self.label_2 = QLabel(self.frame_8)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(83, 0))
        self.label_2.setStyleSheet(u"QLabel{\n"
"font: 13pt \"Segoe UI\";\n"
"\n"
"	color: rgb(134, 134, 134);\n"
"}")

        self.horizontalLayout_6.addWidget(self.label_2)


        self.horizontalLayout_7.addWidget(self.frame_8)

        self.horizontalSpacer_11 = QSpacerItem(96, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_11)


        self.gridLayout_5.addWidget(self.frame_4, 1, 1, 1, 1)

        self.horizontalSpacer_15 = QSpacerItem(68, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.horizontalSpacer_15, 2, 0, 1, 1)

        self.horizontalSpacer_13 = QSpacerItem(67, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.horizontalSpacer_13, 2, 2, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 43, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_6, 3, 1, 1, 1)

        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.horizontalLayout_8 = QHBoxLayout(self.page_4)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_23 = QSpacerItem(69, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_23)

        self.frame_9 = QFrame(self.page_4)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setStyleSheet(u"QFrame{\n"
"\n"
"background-repeat:none;\n"
"background-position:right;\n"
"background-color:rgba(63, 63, 63, 000);\n"
"\n"
"}")
        self.frame_9.setFrameShape(QFrame.Shape.NoFrame)
        self.gridLayout_6 = QGridLayout(self.frame_9)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_7, 3, 1, 1, 1)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_9, 0, 1, 1, 1)

        self.textArea = QLineEdit(self.frame_9)
        self.textArea.setObjectName(u"textArea")
        self.textArea.setMinimumSize(QSize(221, 41))
        self.textArea.setMaximumSize(QSize(221, 41))
        self.textArea.setStyleSheet(u"QLineEdit{\n"
"\n"
"	border-radius:20px;\n"
"	background-color: rgb(255, 255, 255);\n"
"	\n"
"	color: rgb(77, 77, 77);\n"
"	\n"
"	font: 9.5pt \"Segoe UI\";\n"
"}\n"
"\n"
"\n"
"")
        self.textArea.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_6.addWidget(self.textArea, 4, 1, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 57, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_8, 1, 1, 1, 1)

        self.colorLabel = QLabel(self.frame_9)
        self.colorLabel.setObjectName(u"colorLabel")
        self.colorLabel.setMinimumSize(QSize(220, 98))
        self.colorLabel.setMaximumSize(QSize(210, 98))
        self.colorLabel.setStyleSheet(u"QLabel{\n"
"\n"
"color:black;\n"
"	font: 50pt \"Segoe UI\";\n"
"	\n"
"border-bottom-left-radius:40px;\n"
"border-top-right-radius:40px;\n"
"background:none;\n"
"\n"
"\n"
"background-repeat:none;\n"
"background-position:centre;\n"
"\n"
"	\n"
"\n"
"\n"
"	\n"
"}")
        self.colorLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_6.addWidget(self.colorLabel, 2, 1, 1, 1)

        self.pointsLabel = QLabel(self.frame_9)
        self.pointsLabel.setObjectName(u"pointsLabel")
        self.pointsLabel.setStyleSheet(u"QLabel{\n"
"\n"
"color:black;\n"
"	\n"
"	font: 63 13pt \"Segoe UI\";\n"
"	\n"
"border-radius:10px;\n"
"background:none;\n"
"}")

        self.gridLayout_6.addWidget(self.pointsLabel, 1, 2, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(55, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_6.addItem(self.horizontalSpacer_9, 2, 2, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(41, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_6.addItem(self.horizontalSpacer_10, 2, 0, 1, 1)


        self.horizontalLayout_8.addWidget(self.frame_9)

        self.horizontalSpacer_22 = QSpacerItem(68, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_22)

        self.stackedWidget.addWidget(self.page_4)

        self.gridLayout.addWidget(self.stackedWidget, 1, 1, 1, 1)


        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.minimiseButton.setText("")
        self.closeButton.setText("")
        self.settingsButton.setText("")
        self.playButton.setText("")
        self.startButton.setText("")
        self.spellCheck.setText(QCoreApplication.translate("MainWindow", u"Enable", None))
        self.volumeLabel.setText(QCoreApplication.translate("MainWindow", u"30%", None))
        self.bgmOnly.setText(QCoreApplication.translate("MainWindow", u"Bgm ", None))
        self.noBgm.setText(QCoreApplication.translate("MainWindow", u"No Music", None))
        self.backtoHome.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.label_3.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.textArea.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter name of colour", None))
        self.colorLabel.setText(QCoreApplication.translate("MainWindow", u"Black", None))
        self.pointsLabel.setText(QCoreApplication.translate("MainWindow", u"Points : ", None))
    # retranslateUi


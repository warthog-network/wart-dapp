# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'entry_screen.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QWidget)
import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.resize(1000, 696)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1000, 696))
        MainWindow.setMaximumSize(QSize(1450, 930))
        font = QFont()
        font.setFamilies([u"Playbill"])
        font.setBold(True)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/icon/icons/icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color:#16191d;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.centralwidget.setMinimumSize(QSize(1450, 930))
        self.centralwidget.setMaximumSize(QSize(1450, 930))
        font1 = QFont()
        font1.setBold(True)
        self.centralwidget.setFont(font1)
        self.centralwidget.setStyleSheet(u"body {\n"
"    width: 100vw;\n"
"    height: 100vh;\n"
"    margin: 0;\n"
"    background-color: var(--bg);\n"
"    color: white;\n"
"}")
        self.public_button = QPushButton(self.centralwidget)
        self.public_button.setObjectName(u"public_button")
        self.public_button.setGeometry(QRect(370, 260, 287, 41))
        font2 = QFont()
        font2.setFamilies([u"MS Sans Serif"])
        font2.setBold(False)
        font2.setItalic(False)
        font2.setUnderline(False)
        font2.setStrikeOut(False)
        self.public_button.setFont(font2)
        self.public_button.setStyleSheet(u"QPushButton{background-color: rgba(0, 0, 0, 0);\n"
"font-size:28px;\n"
"color:white;\n"
"hover:{color:white;}\n"
"}\n"
"QPushButton:hover{\n"
"color:white;\n"
"border: 2px solid rgba(255,255,255,40);\n"
"border-radius:10px;\n"
"background-color: rgba(255,255,255,60);\n"
"}")
        self.input_field = QLineEdit(self.centralwidget)
        self.input_field.setObjectName(u"input_field")
        self.input_field.setGeometry(QRect(380, 310, 261, 51))
        font3 = QFont()
        font3.setFamilies([u"MS Sans Serif"])
        self.input_field.setFont(font3)
        self.input_field.setStyleSheet(u"color:black;\n"
"font-size:28px;\n"
"border-radius: 10px;\n"
"border: 1px solid rgba(255,255,255,40);\n"
"background-color: rgba(255,255,255,70);")
        self.input_field.setEchoMode(QLineEdit.Normal)
        self.input_field.setCursorPosition(12)
        self.input_field.setDragEnabled(True)
        self.input_field.setClearButtonEnabled(False)
        self.connect_button = QPushButton(self.centralwidget)
        self.connect_button.setObjectName(u"connect_button")
        self.connect_button.setGeometry(QRect(380, 370, 261, 41))
        font4 = QFont()
        font4.setFamilies([u"MS Sans Serif"])
        font4.setBold(False)
        self.connect_button.setFont(font4)
        self.connect_button.setStyleSheet(u"QPushButton{\n"
"border-radius: 10px;\n"
"font-size: 28px;\n"
"border: 2px solid rgba(255,255,255,40);\n"
"\n"
"color: white;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255,255,255,60);\n"
"color:white;\n"
"}")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(340, 40, 351, 140))
        self.label.setPixmap(QPixmap(u":/icon/icons/logo4.png"))
        self.headerContainer = QWidget(self.centralwidget)
        self.headerContainer.setObjectName(u"headerContainer")
        self.headerContainer.setGeometry(QRect(-450, 0, 1451, 41))
        self.headerContainer.setStyleSheet(u"background-color:#ffff;")
        self.horizontalLayout_5 = QHBoxLayout(self.headerContainer)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frame_6 = QFrame(self.headerContainer)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.headerContainer)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_5.addWidget(self.frame_7, 0, Qt.AlignHCenter)

        self.frame_8 = QFrame(self.headerContainer)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)


        self.horizontalLayout_5.addWidget(self.frame_8, 0, Qt.AlignRight)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Warthog Network", None))
        self.public_button.setText(QCoreApplication.translate("MainWindow", u"Connect public node", None))
        self.input_field.setInputMask("")
        self.input_field.setText(QCoreApplication.translate("MainWindow", u"Your node ip", None))
        self.connect_button.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.label.setText("")
    # retranslateUi


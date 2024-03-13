# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'wallets.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDialog, QFrame,
    QHBoxLayout, QLabel, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QWidget)
import res_rc

class Ui_WalletsWindow(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1000, 696)
        Dialog.setMinimumSize(QSize(1000, 696))
        Dialog.setMaximumSize(QSize(1000, 696))
        icon = QIcon()
        icon.addFile(u":/icon/icons/icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet(u"background-color:#16191d;\n"
"QPushButton{background-color: rgba(0, 0, 0, 0);\n"
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
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(330, 20, 341, 131))
        self.label.setPixmap(QPixmap(u":/icon/icons/logo4.png"))
        self.new_wallet_button = QPushButton(Dialog)
        self.new_wallet_button.setObjectName(u"new_wallet_button")
        self.new_wallet_button.setGeometry(QRect(360, 170, 281, 41))
        font = QFont()
        font.setFamilies([u"MS Sans Serif"])
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.new_wallet_button.setFont(font)
        self.new_wallet_button.setStyleSheet(u"QPushButton{background-color: rgba(0, 0, 0, 0);\n"
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
        self.listWidget = QListWidget(Dialog)
        QListWidgetItem(self.listWidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(140, 300, 721, 371))
        font1 = QFont()
        font1.setFamilies([u"MS Sans Serif"])
        font1.setBold(False)
        self.listWidget.setFont(font1)
        self.listWidget.setStyleSheet(u"font-size:28px;\n"
"border-radius:10px;\n"
"color:white;\n"
"border: 2px solid rgba(255,255,255,40);\n"
"")
        self.listWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listWidget.setEditTriggers(QAbstractItemView.DoubleClicked|QAbstractItemView.EditKeyPressed|QAbstractItemView.SelectedClicked)
        self.listWidget.setSelectionRectVisible(True)
        self.private_key_button = QPushButton(Dialog)
        self.private_key_button.setObjectName(u"private_key_button")
        self.private_key_button.setGeometry(QRect(360, 250, 281, 41))
        self.private_key_button.setFont(font)
        self.private_key_button.setStyleSheet(u"QPushButton{background-color: rgba(0, 0, 0, 0);\n"
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
        self.mnemonic_button = QPushButton(Dialog)
        self.mnemonic_button.setObjectName(u"mnemonic_button")
        self.mnemonic_button.setGeometry(QRect(330, 210, 341, 41))
        self.mnemonic_button.setFont(font)
        self.mnemonic_button.setStyleSheet(u"QPushButton{background-color: rgba(0, 0, 0, 0);\n"
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
        self.headerContainer = QWidget(Dialog)
        self.headerContainer.setObjectName(u"headerContainer")
        self.headerContainer.setGeometry(QRect(-10, 0, 1000, 41))
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


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Warthog Network", None))
        self.label.setText("")
        self.new_wallet_button.setText(QCoreApplication.translate("Dialog", u"Create new wallet", None))

        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("Dialog", u"7a787c4a626283fdd3501293187be7e93e022c79f32b7e0d", None));
        self.listWidget.setSortingEnabled(__sortingEnabled)

        self.private_key_button.setText(QCoreApplication.translate("Dialog", u"Add by Private Key", None))
        self.mnemonic_button.setText(QCoreApplication.translate("Dialog", u"Add by Mnemonic Phrase", None))
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'register.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QWidget)
import res_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(950, 345)
        Dialog.setMinimumSize(QSize(950, 345))
        Dialog.setMaximumSize(QSize(950, 345))
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
"}\n"
"border: 5px solid rgba(255,255,255,40);")
        Dialog.setModal(True)
        self.ok_btn = QPushButton(Dialog)
        self.ok_btn.setObjectName(u"ok_btn")
        self.ok_btn.setGeometry(QRect(440, 280, 75, 41))
        font = QFont()
        font.setFamilies([u"MS Sans Serif"])
        self.ok_btn.setFont(font)
        icon = QIcon()
        icon.addFile(u":/icon/icons/icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.ok_btn.setStyleSheet(u"QPushButton{background-color: rgba(0, 0, 0, 0);\n"
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
        self.mnemo_label = QLabel(Dialog)
        self.mnemo_label.setObjectName(u"mnemo_label")
        self.mnemo_label.setGeometry(QRect(50, 110, 841, 161))
        font1 = QFont()
        font1.setFamilies([u"MS Sans Serif"])
        font1.setPointSize(16)
        font1.setHintingPreference(QFont.PreferDefaultHinting)
        self.mnemo_label.setFont(font1)
        self.mnemo_label.setStyleSheet(u"color:yellow;")
        self.mnemo_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.mnemo_label.setWordWrap(True)
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 60, 841, 31))
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color:white;")
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_2.setWordWrap(True)
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 950, 345))
        self.frame.setStyleSheet(u"#frame{border: 5px solid rgba(255,255,255,40);}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.headerContainer = QWidget(self.frame)
        self.headerContainer.setObjectName(u"headerContainer")
        self.headerContainer.setGeometry(QRect(10, 10, 931, 41))
        self.headerContainer.setStyleSheet(u"background-color:#ffff;")
        self.horizontalLayout_5 = QHBoxLayout(self.headerContainer)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frame_7 = QFrame(self.headerContainer)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_5.addWidget(self.frame_7, 0, Qt.AlignHCenter)

        self.frame_6 = QFrame(self.headerContainer)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_6)

        self.frame_8 = QFrame(self.headerContainer)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)


        self.horizontalLayout_5.addWidget(self.frame_8, 0, Qt.AlignRight)

        self.frame.raise_()
        self.ok_btn.raise_()
        self.mnemo_label.raise_()
        self.label_2.raise_()

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Warthog Network: Mnemonic Phrase", None))
        self.ok_btn.setText(QCoreApplication.translate("Dialog", u"OK", None))
        self.mnemo_label.setText("")
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Save this mnemonic phrase:", None))
    # retranslateUi


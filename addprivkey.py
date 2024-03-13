# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'restore_privkey.ui'
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
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QWidget)
import res_rc

class Ui_Dialog_Priv(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(950, 400)
        Dialog.setMinimumSize(QSize(950, 400))
        Dialog.setMaximumSize(QSize(950, 400))
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
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 950, 401))
        self.frame.setStyleSheet(u"#frame{border: 5px solid rgba(255,255,255,40);}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.headerContainer_2 = QWidget(self.frame)
        self.headerContainer_2.setObjectName(u"headerContainer_2")
        self.headerContainer_2.setGeometry(QRect(10, 10, 931, 41))
        self.headerContainer_2.setStyleSheet(u"background-color:#ffff;")
        self.horizontalLayout_7 = QHBoxLayout(self.headerContainer_2)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.frame_9 = QFrame(self.headerContainer_2)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_7.addWidget(self.frame_9, 0, Qt.AlignHCenter)

        self.frame_10 = QFrame(self.headerContainer_2)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_7.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.headerContainer_2)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)


        self.horizontalLayout_7.addWidget(self.frame_11, 0, Qt.AlignRight)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 110, 261, 31))
        font = QFont()
        font.setFamilies([u"MS Sans Serif"])
        font.setPointSize(16)
        font.setHintingPreference(QFont.PreferDefaultHinting)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color:white;")
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_2.setWordWrap(True)
        self.ok_btn = QPushButton(self.frame)
        self.ok_btn.setObjectName(u"ok_btn")
        self.ok_btn.setGeometry(QRect(440, 280, 75, 41))
        font1 = QFont()
        font1.setFamilies([u"MS Sans Serif"])
        self.ok_btn.setFont(font1)
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
        self.pk_label = QLineEdit(self.frame)
        self.pk_label.setObjectName(u"pk_label")
        self.pk_label.setGeometry(QRect(40, 161, 871, 81))
        font2 = QFont()
        font2.setFamilies([u"MS Sans Serif"])
        font2.setPointSize(16)
        self.pk_label.setFont(font2)
        self.pk_label.setStyleSheet(u"color:white;\n"
"border-radius:10px;\n"
"border: 2px solid rgba(255,255,255,40);\n"
"")
        self.pk_label.setMaxLength(256)
        self.pk_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Warthog Network: Private Key", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Enter private key:", None))
        self.ok_btn.setText(QCoreApplication.translate("Dialog", u"OK", None))
    # retranslateUi


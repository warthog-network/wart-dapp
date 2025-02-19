# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
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
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTextEdit, QVBoxLayout, QWidget)
import res_rc

class Ui_MainWindow_Wart(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1300, 696)
        MainWindow.setMinimumSize(QSize(1300, 600))
        MainWindow.setMaximumSize(QSize(1300, 696))
        icon = QIcon()
        icon.addFile(u":/icon/icons/icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"*{\n"
"border:none;\n"
"background-color:transparent;\n"
"background: transparent;\n"
"padding: 0;\n"
"margin:0;\n"
"color:#fff;\n"
"\n"
"\n"
"}\n"
"\n"
"\n"
"#centralwidget{background-color: #333333	;}\n"
"\n"
"#leftMenuSub{\n"
"background-color:#16191d;\n"
"}\n"
"#leftMenuSub QPushButton{\n"
"text-align:left;\n"
"padding:13px 6px;\n"
"margin-left:5px;\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"}\n"
"#centerMenuSub{\n"
" background-color:#2c313c;\n"
"}\n"
"#frame_4, frame_8{\n"
"background-color:#16191d;\n"
"border-radius: 10px;\n"
"}\n"
"#headerContainer{\n"
" background-color:#2c313c;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color:white;\n"
"border: 2px solid rgba(255,255,255,40);\n"
"border-radius:10px;\n"
"background-color: rgba(255,255,255,60);\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenu = QWidget(self.centralwidget)
        self.leftMenu.setObjectName(u"leftMenu")
        self.verticalLayout = QVBoxLayout(self.leftMenu)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuSub = QWidget(self.leftMenu)
        self.leftMenuSub.setObjectName(u"leftMenuSub")
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuSub)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame = QFrame(self.leftMenuSub)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 140))
        self.frame.setMaximumSize(QSize(16777215, 140))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u":/icon/icons/logo4.png"))

        self.horizontalLayout_2.addWidget(self.label, 0, Qt.AlignTop)


        self.verticalLayout_3.addWidget(self.frame)

        self.frame_2 = QFrame(self.leftMenuSub)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setStyleSheet(u"margin-bottom:14px;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.address_button = QPushButton(self.frame_2)
        self.address_button.setObjectName(u"address_button")
        font = QFont()
        font.setFamilies([u"Microsoft YaHei Light"])
        font.setPointSize(16)
        self.address_button.setFont(font)
        self.address_button.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/icon/icons/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.address_button.setIcon(icon1)
        self.address_button.setIconSize(QSize(28, 28))

        self.verticalLayout_2.addWidget(self.address_button)

        self.send_button = QPushButton(self.frame_2)
        self.send_button.setObjectName(u"send_button")
        self.send_button.setFont(font)
        self.send_button.setStyleSheet(u"#send_button:click{\n"
"color:black;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icon/icons/sender.png", QSize(), QIcon.Normal, QIcon.Off)
        self.send_button.setIcon(icon2)
        self.send_button.setIconSize(QSize(28, 28))

        self.verticalLayout_2.addWidget(self.send_button)

        self.contact_button = QPushButton(self.frame_2)
        self.contact_button.setObjectName(u"contact_button")
        self.contact_button.setFont(font)
        icon3 = QIcon()
        icon3.addFile(u":/icon/icons/book-open.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.contact_button.setIcon(icon3)
        self.contact_button.setIconSize(QSize(28, 28))

        self.verticalLayout_2.addWidget(self.contact_button)

        self.transactions_button = QPushButton(self.frame_2)
        self.transactions_button.setObjectName(u"transactions_button")
        self.transactions_button.setFont(font)
        icon4 = QIcon()
        icon4.addFile(u":/icon/icons/icons8-\u0432\u043e\u0437\u0432\u0440\u0430\u0442-2-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.transactions_button.setIcon(icon4)
        self.transactions_button.setIconSize(QSize(28, 28))

        self.verticalLayout_2.addWidget(self.transactions_button)

        self.miners_button = QPushButton(self.frame_2)
        self.miners_button.setObjectName(u"miners_button")
        self.miners_button.setFont(font)
        icon5 = QIcon()
        icon5.addFile(u":/icon/icons/icons8-\u043f\u0435\u0449\u0435\u0440\u0430-51.png", QSize(), QIcon.Normal, QIcon.Off)
        self.miners_button.setIcon(icon5)
        self.miners_button.setIconSize(QSize(28, 28))

        self.verticalLayout_2.addWidget(self.miners_button)


        self.verticalLayout_3.addWidget(self.frame_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.notes = QPushButton(self.leftMenuSub)
        self.notes.setObjectName(u"notes")
        self.notes.setFont(font)
        self.notes.setStyleSheet(u"margin-top:15px;\n"
"padding-top:20px;")
        icon6 = QIcon()
        icon6.addFile(u":/icon/icons/calendar.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.notes.setIcon(icon6)
        self.notes.setIconSize(QSize(28, 28))

        self.verticalLayout_3.addWidget(self.notes, 0, Qt.AlignBottom)

        self.frame_3 = QFrame(self.leftMenuSub)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.browser_btn = QPushButton(self.frame_3)
        self.browser_btn.setObjectName(u"browser_btn")
        self.browser_btn.setStyleSheet(u"color:white;")
        icon7 = QIcon()
        icon7.addFile(u":/icon/icons/icons8-\u0438\u043d\u0442\u0435\u0440\u043d\u0435\u0442-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.browser_btn.setIcon(icon7)
        self.browser_btn.setIconSize(QSize(40, 40))

        self.horizontalLayout_3.addWidget(self.browser_btn)

        self.twitter_btn = QPushButton(self.frame_3)
        self.twitter_btn.setObjectName(u"twitter_btn")
        self.twitter_btn.setStyleSheet(u"color:white;")
        icon8 = QIcon()
        icon8.addFile(u":/icon/icons/twitter.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.twitter_btn.setIcon(icon8)
        self.twitter_btn.setIconSize(QSize(40, 40))

        self.horizontalLayout_3.addWidget(self.twitter_btn)

        self.discord_btn = QPushButton(self.frame_3)
        self.discord_btn.setObjectName(u"discord_btn")
        self.discord_btn.setStyleSheet(u"color:white;")
        icon9 = QIcon()
        icon9.addFile(u":/icon/icons/discord.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.discord_btn.setIcon(icon9)
        self.discord_btn.setIconSize(QSize(40, 40))

        self.horizontalLayout_3.addWidget(self.discord_btn)

        self.telegram_btn = QPushButton(self.frame_3)
        self.telegram_btn.setObjectName(u"telegram_btn")
        self.telegram_btn.setStyleSheet(u"color:white;")
        icon10 = QIcon()
        icon10.addFile(u":/icon/icons/icons8-\u0442\u0435\u043b\u0435\u0433\u0440\u0430\u043c-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.telegram_btn.setIcon(icon10)
        self.telegram_btn.setIconSize(QSize(40, 40))

        self.horizontalLayout_3.addWidget(self.telegram_btn)

        self.git_btn = QPushButton(self.frame_3)
        self.git_btn.setObjectName(u"git_btn")
        self.git_btn.setStyleSheet(u"color:white;")
        icon11 = QIcon()
        icon11.addFile(u":/icon/icons/icons8-github-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.git_btn.setIcon(icon11)
        self.git_btn.setIconSize(QSize(40, 40))

        self.horizontalLayout_3.addWidget(self.git_btn)


        self.verticalLayout_3.addWidget(self.frame_3, 0, Qt.AlignBottom)


        self.verticalLayout.addWidget(self.leftMenuSub, 0, Qt.AlignLeft)


        self.horizontalLayout.addWidget(self.leftMenu)

        self.mainBody = QWidget(self.centralwidget)
        self.mainBody.setObjectName(u"mainBody")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.mainBody.sizePolicy().hasHeightForWidth())
        self.mainBody.setSizePolicy(sizePolicy1)
        self.mainBody.setStyleSheet(u"background-color:#16191d;")
        self.verticalLayout_10 = QVBoxLayout(self.mainBody)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.headerContainer = QWidget(self.mainBody)
        self.headerContainer.setObjectName(u"headerContainer")
        self.headerContainer.setMouseTracking(True)
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
        self.pushButton_4 = QPushButton(self.frame_8)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setLayoutDirection(Qt.LeftToRight)


        self.horizontalLayout_5.addWidget(self.frame_8, 0, Qt.AlignRight)


        self.verticalLayout_10.addWidget(self.headerContainer)

        self.mainBodyContent = QWidget(self.mainBody)
        self.mainBodyContent.setObjectName(u"mainBodyContent")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.mainBodyContent.sizePolicy().hasHeightForWidth())
        self.mainBodyContent.setSizePolicy(sizePolicy2)
        self.horizontalLayout_7 = QHBoxLayout(self.mainBodyContent)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.mainContent = QWidget(self.mainBodyContent)
        self.mainContent.setObjectName(u"mainContent")
        self.stackedWidget = QStackedWidget(self.mainContent)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(-10, 40, 611, 581))
        font1 = QFont()
        font1.setFamilies([u"Microsoft YaHei UI"])
        self.stackedWidget.setFont(font1)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.label_12 = QLabel(self.page_6)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(20, 210, 141, 41))
        font2 = QFont()
        font2.setFamilies([u"Microsoft YaHei UI Light"])
        font2.setPointSize(19)
        font2.setBold(True)
        self.label_12.setFont(font2)
        self.label_13 = QLabel(self.page_6)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(20, 310, 581, 61))
        font3 = QFont()
        font3.setFamilies([u"Microsoft YaHei UI Light"])
        font3.setPointSize(12)
        font3.setBold(True)
        self.label_13.setFont(font3)
        self.label_13.setScaledContents(True)
        self.label_13.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_13.setWordWrap(True)
        self.label_14 = QLabel(self.page_6)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(20, 260, 201, 41))
        font4 = QFont()
        font4.setFamilies([u"Microsoft YaHei UI Light"])
        font4.setPointSize(11)
        font4.setBold(False)
        self.label_14.setFont(font4)
        self.label_16 = QLabel(self.page_6)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(20, 10, 141, 41))
        self.label_16.setFont(font2)
        self.label_17 = QLabel(self.page_6)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(20, 60, 191, 41))
        self.label_17.setFont(font4)
        self.label_18 = QLabel(self.page_6)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(20, 110, 581, 61))
        self.label_18.setFont(font3)
        self.label_18.setScaledContents(True)
        self.label_18.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_18.setWordWrap(True)
        self.stackedWidget.addWidget(self.page_6)
        self.label_13.raise_()
        self.label_12.raise_()
        self.label_14.raise_()
        self.label_16.raise_()
        self.label_17.raise_()
        self.label_18.raise_()
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.stackedWidget.addWidget(self.page_7)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.label_3 = QLabel(self.page)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 50, 41, 41))
        self.label_3.setTextFormat(Qt.RichText)
        self.label_3.setPixmap(QPixmap(u":/icon/icons/icons8-payment-method-64.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_3.setOpenExternalLinks(True)
        self.address_text = QTextEdit(self.page)
        self.address_text.setObjectName(u"address_text")
        self.address_text.setGeometry(QRect(70, 50, 541, 41))
        font5 = QFont()
        font5.setFamilies([u"Segoe UI Light"])
        font5.setBold(False)
        font5.setItalic(False)
        font5.setUnderline(False)
        self.address_text.setFont(font5)
        self.address_text.setStyleSheet(u"border-radius: 15px;\n"
"font-size: 20px;\n"
"background-color: rgba(200,200,255,40);\n"
"border: 1px solid rgba(255,255,255,40);")
        self.address_text.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.address_text.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.address_text.setReadOnly(True)
        self.label_15 = QLabel(self.page)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(260, 20, 111, 21))
        font6 = QFont()
        font6.setFamilies([u"Microsoft YaHei UI Light"])
        font6.setPointSize(16)
        self.label_15.setFont(font6)
        self.copy_btn = QPushButton(self.page)
        self.copy_btn.setObjectName(u"copy_btn")
        self.copy_btn.setGeometry(QRect(560, 50, 51, 41))
        self.copy_btn.setStyleSheet(u"color:white;\n"
"background:none;")
        icon14 = QIcon()
        icon14.addFile(u":/icon/icons/copy.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.copy_btn.setIcon(icon14)
        self.copy_btn.setIconSize(QSize(24, 24))
        self.stackedWidget.addWidget(self.page)
        self.address_text.raise_()
        self.label_3.raise_()
        self.label_15.raise_()
        self.copy_btn.raise_()
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setStyleSheet(u"")
        self.fee_text = QLineEdit(self.page_2)
        self.fee_text.setObjectName(u"fee_text")
        self.fee_text.setGeometry(QRect(10, 250, 601, 31))
        font7 = QFont()
        font7.setFamilies([u"MS Sans Serif"])
        font7.setPointSize(16)
        self.fee_text.setFont(font7)
        self.fee_text.setStyleSheet(u"color:white;\n"
"border-radius:10px;\n"
"border: 2px solid rgba(255,255,255,40);\n"
"background-color: rgba(200,200,255,40);")
        self.fee_text.setMaxLength(256)
        self.fee_text.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.send_btn = QPushButton(self.page_2)
        self.send_btn.setObjectName(u"send_btn")
        self.send_btn.setGeometry(QRect(270, 310, 63, 35))
        font8 = QFont()
        font8.setFamilies([u"Microsoft JhengHei UI Light"])
        self.send_btn.setFont(font8)
        self.send_btn.setStyleSheet(u"QPushButton{background-color: rgba(0, 0, 0, 0);\n"
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
        self.amount_text = QLineEdit(self.page_2)
        self.amount_text.setObjectName(u"amount_text")
        self.amount_text.setGeometry(QRect(10, 170, 601, 31))
        self.amount_text.setFont(font7)
        self.amount_text.setStyleSheet(u"color:white;\n"
"border-radius:10px;\n"
"border: 2px solid rgba(255,255,255,40);\n"
"background-color: rgba(200,200,255,40);")
        self.amount_text.setMaxLength(256)
        self.amount_text.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_6 = QLabel(self.page_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 210, 38, 26))
        self.label_6.setMaximumSize(QSize(16777215, 30))
        font9 = QFont()
        font9.setFamilies([u"Microsoft JhengHei UI Light"])
        font9.setPointSize(16)
        font9.setHintingPreference(QFont.PreferDefaultHinting)
        self.label_6.setFont(font9)
        self.label_6.setStyleSheet(u"color:white;")
        self.label_6.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_6.setWordWrap(True)
        self.label_4 = QLabel(self.page_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setEnabled(True)
        self.label_4.setGeometry(QRect(9, 48, 593, 30))
        self.label_4.setMinimumSize(QSize(4, 0))
        self.label_4.setMaximumSize(QSize(16777215, 30))
        self.label_4.setFont(font9)
        self.label_4.setStyleSheet(u"color:white;")
        self.label_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_4.setWordWrap(True)
        self.addr_text = QLineEdit(self.page_2)
        self.addr_text.setObjectName(u"addr_text")
        self.addr_text.setGeometry(QRect(10, 90, 601, 31))
        self.addr_text.setFont(font7)
        self.addr_text.setStyleSheet(u"color:white;\n"
"border-radius:10px;\n"
"border: 2px solid rgba(255,255,255,40);\n"
"background-color: rgba(200,200,255,40);")
        self.addr_text.setMaxLength(256)
        self.addr_text.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_5 = QLabel(self.page_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 130, 593, 25))
        self.label_5.setMaximumSize(QSize(600, 25))
        self.label_5.setFont(font9)
        self.label_5.setStyleSheet(u"color:white;")
        self.label_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_5.setWordWrap(True)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        font10 = QFont()
        font10.setFamilies([u"Segoe UI"])
        self.page_3.setFont(font10)
        self.friends = QListWidget(self.page_3)
        self.friends.setObjectName(u"friends")
        self.friends.setGeometry(QRect(20, 120, 581, 401))
        self.friends.setStyleSheet(u"font-size:28px;\n"
"border-radius:10px;\n"
"color:white;\n"
"border: 2px solid rgba(255,255,255,40);\n"
"")
        self.add_bttn = QPushButton(self.page_3)
        self.add_bttn.setObjectName(u"add_bttn")
        self.add_bttn.setGeometry(QRect(280, 530, 75, 41))
        self.add_bttn.setFont(font8)
        self.add_bttn.setStyleSheet(u"QPushButton{background-color: rgba(0, 0, 0, 0);\n"
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
        self.addr_text_2 = QLineEdit(self.page_3)
        self.addr_text_2.setObjectName(u"addr_text_2")
        self.addr_text_2.setGeometry(QRect(110, 20, 491, 41))
        self.addr_text_2.setFont(font7)
        self.addr_text_2.setStyleSheet(u"color:white;\n"
"border-radius:10px;\n"
"border: 2px solid rgba(255,255,255,40);\n"
"background-color: rgba(200,200,255,40);\n"
"")
        self.addr_text_2.setMaxLength(256)
        self.addr_text_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_8 = QLabel(self.page_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(20, 10, 91, 51))
        self.label_8.setFont(font6)
        self.addr_text_3 = QLineEdit(self.page_3)
        self.addr_text_3.setObjectName(u"addr_text_3")
        self.addr_text_3.setGeometry(QRect(110, 70, 491, 41))
        self.addr_text_3.setFont(font7)
        self.addr_text_3.setStyleSheet(u"color:white;\n"
"border-radius:10px;\n"
"border: 2px solid rgba(255,255,255,40);\n"
"background-color: rgba(200,200,255,40);")
        self.addr_text_3.setMaxLength(256)
        self.addr_text_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_11 = QLabel(self.page_3)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(20, 50, 111, 71))
        self.label_11.setFont(font6)
        self.stackedWidget.addWidget(self.page_3)
        self.label_8.raise_()
        self.label_11.raise_()
        self.friends.raise_()
        self.add_bttn.raise_()
        self.addr_text_2.raise_()
        self.addr_text_3.raise_()
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.friends_2 = QListWidget(self.page_4)
        self.friends_2.setObjectName(u"friends_2")
        self.friends_2.setGeometry(QRect(20, 70, 581, 451))
        self.friends_2.setStyleSheet(u"font-size:19px;\n"
"border-radius:10px;\n"
"color:white;\n"
"border: 2px solid rgba(255,255,255,40);\n"
"")
        self.label_9 = QLabel(self.page_4)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(20, 0, 81, 71))
        self.label_9.setFont(font6)
        self.blocks_btn = QLineEdit(self.page_4)
        self.blocks_btn.setObjectName(u"blocks_btn")
        self.blocks_btn.setGeometry(QRect(100, 20, 501, 41))
        self.blocks_btn.setFont(font7)
        self.blocks_btn.setStyleSheet(u"color:white;\n"
"border-radius:10px;\n"
"border: 2px solid rgba(255,255,255,40);\n"
"background-color: rgba(200,200,255,40);\n"
"")
        self.blocks_btn.setMaxLength(256)
        self.blocks_btn.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.show_btn = QPushButton(self.page_4)
        self.show_btn.setObjectName(u"show_btn")
        self.show_btn.setGeometry(QRect(190, 530, 241, 31))
        self.show_btn.setFont(font8)
        self.show_btn.setStyleSheet(u"QPushButton{background-color: rgba(0, 0, 0, 0);\n"
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
        self.stackedWidget.addWidget(self.page_4)
        self.label_9.raise_()
        self.friends_2.raise_()
        self.blocks_btn.raise_()
        self.show_btn.raise_()
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.miners_lst = QListWidget(self.page_5)
        QListWidgetItem(self.miners_lst)
        self.miners_lst.setObjectName(u"miners_lst")
        self.miners_lst.setGeometry(QRect(20, 70, 581, 451))
        self.miners_lst.setStyleSheet(u"font-size:19px;\n"
"border-radius:10px;\n"
"color:white;\n"
"border: 2px solid rgba(255,255,255,40);\n"
"")
        self.miners_lst.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.label_10 = QLabel(self.page_5)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(20, 0, 81, 71))
        self.label_10.setFont(font6)
        self.blocks_btn_2 = QLineEdit(self.page_5)
        self.blocks_btn_2.setObjectName(u"blocks_btn_2")
        self.blocks_btn_2.setGeometry(QRect(100, 20, 501, 41))
        self.blocks_btn_2.setFont(font7)
        self.blocks_btn_2.setStyleSheet(u"color:white;\n"
"border-radius:10px;\n"
"border: 2px solid rgba(255,255,255,40);\n"
"background-color: rgba(200,200,255,40);\n"
"")
        self.blocks_btn_2.setMaxLength(256)
        self.blocks_btn_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.show_miners = QPushButton(self.page_5)
        self.show_miners.setObjectName(u"show_miners")
        self.show_miners.setGeometry(QRect(190, 530, 241, 31))
        self.show_miners.setFont(font8)
        self.show_miners.setStyleSheet(u"QPushButton{background-color: rgba(0, 0, 0, 0);\n"
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
        self.stackedWidget.addWidget(self.page_5)
        self.label_10.raise_()
        self.miners_lst.raise_()
        self.blocks_btn_2.raise_()
        self.show_miners.raise_()
        self.label_2 = QLabel(self.mainContent)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(360, 0, 91, 31))
        self.label_2.setFont(font)
        self.label_7 = QLabel(self.mainContent)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(320, -110, 41, 171))
        font11 = QFont()
        font11.setPointSize(84)
        font11.setBold(False)
        self.label_7.setFont(font11)
        self.label_7.setStyleSheet(u"color:green;")
        self.label_7.setAlignment(Qt.AlignCenter)
        self.balance = QLabel(self.mainContent)
        self.balance.setObjectName(u"balance")
        self.balance.setGeometry(QRect(440, 0, 151, 31))
        self.balance.setFont(font)
        self.label_7.raise_()
        self.stackedWidget.raise_()
        self.label_2.raise_()
        self.balance.raise_()

        self.horizontalLayout_7.addWidget(self.mainContent)


        self.verticalLayout_10.addWidget(self.mainBodyContent)


        self.horizontalLayout.addWidget(self.mainBody)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.address_button.setText(QCoreApplication.translate("MainWindow", u"Address", None))
        self.send_button.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        self.contact_button.setText(QCoreApplication.translate("MainWindow", u"Address Book", None))
        self.transactions_button.setText(QCoreApplication.translate("MainWindow", u"Transactions Chain", None))
        self.miners_button.setText(QCoreApplication.translate("MainWindow", u"Miners Chain", None))
        self.notes.setText(QCoreApplication.translate("MainWindow", u"Release Notes", None))
        self.browser_btn.setText("")
        self.twitter_btn.setText("")
        self.discord_btn.setText("")
        self.telegram_btn.setText("")
        self.git_btn.setText("")
        self.pushButton_4.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Version 1.0", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"In this version of dapp were added address,send,address book,transactions,miners tabs.Give feedback about use experiense.", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Thursday, 15 February 2024", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Version 1.1", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Friday, 8 March 2024", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"In this version of dapp were changed sizes of dapp screens and some fields appearance,the list of public nodes has been expanded,added \"Copy to clipboard\" button near your wallet address,also were added fee amount as default.", None))
        self.label_3.setText("")
        self.address_text.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI Light'; font-size:16px; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">c176b667206e0b92edcaf4a555893a36ba11ce5c1910f2b1</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px;\">r</span></p></body></html>", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Your wallet:", None))
        self.copy_btn.setText("")
        self.fee_text.setText(QCoreApplication.translate("MainWindow", u"0.00000001", None))
        self.send_btn.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Fee:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Enter recipient address:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Amount:", None))
        self.add_bttn.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.addr_text_2.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.addr_text_3.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Address:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Blocks:", None))
        self.show_btn.setText(QCoreApplication.translate("MainWindow", u"Show transactions", None))

        __sortingEnabled = self.miners_lst.isSortingEnabled()
        self.miners_lst.setSortingEnabled(False)
        ___qlistwidgetitem = self.miners_lst.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", None));
        self.miners_lst.setSortingEnabled(__sortingEnabled)

        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Blocks:", None))
        self.show_miners.setText(QCoreApplication.translate("MainWindow", u"Show miners", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Balance:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.balance.setText("")
    # retranslateUi

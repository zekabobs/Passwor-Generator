
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(500, 192)
        MainWindow.setMaximumSize(QSize(500, 192))
        MainWindow.setMinimumSize(QSize(500, 192))
        MainWindow.setSizeIncrement(QSize(400, 192))
        MainWindow.setMouseTracking(False)
        MainWindow.setTabletTracking(False)
        MainWindow.setContextMenuPolicy(Qt.ActionsContextMenu)
        MainWindow.setAcceptDrops(False)
        icon = QIcon()
        icon.addFile(u"share.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setLayoutDirection(Qt.LeftToRight)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"background-color: #ffbd08;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 79, 50, 22))
        font = QFont()
        font.setFamily(u"Century Gothic")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setContextMenuPolicy(Qt.PreventContextMenu)
        self.label.setStyleSheet(u"font-size: 14pt;\n"
"font-family: Century Gothic;\n"
"")
        self.label.setAlignment(Qt.AlignCenter)
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(20, 19, 371, 30))
        font1 = QFont()
        font1.setFamily(u"Century Gothic")
        font1.setPointSize(16)
        self.lineEdit.setFont(font1)
        self.lineEdit.setContextMenuPolicy(Qt.PreventContextMenu)
        self.lineEdit.setStyleSheet(u"background-color: #333230;\n"
"color: #ffffff;\n"
"border: 2px solid #000000;\n"
"border-radius: 10px;\n"
"font-size: 16pt;\n"
"font-family: Century Gothic;")
        self.lineEdit.setMaxLength(20)
        self.lineEdit.setEchoMode(QLineEdit.Normal)
        self.lineEdit.setAlignment(Qt.AlignCenter)
        self.horizontalSlider = QSlider(self.centralwidget)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setGeometry(QRect(30, 57, 441, 20))
        self.horizontalSlider.setContextMenuPolicy(Qt.PreventContextMenu)
        self.horizontalSlider.setMinimum(1)
        self.horizontalSlider.setMaximum(4)
        self.horizontalSlider.setPageStep(1)
        self.horizontalSlider.setSliderPosition(3)
        self.horizontalSlider.setOrientation(Qt.Horizontal)
        self.horizontalSlider.setTickPosition(QSlider.TicksBelow)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(300, 80, 50, 22))
        self.label_2.setFont(font)
        self.label_2.setContextMenuPolicy(Qt.PreventContextMenu)
        self.label_2.setStyleSheet(u"font-size: 14pt;\n"
"font-family: Century Gothic;")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(140, 79, 70, 22))
        self.label_3.setFont(font)
        self.label_3.setContextMenuPolicy(Qt.PreventContextMenu)
        self.label_3.setStyleSheet(u"font-size: 14pt;\n"
"font-family: Century Gothic;")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(20, 140, 451, 31))
        self.pushButton.setContextMenuPolicy(Qt.PreventContextMenu)
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"	background-color: #333230;\n"
"	color: #ffffff;\n"
"	border-radius: 10px;\n"
"	border: 2px solid #000000;\n"
"	font-size: 14pt;\n"
"	font-family: Century Gothic 'bold';\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #464544;\n"
"	color: #ffffff;\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: #6C6960;\n"
"	color: #ffffff;\n"
"}")
        self.spinBox = QSpinBox(self.centralwidget)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setGeometry(QRect(410, 20, 61, 31))
        self.spinBox.setStyleSheet(u"	background-color: #333230;\n"
"	color: #ffffff;\n"
"	border-radius: 4px;\n"
"	border: 2px solid #000000;\n"
"	font-size: 14pt;\n"
"	font-family: Century Gothic 'bold';")
        self.spinBox.setMinimum(4)
        self.spinBox.setMaximum(20)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(430, 80, 50, 22))
        self.label_4.setFont(font)
        self.label_4.setContextMenuPolicy(Qt.PreventContextMenu)
        self.label_4.setStyleSheet(u"font-size: 14pt;\n"
"font-family: Century Gothic;")
        self.label_4.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Password Generator", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"E", None))
        self.lineEdit.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"H", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"M", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"VH", None))
    # retranslateUi
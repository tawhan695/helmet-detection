import sys
from os import path

import cv2
import numpy as np

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton,QLabel,QFileDialog
from PyQt5.QtCore import pyqtSlot
import time
from random import *

class Ui_MainWindow(object):
    FileName = "file error"
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(1920, 1080) 
        font = QtGui.QFont()
        font.setFamily("Ink Free")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        MainWindow.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        MainWindow.setWindowTitle("Detect helmet")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon/motorbike_helmet_48px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(4.0)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(41, 48, 51);")
        MainWindow.setAnimated(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.frame_video = QtWidgets.QFrame(self.centralwidget)
        self.frame_video.setGeometry(QtCore.QRect(25, 120, 1280, 720))
        self.frame_video.setStyleSheet("background-color: rgb(22, 24, 25);\n""image: url(icon/video_100px.png);\n""\n""")
        self.frame_video.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_video.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_video.setObjectName("frame_video")

        self.Video = QtWidgets.QLabel(self.frame_video)
        self.Video.setGeometry(QtCore.QRect(0, 0, 1280, 720))
        self.Video.setText("")
        self.Video.setScaledContents(True)
        self.Video.setObjectName("Video")
        
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 1921, 71)) 
        self.label_4.setStyleSheet("background-color: rgb(30, 35, 38);\n""")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")

        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(1290, 70, 615, 1020)) 
        font = QtGui.QFont()
        font.setStrikeOut(False)
        self.widget.setFont(font)
        self.widget.setAcceptDrops(False)
        self.widget.setObjectName("widget")

        self.Show_img = QtWidgets.QFrame(self.widget)
        self.Show_img.setGeometry(QtCore.QRect(100, 50,413,483))
        self.Show_img.setStyleSheet("background-color: rgb(22, 24, 25);\n""image: url(icon/picture_filled_100px.png);")
        self.Show_img.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Show_img.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Show_img.setObjectName("Show_img")

        self.IMG_show = QtWidgets.QLabel(self.Show_img)
        self.IMG_show.setGeometry(QtCore.QRect(50, 50,313,383))
        self.IMG_show.setText("")
        self.IMG_show.setObjectName("IMG_show")

        self.frame_4 = QtWidgets.QFrame(self.Show_img)
        self.frame_4.setGeometry(QtCore.QRect(1140, 410, 1280, 720)) 
        self.frame_4.setStyleSheet("background-color: rgb(22, 24, 25);\n""")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")

        self.label_icon_helmet = QtWidgets.QLabel(self.widget)
        self.label_icon_helmet.setGeometry(QtCore.QRect(90, 550, 121, 101)) 
        self.label_icon_helmet.setStyleSheet("image: url(icon/motorbike_helmet_filled_100px.png);")
        self.label_icon_helmet.setText("")
        self.label_icon_helmet.setObjectName("label_icon_helmet")

        self.label_icon_person = QtWidgets.QLabel(self.widget)
        self.label_icon_person.setGeometry(QtCore.QRect(90, 660, 121, 101)) 
        self.label_icon_person.setStyleSheet("image: url(icon/user_male_filled_100px.png);")
        self.label_icon_person.setText("")
        self.label_icon_person.setObjectName("label_icon_person")

        self.label_helmet = QtWidgets.QLabel(self.widget)
        self.label_helmet.setGeometry(QtCore.QRect(230, 560, 511, 51)) 
        self.label_helmet.setStyleSheet("font: 24pt \"Ink Free\";\n""color: rgb(255, 255, 255);")
        self.label_helmet.setObjectName("label_helmet")

        self.label_no_helmet = QtWidgets.QLabel(self.widget)
        self.label_no_helmet.setGeometry(QtCore.QRect(220, 690, 501, 51))
        self.label_no_helmet.setStyleSheet("font: 24pt \"Ink Free\";\n""color: rgb(255, 255, 255);")
        self.label_no_helmet.setObjectName("label_no_helmet")

        self.widget_button = QtWidgets.QWidget(self.centralwidget)
        self.widget_button.setGeometry(QtCore.QRect(25, 860, 1280, 121)) 
        self.widget_button.setStyleSheet("background-color:rgb(24, 28, 31);\n""  border-radius: 10px;")
        self.widget_button.setObjectName("widget_button")

        self.stop_video = QtWidgets.QPushButton(self.widget_button)
        self.stop_video.setGeometry(QtCore.QRect(670, 30, 193, 63)) 
        self.stop_video.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.stop_video.setStyleSheet("width:500px;\n""color: rgb(255, 0, 0);\n""height:500px;\n""border-ridge:40px;\n""font: 15pt \"Ink Free\";\n""  border-radius: 5px;\n""background-color: rgb(54, 66, 71);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icon/stop_squared_filled_100px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stop_video.setIcon(icon1)
        self.stop_video.setIconSize(QtCore.QSize(40, 50))
        self.stop_video.setObjectName("stop_video")
        self.stop_video.setEnabled(False)

        self.play_video = QtWidgets.QPushButton(self.widget_button)
        self.play_video.setGeometry(QtCore.QRect(470, 30, 194, 63)) 
        self.play_video.setBaseSize(QtCore.QSize(0, 1))
        self.play_video.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        
        font = QtGui.QFont()
        font.setFamily("Ink Free")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)

        self.play_video.setFont(font)
        self.play_video.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.play_video.setStyleSheet("width:500px;\n""\n""font: 15pt \"Ink Free\";\n""color: rgb(255, 0, 0);\n""height:500px;\n""border-ridge:40px;\n""background-color: rgb(54, 66, 71);\n""")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icon/play_button_circled_60px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.play_video.setIcon(icon2)
        self.play_video.setIconSize(QtCore.QSize(50, 50))
        self.play_video.setObjectName("play_video")
        
        self.open_file_video = QtWidgets.QPushButton(self.widget_button)
        self.open_file_video.setGeometry(QtCore.QRect(270, 30, 194, 63))
        self.open_file_video.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.open_file_video.setStyleSheet("width:500px;\n""color: rgb(255, 255, 255);\n""height:500px;\n""border-ridge:40px;\n""font: 15pt \"Ink Free\";\n""background-color: rgb(54, 66, 71);")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icon/opened_folder_filled_100px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.open_file_video.setIcon(icon3)
        self.open_file_video.setIconSize(QtCore.QSize(40, 50))
        self.open_file_video.setObjectName("open_file_video")
       


       


        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1870, 20, 30, 30))
        self.pushButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icon/close_window_filled_30px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon4)
        self.pushButton.setIconSize(QtCore.QSize(30, 30))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_minimize = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_minimize.setGeometry(QtCore.QRect(1840, 20, 30, 30))
        self.pushButton_minimize.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icon/minimize_window_filled_30px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_minimize.setIcon(icon5)
        self.pushButton_minimize.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_minimize.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_minimize.setObjectName("pushButton")

        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(90, 10, 261, 51))
        self.label_title.setStyleSheet("font: 24pt \"Ink Free\";\n""background-color: rgb(30, 35, 38);\n""color: rgb(255, 255, 255);")
        self.label_title.setObjectName("label_title")
        self.label_icon_title = QtWidgets.QLabel(self.centralwidget)
        self.label_icon_title.setGeometry(QtCore.QRect(20, 10, 50, 50))
        self.label_icon_title.setStyleSheet("image: url(icon/motorbike_helmet_50px.png);\n""background-color: rgb(30, 35, 38);")
        self.label_icon_title.setText("")
        self.label_icon_title.setObjectName("label_icon_title")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_file = QtWidgets.QAction(MainWindow)
        self.actionOpen_file.setObjectName("actionOpen_file")
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_helmet.setText(_translate("MainWindow", "With helmet : 0"))
        self.label_no_helmet.setText(_translate("MainWindow", "No helmet : 0"))
        self.stop_video.setText(_translate("MainWindow", "Stop"))
        self.play_video.setText(_translate("MainWindow", "Play"))
        self.open_file_video.setText(_translate("MainWindow", "Open file video"))
        self.pushButton.setToolTip(_translate("MainWindow", "Close"))
        self.pushButton_minimize.setToolTip(_translate("MainWindow", "Minimize"))
        self.label_title.setText(_translate("MainWindow", "Helmet Detection"))
        self.actionOpen_file.setText(_translate("MainWindow", "Open file"))

if __name__=='__main__':
    import sys
    Program =  QtWidgets.QApplication(sys.argv)
    MainWindows =QtWidgets.QMainWindow()
    MyProg = Ui_MainWindow()
    MyProg.setupUi(MainWindows)
    MainWindows.show()
    sys.exit(Program.exec_())


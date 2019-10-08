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
        MainWindow.resize(1920, 1080) #set size frame 1080p hd
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
        MainWindow.setWindowFlag(QtCore.Qt.FramelessWindowHint)  #set unTapbar title
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.frame_video = QtWidgets.QFrame(self.centralwidget)
        self.frame_video.setGeometry(QtCore.QRect(25, 120, 1280, 720)) #set lacation x y,size x y
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
        self.label_4.setGeometry(QtCore.QRect(0, 0, 1921, 71)) #set lacation x y,size x y
        self.label_4.setStyleSheet("background-color: rgb(30, 35, 38);\n""")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")

        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(1290, 70, 615, 1020)) #set lacation x y,size x y
        font = QtGui.QFont()
        font.setStrikeOut(False)
        self.widget.setFont(font)
        self.widget.setAcceptDrops(False)
        self.widget.setObjectName("widget")

        self.Show_img = QtWidgets.QFrame(self.widget)
        self.Show_img.setGeometry(QtCore.QRect(100, 50,413,483)) #set lacation x y,size x y
        self.Show_img.setStyleSheet("background-color: rgb(22, 24, 25);\n""image: url(icon/picture_filled_100px.png);")
        self.Show_img.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Show_img.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Show_img.setObjectName("Show_img")   

        self.IMG_show = QtWidgets.QLabel(self.Show_img)
        self.IMG_show.setGeometry(QtCore.QRect(50, 50,313,383))
        self.IMG_show.setText("")
        self.IMG_show.setObjectName("IMG_show")

        self.frame_4 = QtWidgets.QFrame(self.Show_img)
        self.frame_4.setGeometry(QtCore.QRect(1140, 410, 1280, 720)) #set lacation x y,size x y
        self.frame_4.setStyleSheet("background-color: rgb(22, 24, 25);\n""")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")

        self.label_icon_helmet = QtWidgets.QLabel(self.widget)
        self.label_icon_helmet.setGeometry(QtCore.QRect(90, 550, 121, 101)) #set lacation x y,size x y
        self.label_icon_helmet.setStyleSheet("image: url(icon/motorbike_helmet_filled_100px.png);")
        self.label_icon_helmet.setText("")
        self.label_icon_helmet.setObjectName("label_icon_helmet")

        self.label_icon_person = QtWidgets.QLabel(self.widget)
        self.label_icon_person.setGeometry(QtCore.QRect(90, 660, 121, 101)) #set lacation x y,size x y
        self.label_icon_person.setStyleSheet("image: url(icon/user_male_filled_100px.png);")
        self.label_icon_person.setText("")
        self.label_icon_person.setObjectName("label_icon_person")

        self.label_helmet = QtWidgets.QLabel(self.widget)
        self.label_helmet.setGeometry(QtCore.QRect(230, 560, 511, 51)) #set lacation x y,size x y
        self.label_helmet.setStyleSheet("font: 24pt \"Ink Free\";\n""color: rgb(255, 255, 255);")
        self.label_helmet.setObjectName("label_helmet")
        # self.label_helmet.setText("000000")

        self.label_no_helmet = QtWidgets.QLabel(self.widget)
        self.label_no_helmet.setGeometry(QtCore.QRect(220, 690, 501, 51)) #set lacation x y,size x y
        self.label_no_helmet.setStyleSheet("font: 24pt \"Ink Free\";\n""color: rgb(255, 255, 255);")
        self.label_no_helmet.setObjectName("label_no_helmet")

        self.label_Accuracy_percent = QtWidgets.QLabel(self.widget)
        self.label_Accuracy_percent.setGeometry(QtCore.QRect(220, 800, 501, 51)) #set lacation x y,size x y
        self.label_Accuracy_percent.setStyleSheet("font: 24pt \"Ink Free\";\n""color: rgb(255, 255, 255);")
        self.label_Accuracy_percent.setObjectName("label_Accuracy_percent")
        self.label_Accuracy_percent.setText("Accuracy percent  ?  %")

        self.widget_button = QtWidgets.QWidget(self.centralwidget)
        self.widget_button.setGeometry(QtCore.QRect(25, 860, 1280, 121)) #set lacation x y,size x y
        self.widget_button.setStyleSheet("background-color:rgb(24, 28, 31);\n""  border-radius: 10px;")
        self.widget_button.setObjectName("widget_button")

        self.stop_video = QtWidgets.QPushButton(self.widget_button)
        self.stop_video.setGeometry(QtCore.QRect(670, 30, 193, 63))  #set lacation x y,size x y
        self.stop_video.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.stop_video.setStyleSheet("width:500px;\n""color: rgb(255, 0, 0);\n""height:500px;\n""border-ridge:40px;\n""font: 15pt \"Ink Free\";\n""  border-radius: 5px;\n""background-color: rgb(54, 66, 71);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icon/stop_squared_filled_100px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stop_video.setIcon(icon1)
        self.stop_video.setIconSize(QtCore.QSize(40, 50))
        self.stop_video.setObjectName("stop_video")
        self.stop_video.setEnabled(False)
       # self.stop_video.clicked.connect(self.Lable_PressEvent)
       
        self.play_video = QtWidgets.QPushButton(self.widget_button)
        self.play_video.setGeometry(QtCore.QRect(470, 30, 194, 63)) #set lacation x y,size x y
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
        self.open_file_video.setGeometry(QtCore.QRect(270, 30, 194, 63))#set lacation x y,size x y
        self.open_file_video.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.open_file_video.setStyleSheet("width:500px;\n""color: rgb(255, 255, 255);\n""height:500px;\n""border-ridge:40px;\n""font: 15pt \"Ink Free\";\n""background-color: rgb(54, 66, 71);")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icon/opened_folder_filled_100px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.open_file_video.setIcon(icon3)
        self.open_file_video.setIconSize(QtCore.QSize(40, 50))
        self.open_file_video.setObjectName("open_file_video")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1870, 20, 30, 30))#set lacation x y,size x y
        self.pushButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icon/close_window_filled_30px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon4)
        self.pushButton.setIconSize(QtCore.QSize(30, 30))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.on_product_clicked)


        self.pushButton_minimize = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_minimize.setGeometry(QtCore.QRect(1840, 20, 30, 30))#set lacation x y,size x y
        self.pushButton_minimize.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icon/minimize_window_filled_30px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_minimize.setIcon(icon5)
        self.pushButton_minimize.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_minimize.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_minimize.setObjectName("pushButton")
        self.pushButton_minimize.clicked.connect(self.pushButton_Minimize)



        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(90, 10, 261, 51))#set lacation x y,size x y
        self.label_title.setStyleSheet("font: 24pt \"Ink Free\";\n""background-color: rgb(30, 35, 38);\n""color: rgb(255, 255, 255);")
        self.label_title.setObjectName("label_title")
        self.label_icon_title = QtWidgets.QLabel(self.centralwidget)
        self.label_icon_title.setGeometry(QtCore.QRect(20, 10, 50, 50))#set lacation x y,size x y
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
        #QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def ThardStart(self):
        self.thardclass = Thread()
        self.thardclass.changePixmap.connect(self.setImage)
        self.thardclass.start()
       
    def Lable_PressEvent(self):
        sys.exit()
    def on_product_clicked(self):
        sys.exit()
    def pushButton_Minimize(self):
        print("MMMMM")


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

class Thread(QtCore.QThread):
    changePixmap = QtCore.pyqtSignal(QtGui.QImage)
    sendIMG =  QtCore.pyqtSignal(QtGui.QImage)
    def __init__(self,PATH='01.mp4',parent=None):
        super(Thread,self).__init__(parent)

        self.flag = False
 
    def run(self):
        self.flag = True
        self.play()
        

    def stop(self):
        self.flag = False

    def on(self):
        global file
        self.o = Prog()
        file= self.o.openFileNameDialog()
   
    def play(self):
        prog = Prog()
        self.cap1 = cv2.VideoCapture(file) 
        self.bike_cascade = cv2.CascadeClassifier('cascade/bike_cascade.xml')
        self.i=0
        star = 0
        while self.flag:
                
                    ret, frame = self.cap1.read()
                    if ret == True:
                        Frame=cv2.resize(frame, (1280, 720)) 
                        gray = cv2.cvtColor(Frame, cv2.COLOR_BGR2GRAY)
                
                        bike = self.bike_cascade.detectMultiScale(gray,1.5,8)
                        self.cu =0
                        for (x,y,w,h) in bike:
                        
                            x1=x-100
                            y1=y-100
                            self.cu=1
                            if(w>160):
                                self.i+=1
                                cv2.rectangle(Frame,(x-100,y-100),(x+w+50,y+h+50),(255,0,0),4)
                                if (self.i==4 ) :
                                    cv2.imwrite("imgDetection/img2.jpg",Frame[y1:y+h+50,x1:x+w+50])
                                    prog.show_i()                                 
                                    RGB_img=cv2.cvtColor(Frame[y1:y+h+50,x1:x+w+50], cv2.COLOR_BGR2RGB)
                                    Cvt2qt = QtGui.QImage(RGB_img.data, RGB_img.shape[1], RGB_img.shape[0], QtGui.QImage.Format_RGB888) 
                                    self.sendIMG.emit(Cvt2qt)
                                    
                        if((self.cu==0)or(self.i>10)):
                            self.i=0
                        #print(self.cu)
                        rgb_image = cv2.cvtColor(Frame, cv2.COLOR_BGR2RGB)
                        cvt2qt = QtGui.QImage(rgb_image.data, rgb_image.shape[1], rgb_image.shape[0], QtGui.QImage.Format_RGB888)                                 
                        self.changePixmap.emit(cvt2qt)   
                        if cv2.waitKey(30) == 27 :                     
                            break
                        if  self.flag == False :  
                            self.flag =False
                            break
                            print("stop!")


        cv2.destroyAllWindows()

class Prog(QtWidgets.QMainWindow, Ui_MainWindow):
    i=0
    name =0
    
    No_helmetN = 0
    HelmetN =0
    a = [0] * 2
    Detect=[0]* 2
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.open_file_video.clicked.connect(self.On)
        self.play_video.clicked.connect(self.Start)
        self.stop_video.clicked.connect(self.Stop)
        self.play_video.setEnabled(False)
        self.th = Thread()
        self._helmet=0
        self._nohelmet=0

    def show_i(self):
        cap = cv2.imread('imgDetection/img2.jpg')
        helmet_cascade = cv2.CascadeClassifier('cascade/helmet.xml')
        no_helmet_cascade = cv2.CascadeClassifier('cascade/no_helmet.xml')
        gray = cv2.cvtColor(cap, cv2.COLOR_BGR2GRAY)
        helmet = helmet_cascade.detectMultiScale(gray,scaleFactor=2.1, minNeighbors=23, minSize=(50,50),maxSize=(55,55))
        no_helmet = no_helmet_cascade.detectMultiScale(gray,scaleFactor=1.5, minNeighbors=20 ,minSize=(50,50),maxSize=(55,55))  #ถ้าหมวกไม่แม่นให้ ให้ใช้ตัวล่าง
        #no_helmet = no_helmet_cascade.detectMultiScale(gray,scaleFactor=1.5, minNeighbors=10 ,minSize=(50,50),maxSize=(55,55))
        coun_helmet =0
        coun_no_helmet=0
        self.Detect[1]+=1
        for (x,y,w,h) in helmet:
            cv2.rectangle(cap,(x,y),(x+w,y+h),(0,255,0),2)
            coun_helmet +=1
        for (x,y,w,h) in no_helmet:
            cv2.rectangle(cap,(x,y),(x+w,y+h),(0,0,255),2)
            coun_no_helmet +=1
        cv2.imwrite("imgDetection/show.jpg",cap)
        
        if (coun_helmet>0 ) :
            r=randint(11111,9999999)
            cv2.imwrite("data/helmet/helmet-"+str(r)+".jpg",cap)
            self.count_Helmet(coun_helmet)
            
        if (coun_no_helmet>0):
            r=randint(11111,9999999)
            cv2.imwrite("data/no-helmet/no-helmet-"+str(r)+".jpg",cap)
            self.count_noHelmet(coun_no_helmet)
            
        if (coun_helmet==0 and coun_no_helmet==0) :
            r=randint(11111,9999999)
            cv2.imwrite("data/unknown1/unknown-"+str(r)+".jpg",cap)
            self.Detect[0]+=1

    def count_Helmet(self,h):
        self.HelmetN += h
        print('helmet : '+str(self.HelmetN))
        self.a[0]= self.HelmetN

    def count_noHelmet(self,n):
        self.No_helmetN += n
        print('no helmet : '+str(self.No_helmetN))
        self.a[1]=self.No_helmetN
    def Start(self):


        self.a[0]=0
        self.Detect[0]=0
        self.a[1]=0
        self.Detect[1]=0
        self.th.changePixmap.connect(self.setImage)
        self.th.sendIMG.connect(self.setShow)

        self.play_video.setEnabled(False)
        self.stop_video.setEnabled(True)
        self.stop_video.setStyleSheet("width:500px;\n""color: rgb(255, 255, 255);\n""height:500px;\n""border-ridge:40px;\n""font: 15pt \"Ink Free\";\n""  border-radius: 5px;\n""background-color: rgb(54, 66, 71);")
        self.play_video.setStyleSheet("width:500px;\n""\n""font: 15pt \"Ink Free\";\n""color: rgb(255, 0, 0);\n""height:500px;\n""border-ridge:40px;\n""background-color: rgb(54, 66, 71);\n""")
        self.th.start()

    def Stop(self):
        print("stop...")
        self.th.stop()
        self.play_video.setEnabled(True)
        self.stop_video.setEnabled(False)
        self.play_video.setStyleSheet("width:500px;\n""\n""font: 15pt \"Ink Free\";\n""color: rgb(255, 255, 255);\n""height:500px;\n""border-ridge:40px;\n""background-color: rgb(54, 66, 71);\n""")
        self.stop_video.setStyleSheet("width:500px;\n""color: rgb(255, 0, 0);\n""height:500px;\n""border-ridge:40px;\n""font: 15pt \"Ink Free\";\n""  border-radius: 5px;\n""background-color: rgb(54, 66, 71);")
    def On(self):
        self.play_video.setEnabled(True)
        self.play_video.setStyleSheet("width:500px;\n""\n""font: 15pt \"Ink Free\";\n""color: rgb(255, 255, 255);\n""height:500px;\n""border-ridge:40px;\n""background-color: rgb(54, 66, 71);\n""") 
        self.th.on()


    def openFileNameDialog(self):
        
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self,"Video", "","All Files (*);;Video Files (*.mp4)", options=options)

        return fileName

    @QtCore.pyqtSlot(QtGui.QImage) 
    def setImage(self, image):
       
        self.Video.setPixmap(QtGui.QPixmap.fromImage(image))

    def setShow(self,img):

        script_dir = path.dirname(path.realpath(__file__))
        img_filepath = path.join(script_dir,'imgDetection','show.jpg')
        img_filepath = path.abspath(img_filepath)
        px = QtGui.QPixmap(img_filepath)
        pixmap = px.scaled(313, 383)
        self.IMG_show.setPixmap(pixmap)
        print("มีหวมก = "+str(self.a[0]))
        print("ไม่มีหมวก = "+str(self.a[1]))
        print("ทั้งหมดที่ตรวจเจอ = "+str(self.Detect[1]))

        self.label_helmet.setText("With helmet : "+str(self.a[0]))
        self.label_no_helmet.setText("No helmet : "+str(self.a[1]))
        
        value =0
        
        sub = self.a[0]+self.a[1]
        div =sub/self.Detect[1]
        mul =div*100
        print(' มี + ไม่มี = '+str(sub))
        print(' หาร  = '+str(div))
        print(' คูน  = '+str(mul))

        self.label_Accuracy_percent.setText("Accuracy percent  "+str(int(mul))+" %")

    def closeEvent(self, event):
        self.th.stop()
        self.th.wait()
        super().closeEvent(event)
class data:
    HHH =1
    NHH =1

if __name__=='__main__':
    Program =  QtWidgets.QApplication(sys.argv)
    MyProg = Prog()
    MyProg.show()
    sys.exit(Program.exec_())
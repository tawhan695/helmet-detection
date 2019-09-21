import cv2
import os
import time
from random import *
# Load the cascade
#face_cascade = cv2.CascadeClassifier('cascade.xml')
#cap1 = cv2.imread('imgDetection/img2.jpg') 

# Read the input image

# Convert into grayscale
path ='C:/Users/tawhan/Desktop/helmet-detection/imgData'  

# Draw rectangle around the faces
imagePaths = [os.path.join(path,f) for f in os.listdir(path)]
#print(imagePaths)

helmet_cascade = cv2.CascadeClassifier('cascade/helmet7_cascade.xml')
no_helmet_cascade = cv2.CascadeClassifier('cascade/test3_cascade.xml')
    #no_helmet_cascade = cv2.CascadeClassifier('cascade/no_helmet_4_cascade.xml')
m=0
m2=0
for imagePath in imagePaths:
    base=os.path.basename(imagePath)
    BASE=os.path.splitext(base)[0]

    img = cv2.imread(imagePath) 
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Detect faces
    helmet = helmet_cascade.detectMultiScale(gray,1.5,3)#,1.2,10
    no_helmet = no_helmet_cascade.detectMultiScale(gray,1.1,3)#,1.2,10
    #no_Helmet = no_helmet_cascade.detectMultiScale(gray,1.3,60)
    # gray,1.03,3) = 242
    #(gray,1.1,3) =37
    #(gray,1.03,5) =35
    c=0
    i=0
    n=0
    #m+=1

    c2=0
    i2=0
    n2=0
    #m2+=1
    for (x, y, w, h) in helmet:
        cv2.rectangle(gray, (x, y), (x+w, y+h), (255, 255, 255), 1)
        c=c+1
        x1 = randint(1,9999999) 
        cv2.imwrite('helmet'+str(x1)+".png",gray[y:y+h,x:x+w])#37
        cv2.imshow('show2',gray[y:y+h,x:x+w])
        #cv2.imwrite("/data/helmet/"+str(x1)+".jpg",gray[y:y+h,x:x+w])#37
        m+=1
        #i+=1
    for (x, y, w, h) in no_helmet:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
        c2+=1
        x12 = randint(1,9999999) 
        cv2.imwrite("no-helmet/1"+str(x12)+".jpg",gray[y:y+h,x:x+w])#37
        cv2.imshow('show3',gray[y:y+h,x:x+w])
        m2+=1

    if(c==0):
        x1 = randint(100,9999999) 
        cv2.imwrite("unknown1/1"+str(BASE)+".jpg",gray)#751
        cv2.imshow('show4',gray)
    if(c2==0):
        x1 = randint(100,9999999) 
        cv2.imwrite("unknown2/1"+str(BASE)+".jpg",gray)#751
        cv2.imshow('show5',gray)
    
    print(BASE)

    #cv2.imshow('show',gray)
    # print(m)        
    cv2.waitKey(30)
    #time.sleep(1)
    cv2.destroyAllWindows()
print("มีหมวก =")  
print(m)  
print("ไม่มีหมวก =")  
print(m2) 
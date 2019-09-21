  
import cv2
import os
# Load the cascade
#face_cascade = cv2.CascadeClassifier('cascade.xml')
#cap1 = cv2.imread('imgDetection/img2.jpg') 
helmet_cascade = cv2.CascadeClassifier('cascade/helmet7_cascade.xml')
# Read the input image
img = cv2.imread('imgDetection/img34.jpg') 
# Convert into grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Detect faces
helmet = helmet_cascade.detectMultiScale(gray,1.3,10)
# Draw rectangle around the faces

path ='C:/Users/tawhan/Desktop/traner/all'
imagePaths = [os.path.join(path,f) for f in os.listdir(path)]

for imagePath in imagePaths:

    c=0
    for (x, y, w, h) in helmet:
        cv2.rectangle(gray, (x, y), (x+w, y+h), (0, 0, 255), 2)
        c+=1
        x = randint(100,9999999) 
        cv2.imwrite("C:/Users/tawhan/Desktop/traner/p/N"+str(x)+".jpg",gray[y:y+h,x:x+w])

    print(c)
    if c==0:
        x = randint(100,9999999) 
        cv2.imwrite("C:/Users/tawhan/Desktop/traner/f/"+str(x)+".jpg",gray)#751

    #cv2.imshow('img', gray)
    cv2.waitKey(1)
    cv2.destroyAllWindows()
import cv2

# Load the cascade
#face_cascade = cv2.CascadeClassifier('cascade.xml')
#cap1 = cv2.imread('imgDetection/img2.jpg') 
helmet_cascade = cv2.CascadeClassifier('cascade/h1.xml')
# Read the input image
img = cv2.imread('imgDetection/img34.jpg') 
# Convert into grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Detect faces
helmet = helmet_cascade.detectMultiScale(gray,1.3,3)
# Draw rectangle around the faces

c=0
for (x, y, w, h) in helmet:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
    c+=1

print(c)
#gas =cv2.GaussianBlur(img,(15,15),0)
#ad=cv2.adaptiveThreshold(helmet,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,1)
# Display the output
cv2.imshow('img', img)
cv2.waitKey()
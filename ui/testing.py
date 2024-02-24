import os
import threading
from time import sleep
import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# reads image 'opencv-logo.png' as grayscale
img = cv2.imread('../resources/CONFUSED 1.jpg', 0)
faces = face_cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=10, minSize=(30, 30))
test_image = img

for (x, y, w, h) in faces:
    # Extract the face ROI (Region of Interest)
    face_roi = img[y:y + h, x:x + w]

    # Resize the face ROI to match the input shape of the model
    resized_face = cv2.resize(face_roi, (48, 48), interpolation=cv2.INTER_AREA)
    test_image = resized_face

cv2.imwrite('../resources/image2.jpg', test_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

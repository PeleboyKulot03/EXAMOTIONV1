import os
import threading
from time import sleep
import cv2
from deepface import DeepFace
import numpy as np
import time
from utils import exam_getter

# ts stores the time in seconds
ts = time.time()

emotions = []
emotion_labels = ['angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral']
model = DeepFace.build_model('Emotion')
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

path = os.getcwd() + '/images'
name = input("Type your name: ")
if not os.path.exists(path):
    os.mkdir(path)

path = os.getcwd() + f"/images/{name}"
not_destroy = True


def timer():
    global open_emotion

    while not_destroy:
        for counter in range(15):
            sleep(1)
        open_emotion = True


while True:
    if not os.path.exists(path):
        os.mkdir(path)
        break
    else:
        name = input("Name already in use, please use other name: ")
        path = os.getcwd() + f"/{name}"

# define a video capture object
vid = cv2.VideoCapture(0)

open_emotion = True

threading.Thread(target=timer, args=()).start()
while True:
    _, frame = vid.read()
    frame = cv2.flip(frame, 1)

    # Convert frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=10, minSize=(30, 30))

    for (x, y, w, h) in faces:
        # Extract the face ROI (Region of Interest)
        face_roi = gray_frame[y:y + h, x:x + w]

        # Resize the face ROI to match the input shape of the model
        resized_face = cv2.resize(face_roi, (48, 48), interpolation=cv2.INTER_AREA)

        # Preprocess the image for DEEPFACE
        normalized_face = resized_face / 255.0
        reshaped_face = normalized_face.reshape(1, 48, 48, 1)

        # Predict emotions using the pre-trained model
        preds = model.predict(reshaped_face)
        emotion_idx = np.argmax(preds)
        emotion = emotion_labels[emotion_idx]

        # Draw rectangle around face and label with predicted emotion
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        if emotion == "sad":
            emotion = "Bored"
        elif emotion == "angry":
            emotion = "Frustrated"
        elif emotion == "happy":
            emotion = "Excited"
        elif emotion == "disgust":
            continue
        elif emotion == "neutral":
            emotion = "Neutral"
        elif emotion == "fear":
            emotion = "Nervous"
        elif emotion == "surprise":
            emotion = "Surprised"

        cv2.putText(frame, emotion, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

        if open_emotion and emotion != '':
            emotions.append(emotion)
            ts = time.time()
            cv2.imwrite(f"{path}/{ts}.jpg", frame)
            open_emotion = False
            print("hi")
            break

    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        not_destroy = False
        break


exam_getter.Traditional().add_data(
    dict(name=name, emotions=emotions)
)

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()

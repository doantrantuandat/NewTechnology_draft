import os
import cv2
import numpy as np
from PIL import Image
import pickle

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(BASE_DIR, "images")

face_cascade = cv2.CascadeClassifier('cascades/haarcascade_frontalface_alt2.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()


current_id = 0
labels_id = {}
y_labels = []
x_train = []

for root, dirs, files in os.walk(image_dir):
    for file in files:
        if file.endswith("png") or file.endswith("jpg"):
            path = os.path.join(root, file)
            label = os.path.basename(root).replace(" ", "-").lower()
           
            #print(path)
            if not label in labels_id:
                labels_id[label] = current_id
                current_id += 1
            id_ = labels_id[label]
            #print(labels_id)
            pil_image = Image.open(path).convert("L")
            image_array = np.array(pil_image, "uint8")
            #print(image_array)

            faces = face_cascade.detectMultiScale(image_array, 1.1, 4)
            for (x, y, w, h) in faces:
                roi = image_array[y:y+h, x:x+w]
                x_train.append(roi)
                y_labels.append(id_)

#print(x_train)
#print(y_labels)

with open("labels.pickle", "wb") as f:
    pickle.dump(labels_id, f)

recognizer.train(x_train, np.array(y_labels))
recognizer.save("trainer.yml")

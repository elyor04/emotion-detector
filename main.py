import cv2 as cv
import numpy as np
from keras import models
from random import randint
from typing import Iterable
from os import listdir
from re import findall
from time import time

colors: dict[str, tuple[int, int, int]] = dict()


def visualize_box_and_labels_on_image_array(
    image: cv.UMat,
    imgSize: Iterable[int],
    box: Iterable[int],
    labels: Iterable[str],
) -> np.ndarray:
    wd, hg = imgSize
    xmin, ymin, xmax, ymax = box
    _label = labels[0].split()[0]

    if _label in colors:
        color = colors[_label]
    else:
        color = (randint(0, 255), randint(0, 255), randint(0, 255))
        while (True not in [(pxl > 210) for pxl in color]) or (
            color in colors.values()
        ):
            color = (randint(0, 255), randint(0, 255), randint(0, 255))
        colors[_label] = color

    cv.rectangle(image, (xmin, ymin), (xmax, ymax), color, 4)

    for i, label in enumerate(labels):
        gts = cv.getTextSize(label, cv.FONT_HERSHEY_COMPLEX_SMALL, 2.5, 2)
        gtx = gts[0][0] + xmin
        gty = (gts[0][1] * (i + 1)) + ymin + (i * 12)

        x1, x2 = max(xmin - 2, 0), min(gtx + 2, wd)
        y1, y2 = min((gts[0][1] * i) + ymin + (i * 12), hg), min(gty + 12, hg)
        pts = np.array([[x1, y1], [x2, y1], [x2, y2], [x1, y2]], np.int32)

        cv.drawContours(image, [pts], -1, color, -1)
        cv.putText(
            image, label, (xmin, gty), cv.FONT_HERSHEY_COMPLEX_SMALL, 2.5, (0, 0, 0), 2
        )

    return image


faceCascade = cv.CascadeClassifier("data/haarcascade_frontalface_default.xml")
emotion_labels = ["Angry", "Disgust", "Fear", "Happy", "Neutral", "Sad", "Surprise"]

modelPath = findall("model_emotions[-]\d+[.]\d+[.]h5", " ".join(listdir("data")))
if not modelPath:
    print("Could not find any model in location data/")
    exit(0)

modelPath = f"data/{modelPath[0]}"
print(f"Loading model: {modelPath}")
model: models.Sequential = models.load_model(modelPath)

cam = cv.VideoCapture(0)
imgSize = (
    int(cam.get(cv.CAP_PROP_FRAME_WIDTH)),
    int(cam.get(cv.CAP_PROP_FRAME_HEIGHT)),
)

prevTime = 0
cv.ocl.setUseOpenCL(True)

while True:
    img = cv.UMat(cam.read()[1])
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        img_gray, scaleFactor=1.2, minNeighbors=4, minSize=(60, 60)
    )
    for x1, y1, wd, hg in faces:
        x2, y2 = x1 + wd, y1 + hg

        img_pred = (
            cv.resize(
                cv.UMat(img_gray, [y1, y2], [x1, x2]),
                (48, 48),
                interpolation=cv.INTER_AREA,
            ).get()
            / 255.0
        )
        result = list(model.predict(img_pred.reshape(1, 48, 48, 1))[0])

        emotions = zip(emotion_labels, [int(x * 100) for x in result])
        emotions = sorted(emotions, key=(lambda x: x[1]), reverse=True)
        emotions = [f"{x} {y}%" for x, y in emotions]

        visualize_box_and_labels_on_image_array(
            img, imgSize, (x1, y1, x2, y2), emotions
        )

    currTime = time()
    fps = int(1 / (currTime - prevTime))
    prevTime = currTime

    cv.putText(img, f"FPS: {fps}", (5, 30), cv.FONT_HERSHEY_COMPLEX, 1.0, (250, 0, 0), 2)
    cv.imshow("Emotions Detector", img)

    if cv.waitKey(2) == 27:
        break

cam.release()
cv.destroyAllWindows()

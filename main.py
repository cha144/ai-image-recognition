from ultralytics import YOLO
import pyautogui
from pynput.keyboard import Listener, Key
from PIL import ImageGrab
import time
import os
import keyboard
import pyttsx3

# file must always start with 1
imgIndex = 0
model = YOLO("yolov8n.pt")  # load a pretrained model (recommended for training)
imgSaved = False

# establish tts model
tts_engine = pyttsx3.init()
tts_engine.setProperty('voice', 'com.apple.speech.synthesis.voice.Alex')
tts_engine.setProperty('rate', 150)

tts_engine.say("Press space with your mouse on an image to get started.")
tts_engine.runAndWait()

# current database of items
itemList = {0: 'person', 1: 'bicycle', 2: 'car', 3: 'motorcycle', 4: 'airplane', 5: 'bus', 6: 'train', 7: 'truck',
            8: 'boat', 9: 'traffic light', 10: 'fire hydrant', 11: 'stop sign', 12: 'parking meter', 13: 'bench',
            14: 'bird', 15: 'cat', 16: 'dog', 17: 'horse', 18: 'sheep', 19: 'cow', 20: 'elephant', 21: 'bear',
            22: 'zebra', 23: 'giraffe', 24: 'backpack', 25: 'umbrella', 26: 'handbag', 27: 'tie', 28: 'suitcase',
            29: 'frisbee', 30: 'skis', 31: 'snowboard', 32: 'sports ball', 33: 'kite', 34: 'baseball bat',
            35: 'baseball glove', 36: 'skateboard', 37: 'surfboard', 38: 'tennis racket', 39: 'bottle',
            40: 'wine glass', 41: 'cup', 42: 'fork', 43: 'knife', 44: 'spoon', 45: 'bowl', 46: 'banana', 47: 'apple',
            48: 'sandwich', 49: 'orange', 50: 'broccoli', 51: 'carrot', 52: 'hot dog', 53: 'pizza', 54: 'donut',
            55: 'cake', 56: 'chair', 57: 'couch', 58: 'potted plant', 59: 'bed', 60: 'dining table', 61: 'toilet',
            62: 'tv', 63: 'laptop', 64: 'mouse', 65: 'remote', 66: 'keyboard', 67: 'cell phone', 68: 'microwave',
            69: 'oven', 70: 'toaster', 71: 'sink', 72: 'refrigerator', 73: 'book', 74: 'clock', 75: 'vase',
            76: 'scissors', 77: 'teddy bear', 78: 'hair drier', 79: 'toothbrush'}


def on_key_press(key):
    global imgIndex
    global model
    global imgSaved
    global itemList

    if key == Key.tab:
        try:
            # gets the index of the "predicts"
            with open("predictIndex.txt", "r") as file:
                imgIndex = int(file.readline())

            print(f"Image index is {imgIndex}")
            # finds coordinates of cursor on screen
            cursorX, cursorY = pyautogui.position()
            print("Button pressed")

            # establishes the screenshot region
            ss_region = (cursorX - 410, cursorY - 355, cursorX + 20, cursorY + 110)

            # this if statement is to ensure that this is only ran once every run of the program
            if not imgSaved:
                ss_img = pyautogui.screenshot(region=ss_region)

                results = model.predict(ss_img, project="runs", show=True, save=True, save_conf=True,
                                    save_txt=True)  # predict on an image

                # if imgIndex == 1, this is the first prediction
                if imgIndex == 1:
                    with open("runs/predict/labels/image0.txt", "r") as prediction:
                        firstLine = prediction.readline()
                        objectId = firstLine[:2]
                        print(objectId)
                        objectName = itemList[int(objectId)]

                        # writes the imgIndex but added once
                        with open('predictIndex.txt', 'w') as file:
                            file.write(str(imgIndex + 1))
                            print("Index written to file:", imgIndex)

                        tts_engine.say(f"The objects in your specified region is a {objectName}")
                        tts_engine.runAndWait()

                        imgIndex = imgIndex + 1

                # every other prediction after the first one, known from imgIndex
                else:
                    with open(f"runs/predict{imgIndex}/labels/image0.txt", "r") as prediction:
                        firstLine = prediction.readline()
                        objectId = firstLine[:2]
                        objectName = itemList[int(objectId)]

                        with open('predictIndex.txt', 'w') as file:
                            file.write(str(imgIndex + 1))
                            print("Index written to file:", imgIndex)

                        tts_engine.say(f"The objects in your specified region is a {objectName}")
                        tts_engine.runAndWait()

                imgSaved = True

        # checks if AI model does not detect an object, which then will say a message
        except FileNotFoundError:
            print("No object detected in database")

            with open('predictIndex.txt', 'w') as file:
                file.write(str(imgIndex + 1))
                print("Index written to file:", imgIndex)

            imgIndex = imgIndex + 1
            tts_engine.say("No object detected in database.")
            tts_engine.runAndWait()


def on_key_release(key):
    print("Button released")


# includes a listener that looks for any key pressed
with Listener(on_press=on_key_press, on_release=on_key_release) as listener:
    listener.join()

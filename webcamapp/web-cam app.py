import cv2
import random
import time

imgcapture = cv2.VideoCapture(0)
result = True

while (result):
    name = int(round(time.time()) * 1000)
    name = '{}.png'.format(name)
    ret, frame = imgcapture.read()
    cv2.imwrite(name, frame)
    result = False
    print("image captured.")

imgcapture.release()

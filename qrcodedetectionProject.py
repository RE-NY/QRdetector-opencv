import cv2
import numpy as np
import time
from pyzbar.pyzbar import decode

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
while True:
    success, img = cap.read()
    for barcode in decode(img):
        data = barcode.data.decode("utf-8")
        poly_pts = np.array(barcode.polygon, np.int32)
        rect_pts = barcode.rect
        cv2.polylines(img, [poly_pts], True, (0, 0, 255), 5)
        cv2.putText(img, data, (rect_pts[2], rect_pts[1]), cv2.FONT_HERSHEY_DUPLEX,
                    0.9, (0, 255, 0), 2)
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'): # stops live video by pressing the key "q"
        break
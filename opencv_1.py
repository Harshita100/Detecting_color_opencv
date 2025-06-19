import cv2
from color_req import limits_color
from PIL import Image

cam = cv2.VideoCapture(0)
red = [0,255,255]

while True:
    rect, frame = cam.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    ll,ul = limits_color(color = red)

    mask = cv2.inRange(hsv, ll,ul)

    mask_ =Image.fromarray(mask)
    boxs = mask_.getbbox()

    if boxs is not None:
        x1,y1,x2,y2 = boxs
        frame = cv2.rectangle(frame, (x1,y1), (x2,y2), (0,255,0),5)

    cv2.imshow('f', frame)


    if cv2.waitKey(1) & 0xFF == ord('d'):
        break
cam.release()

cv2.destroyAllWindows()
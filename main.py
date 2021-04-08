import cv2
import winsound
cam = cv2.VideoCapture(0)                           #0 for single 1 for multiple cam. call
while cam.isOpened():                               #for calling cam
    ret, frame1 = cam.read()
    ret, frame2 = cam.read()
    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilates = cv2.dilate(thresh, None, iterations=3)
    contours, _= cv2.findContours(dilates, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)
    for c in contours:
        if cv2.contourArea(c) < 5000:
            continue
        x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(frame1, (x,y), (x+w, y+h), (0, 255, 0), 2)
        winsound.Beep(200, 400)
    if cv2.waitKey(10) == ord('q'):                 #saving my cam from crashes or error
        break
    cv2.imshow('rtsp trial', frame1)
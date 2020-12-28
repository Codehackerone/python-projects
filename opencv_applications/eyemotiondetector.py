import cv2

eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")

video = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX
while True:
    check, frame = video.read()
    frame_img = frame
    gray_img = cv2.cvtColor(frame_img, cv2.COLOR_BGR2GRAY)
    eyes = eye_cascade.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=5)
    for x, y, w, h in eyes:
        frame_img = cv2.rectangle(frame_img, (x, y), (x + w, y + h), (0, 255, 0), 3)
        cv2.putText(frame_img, 'eye', (x, y-10), font, 1, (0, 255, 0), 2, cv2.LINE_4)
    cv2.imshow("Capturing...", frame_img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()

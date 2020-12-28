import cv2

phone_cascade = cv2.CascadeClassifier("phone_cascade.xml")

video = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX
while True:
    check, frame = video.read()
    frame_img = frame
    gray_img = cv2.cvtColor(frame_img, cv2.COLOR_BGR2GRAY)
    faces = phone_cascade.detectMultiScale(gray_img, scaleFactor=3, minNeighbors=9)
    for x, y, w, h in faces:
        frame_img = cv2.rectangle(frame_img, (x, y), (x + w, y + h), (0, 0, 255), 3)
        cv2.putText(frame_img, 'phone', (x, y-10), font, 1, (0, 0, 255), 2, cv2.LINE_4)
    cv2.imshow("Capturing...", frame_img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()

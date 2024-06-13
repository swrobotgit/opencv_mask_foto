import cv2
import mediapipe as mp
import numpy as np
import threading as th

mp_drawing = mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic
cap = cv2.VideoCapture(0)
holistic = mp_holistic.Holistic(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

size_img = (100, 100)
yarik = cv2.imread('yar777.png', cv2.IMREAD_UNCHANGED)
makaka = cv2.imread('MakakaYarik.png', cv2.IMREAD_UNCHANGED)
shrek = cv2.imread('output-onlinepngtools.png', cv2.IMREAD_UNCHANGED)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("плоха дела начаника, камира выключится")
        break

    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = holistic.process(image)

    if results.pose_landmarks:
        nos = results.pose_landmarks.landmark[mp_holistic.PoseLandmark.NOSE]
        LEAR = results.pose_landmarks.landmark[mp_holistic.PoseLandmark.LEFT_EAR]
        REAR = results.pose_landmarks.landmark[mp_holistic.PoseLandmark.RIGHT_EAR]
        height, width, _ = frame.shape
        lex = LEAR.x * width
        ley = LEAR.y * height
        rex = REAR.x * width
        rey = REAR.y * height


        x = int(nos.x * width)
        y = int(nos.y * height)
        try:
            with open("who.txt", "r") as w:
                line = w.readlines()
                w.close()
            line = line[-1]
            line = line.split("+")
            dl = lex-rex+int(line[1])
            if line[0] == "yarik":
                nos_img = yarik
            if line[0] == "makaka":
                nos_img = makaka
            if line[0] == "shrek":
                nos_img = shrek
            if 0 < x < width and 0 < y < height:
                img_nose = cv2.resize(nos_img, (int(dl), int(dl)))
                b, g, r, a = cv2.split(img_nose)
                img_bgr = cv2.merge((b, g, r))
                x_offset = x - size_img[0] // 2
                y_offset = y - size_img[1] // 2
                roi = frame[y_offset-20:y_offset-20+int(dl), x_offset-25:x_offset-25+int(dl)]
                if x_offset + int(dl) < width and y_offset + int(dl) < height and x_offset - int(dl) < width and y_offset - int(dl) < width:
                    for c in range(3):
                        roi[:, :, c] = a / 255.0 * img_nose[:, :, c] + (1 - a / 255.0) * roi[:, :, c]

                cv2.imshow('Eshkere Shrek', frame)
            else:
                cv2.imshow('Eshkere Shrek', frame)
        except Exception as e:
            print(e)
            cv2.imshow('Eshkere Shrek', frame)


    if cv2.waitKey(1) & 0xFF == ord('e'):
        break

cap.release()
cv2.destroyAllWindows()

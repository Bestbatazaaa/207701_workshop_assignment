#This code demonstrate how to show location of hand landmark
import cv2
import mediapipe as mp

Nfing = 0
cap = cv2.VideoCapture(0)

#Call hand pipe line module
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    #print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                if id == 4:
                    id4 = int(id)
                    cx4 = cx
                if id == 3:
                    id3 = int(id)
                    cx3 = cx
                if id == 8:
                    id8 = int(id)
                    cx8 = cx
                if id == 5:
                    id5 = int(id)
                    cx5 = cx
                if id == 12:
                    id12 = int(id)
                    cx12 = cx
                if id == 9:
                    id9 = int(id)
                    cx9 = cx
            if cx4 > cx3:
                Nfing = 4
                if cx8 > cx5:
                    Nfing = 3
                    if cx12 > cx9:
                        Nfing = 2

            else:
                Nfing = 5

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cv2.putText(img, str(int(Nfing)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 255), 3)
    cv2.putText(img, str(str("Best")), (500, 450), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 255), 3)
    cv2.imshow("Image", img)
    cv2.waitKey(1)
#Closeing all open windows
#cv2.destroyAllWindows()
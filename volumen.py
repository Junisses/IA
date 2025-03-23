import cv2
import mediapipe as mp
from math import hypot
import subprocess
import time
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from comtypes import CLSCTX_ALL
import numpy as np

mpHands = mp.solutions.hands
hands = mpHands.Hands(
    static_image_mode=False,
    model_complexity=1,
    min_detection_confidence=0.75,
    min_tracking_confidence=0.75,
    max_num_hands=1
)
Draw = mp.solutions.drawing_utils

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)

vol_range = volume.GetVolumeRange() 
min_vol, max_vol = vol_range[0], vol_range[1]

hand_opened = False

def open_edge():
    subprocess.run(["start", "msedge", "--new-window", "https://www.google.com", "--window-size=800,600"], shell=True)

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    Process = hands.process(frameRGB)

    landmarkList = []
    if Process.multi_hand_landmarks:
        for handlm in Process.multi_hand_landmarks:
            for _id, landmarks in enumerate(handlm.landmark):
                height, width, color_channels = frame.shape
                x, y = int(landmarks.x * width), int(landmarks.y * height)
                landmarkList.append([_id, x, y])
            Draw.draw_landmarks(frame, handlm, mpHands.HAND_CONNECTIONS)

    if landmarkList != []:
        x_1, y_1 = landmarkList[4][1], landmarkList[4][2]
        x_2, y_2 = landmarkList[8][1], landmarkList[8][2] 
        cv2.circle(frame, (x_1, y_1), 7, (0, 255, 0), cv2.FILLED)
        cv2.circle(frame, (x_2, y_2), 7, (0, 255, 0), cv2.FILLED)
        cv2.line(frame, (x_1, y_1), (x_2, y_2), (0, 255, 0), 3)

        L = hypot(x_2 - x_1, y_2 - y_1)

        vol_level = np.interp(L, [30, 150], [min_vol, max_vol]) 
        vol_level = np.clip(vol_level, min_vol, max_vol)
        volume.SetMasterVolumeLevel(vol_level, None)

        if len(landmarkList) >= 21:
            thumb_dist = hypot(landmarkList[4][1] - landmarkList[0][1], landmarkList[4][2] - landmarkList[0][2])
            index_dist = hypot(landmarkList[8][1] - landmarkList[5][1], landmarkList[8][2] - landmarkList[5][2])
            middle_dist = hypot(landmarkList[12][1] - landmarkList[9][1], landmarkList[12][2] - landmarkList[9][2])
            ring_dist = hypot(landmarkList[16][1] - landmarkList[13][1], landmarkList[16][2] - landmarkList[13][2])
            pinky_dist = hypot(landmarkList[20][1] - landmarkList[17][1], landmarkList[20][2] - landmarkList[17][2])

            if thumb_dist > 100 and index_dist > 100 and middle_dist > 100 and ring_dist > 100 and pinky_dist > 100:
                if not hand_opened: 
                    open_edge() 
                    hand_opened = True 

        if hand_opened:
            time.sleep(1)
            hand_opened = False

    cv2.imshow('Control de Gestos', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

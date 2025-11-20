import cv2 as cv
import mediapipe as mp
class OM:
    def __init__(s):
        s.mpd = mp.solutions.drawing_utils
        s.mph = mp.solutions.hands


    def draw(s, frm, lms, g_name):
        h, w, c = frm.shape
        if lms:
            s.mpd.draw_landmarks(frm, lms, s.mph.HAND_CONNECTIONS)
            wrist_x = int(lms.landmark[0].x * w)
            wrist_y = int(lms.landmark[0].y * h)
            
            

            cv.putText(frm, 
                       g_name, 
                       (wrist_x - 50, wrist_y - 50), 
                       cv.FONT_HERSHEY_SIMPLEX, 
                       1, 
                       (255, 0, 0), 
                       2, 
                       cv.LINE_AA)
        if not lms:
             cv.putText(frm, 
                       g_name, 
                       (50, 50), 
                       cv.FONT_HERSHEY_SIMPLEX, 
                       1, 
                       (0, 0, 255), 
                       2, 
                       cv.LINE_AA)
        cv.imshow('Gesture Recognition System', frm)
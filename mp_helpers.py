import cv2
import numpy as np

# We follow the outlined framework provided by MediaPipe https://developers.google.com/mediapipe, for detection, pre prcocessing and frame reading
# All functions are taken from MediaPipe in this file
def detect(image, model):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) 
    image.flags.writeable = False                  
    results = model.process(image)                 
    image.flags.writeable = True                   
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR) 
    return image, results

def landmark_draw(image,results,drawing,holistic):
    drawing.draw_landmarks(image,results.pose_landmarks,holistic.POSE_CONNECTIONS)

def get_landmarks(res):
    #pose landmarks
    if res.pose_landmarks:
        p_landmarks = []
        p_x_y_z = []
        for x in res.pose_landmarks.landmark:
            l = np.array([x.x,x.y,x.z,x.visibility])
             
            p_x_y_z.append([x.x,x.y,x.z])
                             
            p_landmarks.append(l)
        p_landmarks = np.array(p_landmarks).flatten()
    else:
        p_x_y_z = np.zeros((33, 3))
        p_landmarks = np.zeros(132)
        
    #left hand
    if res.left_hand_landmarks:
        l_landmarks = []
        for x in res.left_hand_landmarks.landmark:
            l = np.array([x.x,x.y,x.z])
            l_landmarks.append(l)
        l_landmarks = np.array(l_landmarks).flatten()
    else:
        l_landmarks = np.zeros(21*3)
        
    #right hand
    if res.right_hand_landmarks:
        r_landmarks = []
        for x in res.right_hand_landmarks.landmark:
            l = np.array([x.x,x.y,x.z])
            r_landmarks.append(l)
        r_landmarks = np.array(r_landmarks).flatten()
    else:
        r_landmarks = np.zeros(21*3)
        
    return np.concatenate([p_landmarks]), p_x_y_z

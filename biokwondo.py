import cv2
import mediapipe as mp
import numpy as np
import tensorflow
from tensorflow import keras
from keras.models import load_model
import feedback_generation
import mp_helpers
import pyttsx3


# We follow the outlined framework provided by MediaPipe https://developers.google.com/mediapipe, for detection, pre prcocessing and frame reading

def prob_viz(res, actions, input_frame, colors):
    output_frame = input_frame.copy()
    for num, prob in enumerate(res):
        cv2.rectangle(output_frame, (0,60+num*40), (int(prob*100), 90+num*40), colors, -1)
        cv2.putText(output_frame, action[num], (0, 85+num*40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2, cv2.LINE_AA)
        
    return output_frame

engine = pyttsx3.init() # for audio feedback

holistic = mp.solutions.holistic
drawing = mp.solutions.drawing_utils
action_model = load_model('Models/kcross_action.keras')

low_cross = load_model('Models/low_cross_model.keras')
low_hands = load_model('Models/low_hands_model.keras')

inner_cross = load_model('Models/inner_cross_model.keras')
inner_hands = load_model('Models/inner_hands_model.keras')

high_cross = load_model('Models/high_cross_model.keras')
high_hands = load_model('Models/high_hands_model.keras')

sequence_a = [] # sequence storing for the action recogntion
sequence_f = [] # sequence storing for the feedback
sentence = []
predictions = []
p_x_y_z  = []
threshold = 0.8

action = np.array(['Low Section','Inner Section','High Section','Nothing','Standing Still'])

cap = cv2.VideoCapture(0)
cv2.waitKey(100) 
frame_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
frame_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
print("Frame size ", (frame_width, frame_height))

print("Video FPS: ", cap.get(cv2.CAP_PROP_FPS))

print("testong")
with holistic.Holistic(min_detection_confidence=0.7, min_tracking_confidence=0.7) as h:
    while cap.isOpened():
        # Read feed
        ret, frame = cap.read()

        # Make detections
        image, results = mp_helpers.detect(frame, h)
       # print(results)
        
        # Draw landmarks
        mp_helpers.landmark_draw(image, results)

        # 2. Prediction logic
        keypoints, p_points = mp_helpers.get_landmarks(results)

        sequence_a.append(keypoints)
        sequence_f.append(keypoints)
        p_x_y_z.append(p_points)
        
        sequence_f = sequence_f[-60:]
        sequence_a = sequence_a[-20:]
        

        
        
        if len(sequence_f) == 60 and (sequence_f != None):
            
            #angle1,angle2, point1,point2 = test_hand(results)
            #cv2.putText(image, str(angle1), tuple(point1),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
            #cv2.putText(image, str(angle2), tuple(point2),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
           
            res = action_model.predict(np.expand_dims(sequence_a, axis=0))[0]
            predictions.append(np.argmax(res))
            image = prob_viz(res, action, image, (245,117,16))

        #3. Viz logic
            if np.unique(predictions[-1:])[0]==np.argmax(res) and (sequence_f != None): 
                if res[np.argmax(res)] > threshold: 
                    
                    ##testing stuff 
                    print(action[np.argmax(res)])
                    speak = ""
                    if action[np.argmax(res)] == action[0]: #Low Section Detected
                        speak = feedback_generation.first_feedback_model(sequence_f[:20],low_hands,speak)
                        speak = feedback_generation.second_feedback_model(sequence_f[20:40],low_cross,speak,action[0])
                        speak = feedback_generation.angle_feedback_low(results,speak)

                    if action[np.argmax(res)] == action[1]: #Inner Section Detected
                        speak = feedback_generation.first_feedback_model(sequence_f[:20],inner_hands,speak)
                        speak = feedback_generation.second_feedback_model(sequence_f[20:40],inner_cross,speak,action[1])
                        speak = feedback_generation.angle_feedback_low(results,speak)
                    
                    if action[np.argmax(res)] == action[2]: #High Section Detected
                        speak = feedback_generation.first_feedback_model(sequence_f[:20],high_hands,speak)
                        speak = feedback_generation.second_feedback_model(sequence_f[20:40],high_cross,speak,action[2])
                        speak = feedback_generation.angle_feedback_low(results,speak)
                        
                    engine.say(speak)
                    engine.runAndWait()

                    if len(sentence) > 0: 
                        if action[np.argmax(res)] != sentence[-1]:
                            sentence.append(action[np.argmax(res)])
                    else:
                        sentence.append(action[np.argmax(res)])
                    

            if len(sentence) > 5: 
                sentence = sentence[-5:]

            image = prob_viz(res, action, image, (245,117,16))

        cv2.imshow('BioKwondo', image)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

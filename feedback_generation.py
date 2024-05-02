import numpy as np


def calc_angle(x,y,z):
    x = np.array(x)
    y = np.array(y)
    z = np.array(z)
    
    radians = np.arctan2(z[1]-y[1], z[0]-y[0]) - np.arctan2(x[1]-y[1], x[0]-y[0])
    angle = np.abs(radians*180.0/np.pi)
            
    return angle 

def angle_feedback_high(result,sentence):
    #getting angle between two points to provide feedback

    #frontal plane calc
    right_elbow = [result.pose_landmarks.landmark[14].x, result.pose_landmarks.landmark[14].y]
    right_wrist = [result.pose_landmarks.landmark[16].x, result.pose_landmarks.landmark[16].y]
    right_shoulder = [result.pose_landmarks.landmark[12].x, result.pose_landmarks.landmark[12].y]
    right_hip = [result.pose_landmarks.landmark[24].x, result.pose_landmarks.landmark[24].y]
    

    #saggital plane calc
    right_elbow_s = [result.pose_landmarks.landmark[14].z, result.pose_landmarks.landmark[14].y]
    right_wrist_s = [result.pose_landmarks.landmark[16].z, result.pose_landmarks.landmark[16].y]
    right_shoulder_s = [result.pose_landmarks.landmark[12].z, result.pose_landmarks.landmark[12].y]
    right_hip_s = [result.pose_landmarks.landmark[24].z, result.pose_landmarks.landmark[24].y]


    r_elb = calc_angle(right_shoulder,right_elbow,right_wrist)
    r_hip = calc_angle(right_hip, right_shoulder, right_elbow)
    
    r_hip_s = calc_angle(right_hip_s, right_shoulder_s, right_elbow_s)


    left_elbow = [result.pose_landmarks.landmark[13].x, result.pose_landmarks.landmark[13].y]
    left_wrist = [result.pose_landmarks.landmark[15].x, result.pose_landmarks.landmark[15].y]
    left_shoulder = [result.pose_landmarks.landmark[11].x, result.pose_landmarks.landmark[11].y]
    left_hip = [result.pose_landmarks.landmark[23].x, result.pose_landmarks.landmark[23].y]
    
    left_elbow_s = [result.pose_landmarks.landmark[13].x, result.pose_landmarks.landmark[13].y]
    left_wrist_s = [result.pose_landmarks.landmark[15].x, result.pose_landmarks.landmark[15].y]
    left_shoulder_s = [result.pose_landmarks.landmark[11].x, result.pose_landmarks.landmark[11].y]
    left_hip_s = [result.pose_landmarks.landmark[23].x, result.pose_landmarks.landmark[23].y]


    l_elb = calc_angle(left_shoulder, left_elbow, left_wrist)
    l_hip = calc_angle(left_hip, left_shoulder, left_elbow)
    l_hip_s= calc_angle(left_hip_s, left_shoulder_s, left_elbow_s)

    if r_hip > 100: # means the right hand has been used to block
        
        #checking elbow bend
        angle_elb = 100 - r_elb
        if r_elb < 100: 
            sentence += "Bend your elbow slighlty more by {} degrees".format(angle_elb)
        if r_elb > 130:
            sentence += "Straighten your elbow more by {} degrees".format(-angle_elb)
        else:
            sentence += "Good straightness of the elbow"

        #checking arm posiiton in fronatal and saggital plane
        angle_f = 140-r_hip
        angle_s = 140-r_hip_s
        if r_hip < 140:
            sentence += ", also move your arm roughly {} degrees to the left".format(angle_f)
        elif r_hip > 170:
            sentence += ", also move your arm roughly {} degrees to the right its too to the left of your head".format(-angle_f)

        if r_hip_s < 140:
            sentence += ", also move your arm roughly {} degrees backwards its too in front of you".format(angle_s)
        if r_hip_s > 170:
            sentence += ", also move your arm roughly {} degrees forwards its too much behind your head".format(-angle_s)
        else:
            sentence += ", correct arm position for the high rising block"

    else: # left hand has been used to block
        angle_elb = 100 - l_elb
        if l_elb < 100:
            sentence += "Bend your elbow slighlty more by {} degrees".format(angle_elb)
        if l_elb > 130:
            sentence += "Straighten your elbow more by {} degrees".format(-angle_elb)
        else:
            sentence += "Good straightness of the elbow"

        #saggital and frontal plane check
        angle_f = 140-l_hip
        angle_s = 140-l_hip_s
        if r_hip < 140:
            sentence += ", also move your arm roughly {} degrees to the right".format(angle_f)
        elif r_hip > 170:
            sentence += ", also move your arm roughly {} degrees to the right its too to the right of your head".format(-angle_f)

        if r_hip_s < 140:
            sentence += ", also move your arm roughly {} degrees backwards its too in front of you".format(angle_s)
        if r_hip_s > 170:
            sentence += ", also move your arm roughly {} degrees forwards its too much behind your head".format(-angle_s)
        else:
            sentence += ", correct arm position for the high rising block"

    return sentence

def angle_feedback_inner(result,sentence):
    #getting angle between two points to provide feedback
    right_elbow = [result.pose_landmarks.landmark[14].z, result.pose_landmarks.landmark[14].y]
    right_wrist = [result.pose_landmarks.landmark[16].z, result.pose_landmarks.landmark[16].y]
    right_shoulder = [result.pose_landmarks.landmark[12].z, result.pose_landmarks.landmark[12].y]
    right_hip = [result.pose_landmarks.landmark[24].z, result.pose_landmarks.landmark[24].y]
    

    right_elbow_s = [result.pose_landmarks.landmark[14].z, result.pose_landmarks.landmark[14].y]
    right_wrist_s = [result.pose_landmarks.landmark[16].z, result.pose_landmarks.landmark[16].y]
    right_shoulder_s = [result.pose_landmarks.landmark[12].z, result.pose_landmarks.landmark[12].y]
    right_hip_s = [result.pose_landmarks.landmark[24].z, result.pose_landmarks.landmark[24].y]

    r_elb = calc_angle(right_shoulder,right_elbow,right_wrist)
    r_hip = calc_angle(right_hip, right_shoulder, right_elbow)
    r_hip_s = calc_angle(right_hip_s, right_shoulder_s, right_elbow_s)
    r_elb_s = calc_angle(right_shoulder_s,right_elbow_s,right_wrist_s)

    r_shoulder = calc_angle(right_elbow,right_shoulder,left_shoulder)

    left_elbow = [result.pose_landmarks.landmark[13].x, result.pose_landmarks.landmark[13].y]
    left_wrist = [result.pose_landmarks.landmark[15].x, result.pose_landmarks.landmark[15].y]
    left_shoulder = [result.pose_landmarks.landmark[11].x, result.pose_landmarks.landmark[11].y]
    left_hip = [result.pose_landmarks.landmark[23].x, result.pose_landmarks.landmark[23].y]

    left_elbow_s = [result.pose_landmarks.landmark[13].z, result.pose_landmarks.landmark[13].y]
    left_wrist_s = [result.pose_landmarks.landmark[15].z, result.pose_landmarks.landmark[15].y]
    left_shoulder_s = [result.pose_landmarks.landmark[11].z, result.pose_landmarks.landmark[11].y]
    left_hip_s = [result.pose_landmarks.landmark[23].z, result.pose_landmarks.landmark[23].y]
    
    
    l_elb = calc_angle(left_shoulder, left_elbow, left_wrist)
    l_hip = calc_angle(left_hip, left_shoulder, left_elbow)
    l_hip_s = calc_angle(left_hip_s,left_shoulder_s,left_elbow_s)
    l_shoulder = calc_angle(left_elbow,left_shoulder,right_shoulder)
    l_elb_s = calc_angle(left_shoulder_s, left_elbow_s, left_wrist_s)


    if r_shoulder > 40 and r_shoulder < 150: # means the right hand has been used to block

        #checking elbow bend
        angle_elb = 100 - r_elb_s
        if r_elb_s < 90: 
            sentence += "Bend your elbow slighlty more by {} degrees".format(angle_elb)
        if r_elb_s > 120:
           sentence += "Straighten your elbow more by {} degrees".format(-angle_elb)
        else:
            sentence += "Good straightness of the elbow"


        angle_shoulder = 60-r_shoulder
        anlge_hip = 20 - r_hip_s
        if r_shoulder < 60:
           sentence += ", Move your arm to the right more by {} degrees so the elbow is in front of your right shoulder".format(angle_shoulder)
        elif r_shoulder > 90:
            sentence += ", Move your arm to the left more by {} degrees so the elbow is in front of your right shoulder".format(-angle_shoulder)
        
        if r_hip_s < 25:
           sentence += ", Move your arm slighlty up more by {} degrees".format(anlge_hip)

        if r_hip_s > 45:
            sentence +=  ", Move your arm slighlty down more by {} degrees".format(-anlge_hip)
        else:
            sentence += ", correct arm position for the inner forearm block"
        
    else: # left hand has been used to block
        #checking elbow bend
        angle_elb = 100 - l_elb_s
        if l_elb_s < 90: 
            sentence += "Bend your elbow slighlty more by {} degrees".format(angle_elb)
        if l_elb_s > 120:
           sentence += "Straighten your elbow more by {} degrees".format(-angle_elb)
        else:
            sentence += "Good straightness of the elbow"


        angle_shoulder = 60-l_shoulder
        anlge_hip = 20 - l_hip_s
        if l_shoulder < 60:
           sentence += ", Move your arm to the left more by {} degrees so the elbow is in front of your left shoulder".format(angle_shoulder)
        elif l_shoulder > 90:
            sentence += ", Move your arm to the right more by {} degrees so the elbow is in front of your left shoulder".format(-angle_shoulder)
        
        if l_hip_s < 25:
           sentence += ", Move your arm slighlty up more by {} degrees".format(anlge_hip)

        if l_hip_s > 45:
            sentence += ", Move your down slighlty more by {} degrees".format(-anlge_hip)
        else:
            sentence += ", correct arm position for the inner forearm block"

    return sentence

def angle_feedback_low(result,sentence):
    #getting angle between two points to provide feedback
    right_elbow = [result.pose_landmarks.landmark[14].z, result.pose_landmarks.landmark[14].y]
    right_wrist = [result.pose_landmarks.landmark[16].z, result.pose_landmarks.landmark[16].y]
    right_shoulder = [result.pose_landmarks.landmark[12].z, result.pose_landmarks.landmark[12].y]
    right_hip = [result.pose_landmarks.landmark[24].z, result.pose_landmarks.landmark[24].y]
    

    right_elbow_s = [result.pose_landmarks.landmark[14].z, result.pose_landmarks.landmark[14].y]
    right_wrist_s = [result.pose_landmarks.landmark[16].z, result.pose_landmarks.landmark[16].y]
    right_shoulder_s = [result.pose_landmarks.landmark[12].z, result.pose_landmarks.landmark[12].y]
    right_hip_s = [result.pose_landmarks.landmark[24].z, result.pose_landmarks.landmark[24].y]

    r_elb = calc_angle(right_shoulder,right_elbow,right_wrist)
    r_hip = calc_angle(right_hip, right_shoulder, right_elbow)
    r_hip_s = calc_angle(right_hip_s, right_shoulder_s, right_elbow_s)
    r_elb_s = calc_angle(right_shoulder_s,right_elbow_s,right_wrist_s)

    r_shoulder = calc_angle(right_elbow,right_shoulder,left_shoulder)

    left_elbow = [result.pose_landmarks.landmark[13].x, result.pose_landmarks.landmark[13].y]
    left_wrist = [result.pose_landmarks.landmark[15].x, result.pose_landmarks.landmark[15].y]
    left_shoulder = [result.pose_landmarks.landmark[11].x, result.pose_landmarks.landmark[11].y]
    left_hip = [result.pose_landmarks.landmark[23].x, result.pose_landmarks.landmark[23].y]

    left_elbow_s = [result.pose_landmarks.landmark[13].z, result.pose_landmarks.landmark[13].y]
    left_wrist_s = [result.pose_landmarks.landmark[15].z, result.pose_landmarks.landmark[15].y]
    left_shoulder_s = [result.pose_landmarks.landmark[11].z, result.pose_landmarks.landmark[11].y]
    left_hip_s = [result.pose_landmarks.landmark[23].z, result.pose_landmarks.landmark[23].y]
    
    
    l_elb = calc_angle(left_shoulder, left_elbow, left_wrist)
    l_hip = calc_angle(left_hip, left_shoulder, left_elbow)
    l_hip_s = calc_angle(left_hip_s,left_shoulder_s,left_elbow_s)
    l_shoulder = calc_angle(left_elbow,left_shoulder,right_shoulder)
    l_elb_s = calc_angle(left_shoulder_s, left_elbow_s, left_wrist_s)


    if r_shoulder > 70 and r_shoulder < 150: # means the right hand has been used to block

        #checking elbow bend
        angle_elb = 150 - r_elb
        #having greater kind of redundant as arm is allowed to be 180 degrees which is the maximum straightness
        if r_elb < 150: #
           sentence += "Straighten your elbow more by {} degrees".format(angle_elb)
        else:
            sentence += "Good straightness of the elbow"


        angle_shoulder = 90-r_shoulder
        anlge_hip = 30 - r_hip_s
        if r_shoulder < 90:
            sentence += ", Move your arm to the right more by {} degrees so the arm is in front of your right knee".format(angle_shoulder)
        elif r_shoulder > 90:
            sentence += ", Move your arm to the left more by {} degrees so the arm is in front of your right knee".format(-angle_shoulder)
        
        if r_hip_s < 30:
            sentence += ", Your arm is too close to your body, move it in front of you more by {} degrees".format(anlge_hip)

        if r_hip_s > 60:
            sentence +=  ", Your arm is too far from your body, move it closer to you by {} degrees".format(-anlge_hip)
        else:
            sentence += ", correct arm position for the inner forearm block"
        
    else: # left hand has been used to block
        
        #checking elbow bend
        angle_elb = 150 - l_elb
        #having greater kind of redundant as arm is allowed to be 180 degrees which is the maximum straightness
        if l_elb < 150: #
            sentence += "Straighten your elbow more by {} degrees".format(angle_elb)
        else:
            sentence += "Good straightness of the elbow"


        angle_shoulder = 90-l_shoulder
        anlge_hip = 30 - l_hip_s
        if l_shoulder < 90:
            sentence += ", Move your arm to the left more by {} degrees so the arm is in front of your right knee".format(angle_shoulder)
        elif l_shoulder > 90:
            sentence += ", Move your arm to the right more by {} degrees so the arm is in front of your right knee".format(-angle_shoulder)
        
        if l_hip_s < 30:
            sentence += ", Your arm is too close to your body, move it in front of you more by {} degrees".format(anlge_hip)

        if l_hip_s > 60:
            sentence +=  ", Your arm is too far from your body, move it closer to you by {} degrees".format(-anlge_hip)
        else:
            sentence += ", correct arm position for the inner forearm block"

    return sentence

def first_feedback_model(sequence,model,sentence):
        
        action = np.array(['Hands Off','Hands On'])

        res = model.predict(np.expand_dims(sequence, axis=0))[0]

        if action[np.argmax(res)] == action[0]:
            sentence += "Firsly please make sure you start the block with both hands on the hip"
        else:
            sentence += "Good starting position of your hands"

        return sentence
        #print(action[np.argmax(res)])
        
def second_feedback_model(sequence,model,sentence,a):
        action = np.array(['Crossing', 'No Cross']) 
        res = model.predict(np.expand_dims(sequence, axis=0))[0]

        if action[np.argmax(res)] == action[0]:
            sentence += ", You crossed and performed the chamber correctly"
        else:
            if a == 'Low Section':
                sentence += ", for the low section block make sure the chamber starts with the blocking hand on the opposite shouler and the non blocking hand starts across your body"

            elif a == 'Inner Section':
                sentence += ", for the inner forearm block make sure the the chamber starts with non blocking hand is straight in front of you and the blocking arm is bent directly next to your shoulder"

            elif a == 'High Section':
                sentence += ", for the high rising block make sure the the chamber starts with your arms performing a cross in front of you with the blocking arm horizontal and in front of the other arm which is vertical"

        return sentence

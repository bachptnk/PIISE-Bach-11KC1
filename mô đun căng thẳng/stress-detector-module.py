import cv2
import numpy as np
import csv
import warnings
warnings.filterwarnings("ignore")
#ghi chú, ngày mai trong cái trợ lý ảo làm vina , ngừng / ngưng để dừng mở module căng thẳng
#mai trong cái trợ lý ảo thêm code vina, căng thẳng để mở module căng thẳng

import pyttsx3
import datetime
def export_to_csv_Bach():
    csvdata = [datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S: %p")]
    with open("stress-checkpoint.csv","a") as csvFile:
        Fileout = csv.writer(csvFile, delimiter=',', quoting=csv.QUOTE_ALL)
        Fileout.writerow(csvdata)
PTNK_AI_assistant=pyttsx3.init()  # My name is Bach. I am learning in grade 10 in HIGH SCHOOL FOR THE GIFTED (PTNK)
voice=PTNK_AI_assistant.getProperty('voices')
assistant_voice_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_viVN_An'
PTNK_AI_assistant.setProperty('voice',assistant_voice_id)
Brate = 172
PTNK_AI_assistant.setProperty('rate',Brate)
def speak(audio):
    print('PTNK_AI_assistant: ' + audio)
    PTNK_AI_assistant.say(audio)
    PTNK_AI_assistant.runAndWait()
from keras.models import model_from_json
import time
global emotion_val
global not_stressed_val
global stressed_val
global steps_print_val
emotion_val=0
def reset_values_by_Bach():
    global emotion_val
    emotion_val=0
    global not_stressed_val
    not_stressed_val=0
    global stressed_val
    stressed_val=0
    global steps_print_val
    steps_print_val=0
reset_values_by_Bach()

emotion_dict = {0: "Angry", 1: "Disgusted", 2: "Fearful", 3: "Happy", 4: "Neutral", 5: "Sad", 6: "Surprised"}

# load json and create model
json_file = open('model/emotion_model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
emotion_model = model_from_json(loaded_model_json)
print('loading model ...')

# load weights into new model
emotion_model.load_weights("model/emotion_model.h5")
print("Loaded model from disk")

# start the webcam feed
cap = cv2.VideoCapture(0)

# pass here your video path
# you may download one from here : https://www.pexels.com/video/three-girls-laughing-5273028/
#cap = cv2.VideoCapture("C:\\JustDoIt\\ML\\Sample_videos\\emotion_sample6.mp4")

while True:
    # Find haar cascade to draw bounding box around face
    ret, frame = cap.read()
    frame = cv2.resize(frame, (1280, 720))
    if not ret:
        break
    face_detector = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # detect faces available on camera
    num_faces = face_detector.detectMultiScale(gray_frame, scaleFactor=1.3, minNeighbors=5)

    # take each face available on the camera and Preprocess it
    for (x, y, w, h) in num_faces:
        cv2.rectangle(frame, (x, y-50), (x+w, y+h+10), (0, 255, 0), 4)
        roi_gray_frame = gray_frame[y:y + h, x:x + w]
        cropped_img = np.expand_dims(np.expand_dims(cv2.resize(roi_gray_frame, (48, 48)), -1), 0)

        # predict the emotions
        emotion_prediction = emotion_model.predict(cropped_img)
        maxindex = int(np.argmax(emotion_prediction))
        cv2.putText(frame, emotion_dict[maxindex], (x+5, y-20), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
        print(emotion_dict[maxindex])
        if (emotion_dict[maxindex]=='Happy') or (emotion_dict[maxindex]=='Neutral') or (emotion_dict[maxindex]=='Surprised'):
            #with open('data_stress_val.txt', 'a') as the_file:
                #the_file.write('1\n')
            not_stressed_val= not_stressed_val +1
            steps_print_val=steps_print_val +1 
            emotion_val=(not_stressed_val+stressed_val)/steps_print_val
            print(emotion_val)
            if (steps_print_val==25) and emotion_val<=(-0.342):
                speak('Có vẻ bạn đang căng thẳng')
                speak('Hãy cố gắng bình tĩnh và kiểm soát cảm xúc của mình')
                speak('Bạn nên nghỉ một chút để giảm căng thẳng. Bạn có thể gọi "vi na" và yêu cầu phát nhạc hoặc kể chuyện cười để giảm căng thẳng')
                export_to_csv_Bach()
                reset_values_by_Bach()
            if (steps_print_val==25) and emotion_val>(-0.342):
                reset_values_by_Bach()
        if (emotion_dict[maxindex]=='Angry') or (emotion_dict[maxindex]=='Sad') or (emotion_dict[maxindex]=='Disgusted') or (emotion_dict[maxindex]=='Fearful'):
            #with open('data_stress_val.txt', 'a') as the_file:
                #the_file.write('-1\n')
            stressed_val=stressed_val-1
            steps_print_val=steps_print_val +1 
            emotion_val=(not_stressed_val+stressed_val)/steps_print_val
            print(emotion_val)
            if (steps_print_val==25) and emotion_val<=(-0.342):
                speak('Có vẻ bạn đang căng thẳng')
                speak('Hãy cố gắng bình tĩnh và kiểm soát cảm xúc của mình')
                speak('Bạn nên nghỉ một chút để giảm căng thẳng. Bạn có thể gọi tôi và yêu cầu tôi phát nhạc hoặc kể chuyện cười để giảm căng thẳng')
                export_to_csv_Bach()
                reset_values_by_Bach()
            if (steps_print_val==25) and emotion_val>(-0.342):
                reset_values_by_Bach()

    cv2.imshow('Emotion Detection', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

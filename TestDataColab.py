from keras.models import load_model
import cv2
import numpy as np

#load models
model_age = load_model('D:/learn/ai/mlbasic/nhandien/dudoantuoigt/colab/models/modelage.h5')
model_gender = load_model('D:/learn/ai/mlbasic/nhandien/dudoantuoigt/colab/models/modelgender.h5')

#label
label_gender = ['male', 'female']
label_age = ["8-12", "13-18", "19-25", "26-32", "33-44", "45-55", "56-70", "71-80"]

def detect_image():
    link = str(input("Link Image: "))
    x_test = np.array(cv2.resize(cv2.imread(link), dsize= (92, 92))).reshape(1, 92, 92, 3)
    test_age = model_age.predict(x_test)
    test_gender = model_gender.predict(x_test)

    # print(test_age)
    print(label_age[np.argmax(test_age)])
    print(label_gender[np.argmax(test_gender)])
    img = cv2.imread(link)

    # Show image
    font = cv2.FONT_HERSHEY_SIMPLEX
    org_age = (50, 50)
    org_gender = (50, 90)
    fontScale = 1
    color = (0, 255, 0)
    thickness = 2

    cv2.putText(img, str(label_age[np.argmax(test_age)]), org_age, font, fontScale, color, thickness, cv2.LINE_AA)
    cv2.putText(img, str(label_gender[np.argmax(test_gender)]), org_gender, font, fontScale, color, thickness, cv2.LINE_AA)
    cv2.imshow('nhan dien', img)
    cv2.waitKey(0)

# real live
def live():
    cap = cv2.VideoCapture(0)
    cap.set(3, 1200)
    cap.set(4, 1200)

    while True:
        ret, image_org = cap.read()
        image_detect = image_org
        if not ret:
            continue
        
        image_org = cv2.flip(image_org, 1)
        gray = cv2.cvtColor(image_org, cv2.COLOR_BGR2GRAY)

        #face detection box
        facedetect = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        faces = facedetect.detectMultiScale(gray, 1.3, 5)
        for x,y,w,h in faces:
            cv2.rectangle(image_org, (x,y), (x+w,y+h), (0,255,0), 2)
            image_detect = image_org[x:x+w,y:y+h]


        #detect age
        predict_age = model_age.predict(np.array(cv2.resize(image_detect, dsize = (92, 92))).reshape(1, 92, 92, 3))
        age = label_age[np.argmax(predict_age)]
        rate_age = np.max(predict_age)
        print("Age: , rate: %")

        #detect gender
        predict_gender = model_gender.predict(np.array(cv2.resize(image_detect, dsize = (92, 92))).reshape(1, 92, 92, 3))
        gender = label_gender[np.argmax(predict_gender)]
        rate_gender = np.max(predict_gender)
        print(f"Gender: {gender}, rate: {rate_gender*100}%")

        #print
        if np.max(predict_age) > 0.4:
            print("Age: " + str(age) + ", rate_age: " + str(round(rate_age*100, 2)) + "%")
            print("Gender: " + str(gender) + ", rate_gender: " + str(round(rate_gender*100, 2)) + "%")

            # Show image
            font = cv2.FONT_HERSHEY_SIMPLEX
            org_age = (50, 50)
            org_gender = (50, 90)
            fontScale = 1
            color = (0, 255, 0)
            thickness = 2

            out_age = "Age: " + str(age) + ", rate: " + str(round(rate_age*100, 2)) + "%"
            out_gender = "Gender: " + str(gender) + ", rate: " + str(round(rate_gender*100, 2)) + "%"

            cv2.putText(image_org, out_age, org_age, font, fontScale, color, thickness, cv2.LINE_AA)
            cv2.putText(image_org, out_gender, org_gender, font, fontScale, color, thickness, cv2.LINE_AA)

        cv2.imshow("Picture", image_org)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


#_____________________________________________________________________
print("Tutorial: Select 0 or 1 to use the feature\nClick \"q\" to Stop ")
choose = int(input("0: Image Detection\n1: Real Time\nChoose: "))
if choose == 0:
    detect_image()
elif choose == 1:
    live()
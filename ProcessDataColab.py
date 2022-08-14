from os import listdir
import pickle
import cv2
import numpy as np
from keras.utils import np_utils


def choose_file(raw_folder):
    file8_12    = []
    file13_18   = []
    file19_25   = []
    file26_32   = []
    file33_44   = []
    file45_55   = []
    file56_70   = []
    file71_80   = []
    for file in listdir(raw_folder):
        print('File = ', file)
        if int(file.split("_")[0]) >= 8 and int(file.split("_")[0]) <= 12:
            file8_12.append(file)
        elif int(file.split("_")[0]) >= 14 and int(file.split("_")[0]) <= 18:
            file13_18.append(file)
        elif int(file.split("_")[0]) >= 20 and int(file.split("_")[0]) <= 23:
            file19_25.append(file)
        elif int(file.split("_")[0]) >= 26 and int(file.split("_")[0]) <= 30:
            file26_32.append(file)
        elif int(file.split("_")[0]) >= 36 and int(file.split("_")[0]) <= 40:
            file33_44.append(file)
        elif int(file.split("_")[0]) >= 50 and int(file.split("_")[0]) <= 52:
            file45_55.append(file)
        elif int(file.split("_")[0]) >= 60 and int(file.split("_")[0]) <= 64:
            file56_70.append(file)  
        elif int(file.split("_")[0]) >= 72 and int(file.split("_")[0]) <= 76:
            file71_80.append(file)
    return file8_12, file13_18, file19_25, file26_32, file33_44, file45_55, file56_70, file71_80


def save_data(raw_folder, save_file):
    file8_12, file13_18, file19_25, file26_32, file33_44, file45_55, file56_70, file71_80 = choose_file(raw_folder)
    print('Bat dau xu ly hinn anh:')
    pixels = []
    labels_age = []
    labels_gender = []
    
    for folder in file8_12, file13_18, file19_25, file26_32, file33_44, file45_55, file56_70, file71_80:
        for file in folder:
            print(' File = ', file)
            if file in file8_12:
                labels_age.append(1)
                pixels.append(cv2.resize(cv2.imread(raw_folder + file), dsize = (92,92))/225.0)
                labels_gender.append(file.split("_")[1])
            elif file in file13_18:
                labels_age.append(2)
                pixels.append(cv2.resize(cv2.imread(raw_folder + file), dsize = (92,92))/225.0)
                labels_gender.append(file.split("_")[1])
            elif file in file19_25:
                labels_age.append(3)
                pixels.append(cv2.resize(cv2.imread(raw_folder + file), dsize = (92,92))/225.0)
                labels_gender.append(file.split("_")[1])
            elif file in file26_32:
                labels_age.append(4)
                pixels.append(cv2.resize(cv2.imread(raw_folder + file), dsize = (92,92))/225.0)
                labels_gender.append(file.split("_")[1])
            elif file in file33_44:
                labels_age.append(5)
                pixels.append(cv2.resize(cv2.imread(raw_folder + file), dsize = (92,92))/225.0)
                labels_gender.append(file.split("_")[1])
            elif file in file45_55:
                labels_age.append(6)
                pixels.append(cv2.resize(cv2.imread(raw_folder + file), dsize = (92,92))/225.0)
                labels_gender.append(file.split("_")[1])
            elif file in file56_70:
                labels_age.append(7)
                pixels.append(cv2.resize(cv2.imread(raw_folder + file), dsize = (92,92))/225.0)
                labels_gender.append(file.split("_")[1])
            elif file in file71_80:
                labels_age.append(8)
                pixels.append(cv2.resize(cv2.imread(raw_folder + file), dsize = (92,92))/225.0)
                labels_gender.append(file.split("_")[1])

    pixels = np.array(pixels)
    labels_age = np.array(labels_age)
    labels_gender = np.array(labels_gender)

    from sklearn.preprocessing import LabelBinarizer
    encoder = LabelBinarizer()
    labels_age = encoder.fit_transform(labels_age)
    labels_gender = np_utils.to_categorical(labels_gender, 2, dtype = np.int32)

    print('Data cua UTKface da xu li.')
    file = open(save_file, 'wb')
    pickle.dump((pixels, labels_age, labels_gender), file, protocol=4)
    file.close()

    print(pixels.shape)
    print(labels_age.shape)
    print(labels_gender.shape)
    print(len(file8_12) + len(file13_18) + len(file19_25) + len(file26_32) + len(file33_44) + len(file45_55) + len(file56_70) + len(file71_80))


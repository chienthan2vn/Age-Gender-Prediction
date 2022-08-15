from os import listdir
import pickle
import cv2
import numpy as np
from keras.utils import np_utils


def choose_file(raw_folder):
    file_1_4     = []
    file_5_8     = []
    file_9_12    = []
    file_13_16   = []
    file_19_22   = []
    file_23_26   = []
    file_27_30   = []
    file_31_34   = []
    file_35_38   = []
    file_39_42   = []
    file_43_46   = []
    file_47_50   = []
    file_51_56   = []
    file_57_62   = []
    file_63_70   = []
    file_71_80   = []
    file_81_90   = []
    file_91_116  = []


    for file in listdir(raw_folder):
        print('File = ', file)
        if int(file.split("_")[0]) >= 1 and int(file.split("_")[0]) <= 4:
            file_1_4.append(file)
        if int(file.split("_")[0]) >= 5 and int(file.split("_")[0]) <= 8:
            file_5_8.append(file)
        elif int(file.split("_")[0]) >= 9 and int(file.split("_")[0]) <= 12:
            file_9_12.append(file)
        elif int(file.split("_")[0]) >= 13 and int(file.split("_")[0]) <= 16:
            file_13_16.append(file)
        elif int(file.split("_")[0]) >= 19 and int(file.split("_")[0]) <= 22:
            file_19_22.append(file)
        elif int(file.split("_")[0]) >= 23 and int(file.split("_")[0]) <= 26:
            file_23_26.append(file)
        elif int(file.split("_")[0]) >= 27 and int(file.split("_")[0]) <= 30:
            file_27_30.append(file)
        elif int(file.split("_")[0]) >= 31 and int(file.split("_")[0]) <= 34:
            file_31_34.append(file)  
        elif int(file.split("_")[0]) >= 35 and int(file.split("_")[0]) <= 38:
            file_35_38.append(file)
        elif int(file.split("_")[0]) >= 39 and int(file.split("_")[0]) <= 42:
            file_39_42.append(file)
        elif int(file.split("_")[0]) >= 43 and int(file.split("_")[0]) <= 46:
            file_43_46.append(file)
        elif int(file.split("_")[0]) >= 47 and int(file.split("_")[0]) <= 50:
            file_47_50.append(file)
        elif int(file.split("_")[0]) >= 51 and int(file.split("_")[0]) <= 56:
            file_51_56.append(file)
        elif int(file.split("_")[0]) >= 57 and int(file.split("_")[0]) <= 62:
            file_57_62.append(file)
        elif int(file.split("_")[0]) >= 63 and int(file.split("_")[0]) <= 70:
            file_63_70.append(file)
        elif int(file.split("_")[0]) >= 71 and int(file.split("_")[0]) <= 80:
            file_71_80.append(file)
        elif int(file.split("_")[0]) >= 81 and int(file.split("_")[0]) <= 90:
            file_81_90.append(file)
        elif int(file.split("_")[0]) >= 91 and int(file.split("_")[0]) <= 116:
            file_91_116.append(file)
    return file_1_4, file_5_8, file_9_12, file_13_16, file_19_22, file_23_26, file_27_30, file_31_34, file_35_38, file_39_42, file_43_46, file_47_50, file_51_56, file_57_62, file_63_70, file_71_80, file_81_90, file_91_116


def save_data(raw_folder, save_file):
    file_1_4, file_5_8, file_9_12, file_13_16, file_19_22, file_23_26, file_27_30, file_31_34, file_35_38, file_39_42, file_43_46, file_47_50, file_51_56, file_57_62, file_63_70, file_71_80, file_81_90, file_91_116 = choose_file(raw_folder)
    print('Bat dau xu ly hinn anh:')
    pixels = []
    labels_age = []
    labels_gender = []
    
    for folder in file_1_4, file_5_8, file_9_12, file_13_16, file_19_22, file_23_26, file_27_30, file_31_34, file_35_38, file_39_42, file_43_46, file_47_50, file_51_56, file_57_62, file_63_70, file_71_80, file_81_90, file_91_116:
        for file in folder:
            print(' File = ', file)
            if file in file_1_4:
                labels_age.append(1)
                pixels.append(cv2.resize(cv2.imread(raw_folder + file), dsize = (92,92)))
                labels_gender.append(file.split("_")[1])
            elif file in file_5_8:
                labels_age.append(2)
                pixels.append(cv2.resize(cv2.imread(raw_folder + file), dsize = (92,92)))
                labels_gender.append(file.split("_")[1])
            elif file in file_9_12:
                labels_age.append(3)
                pixels.append(cv2.resize(cv2.imread(raw_folder + file), dsize = (92,92)))
                labels_gender.append(file.split("_")[1])
            elif file in file_13_16:
                labels_age.append(4)
                pixels.append(cv2.resize(cv2.imread(raw_folder + file), dsize = (92,92)))
                labels_gender.append(file.split("_")[1])
            elif file in file_19_22:
                labels_age.append(5)
                pixels.append(cv2.resize(cv2.imread(raw_folder + file), dsize = (92,92)))
                labels_gender.append(file.split("_")[1])
            elif file in file_23_26:
                labels_age.append(6)
                pixels.append(cv2.resize(cv2.imread(raw_folder + file), dsize = (92,92)))
                labels_gender.append(file.split("_")[1])
            elif file in file_27_30:
                labels_age.append(7)
                pixels.append(cv2.resize(cv2.imread(raw_folder + file), dsize = (92,92)))
                labels_gender.append(file.split("_")[1])
            elif file in file_31_34:
                labels_age.append(8)
                pixels.append(cv2.resize(cv2.imread(raw_folder + file), dsize = (92,92)))
                labels_gender.append(file.split("_")[1])
            elif file in file_35_38:
                labels_age.append(9)
                pixels.append(cv2.resize(cv2.imread(raw_folder + file), dsize = (92,92)))
                labels_gender.append(file.split("_")[1])
            elif file in file_39_42:
                labels_age.append(10)
                pixels.append(cv2.resize(cv2.imread(raw_folder + file), dsize = (92,92)))
                labels_gender.append(file.split("_")[1])
            elif file in file_43_46:
                labels_age.append(11)
                pixels.append(cv2.resize(cv2.imread(raw_folder + file), dsize = (92,92)))
                labels_gender.append(file.split("_")[1])
            elif file in file_47_50:
                labels_age.append(12)
                pixels.append(cv2.resize(cv2.imread(raw_folder + file), dsize = (92,92)))
                labels_gender.append(file.split("_")[1])
            elif file in file_51_56:
                labels_age.append(13)
                pixels.append(cv2.resize(cv2.imread(raw_folder + file), dsize = (92,92)))
                labels_gender.append(file.split("_")[1])
            elif file in file_57_62:
                labels_age.append(14)
                pixels.append(cv2.resize(cv2.imread(raw_folder + file), dsize = (92,92)))
                labels_gender.append(file.split("_")[1])
            elif file in file_63_70:
                labels_age.append(15)
                pixels.append(cv2.resize(cv2.imread(raw_folder + file), dsize = (92,92)))
                labels_gender.append(file.split("_")[1])
            elif file in file_71_80:
                labels_age.append(16)
                pixels.append(cv2.resize(cv2.imread(raw_folder + file), dsize = (92,92)))
                labels_gender.append(file.split("_")[1])
            elif file in file_81_90:
                labels_age.append(17)
                pixels.append(cv2.resize(cv2.imread(raw_folder + file), dsize = (92,92)))
                labels_gender.append(file.split("_")[1])
            elif file in file_91_116:
                labels_age.append(18)
                pixels.append(cv2.resize(cv2.imread(raw_folder + file), dsize = (92,92)))
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


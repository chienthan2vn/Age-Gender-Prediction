#Load data
def load_data(data):
    import pickle
    file = open(data, 'rb')
    pixels, labels_age, labels_gender = pickle.load(file)
    file.close()
    return pixels, labels_age, labels_gender

# chia bo data
def split_data(pixels, labels):
    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(pixels, labels, test_size = 0.2, random_state=42)
    return x_train, x_test, y_train, y_test

#VGG_face
def VGG_face(x_train, x_test, y_train, y_test, number, save_model):
    #Lib
    import pandas as pd
    from keras.layers import Dropout, Flatten, Dense, BatchNormalization, Conv2D, MaxPooling2D, Dropout
    from keras.preprocessing.image import ImageDataGenerator
    from keras import regularizers
    from keras.applications.vgg16 import VGG16
    from keras.models import Sequential

    #Model
    model = Sequential()
    model.add(Conv2D(64,(3,3),activation='relu',input_shape=(92,92,3)))
    model.add(Conv2D(64,(3,3),activation='relu'))
    model.add(MaxPooling2D((2,2)))
    model.add(BatchNormalization())

    model.add(Conv2D(128,(3,3),activation='relu'))
    model.add(Conv2D(128,(3,3),activation='relu'))
    model.add(MaxPooling2D((2,2)))
    model.add(BatchNormalization())

    model.add(Conv2D(256,(3,3),activation='relu'))
    model.add(Conv2D(256,(3,3),activation='relu'))
    model.add(MaxPooling2D(2,2))
    model.add(BatchNormalization())

    model.add(Conv2D(512,(3,3),activation='relu'))
    model.add(Conv2D(512,(3,3),activation='relu'))
    model.add(MaxPooling2D((2,2)))
    model.add(BatchNormalization())
    
    model.add(Flatten())
    model.add(Dense(512,activation='relu',kernel_regularizer=regularizers.l2(0.01)))
    model.add(Dense(256,activation='relu',kernel_regularizer=regularizers.l2(0.01)))
    model.add(Dense(64,activation='relu',kernel_regularizer=regularizers.l2(0.01)))
    model.add(Dense(number,activation='softmax',kernel_regularizer=regularizers.l2(0.01)))
    model.summary()

    #compile model
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

    # construct the training image generator for data augmentation
    aug = ImageDataGenerator(rotation_range=20, zoom_range=0.1, width_shift_range=0.1, height_shift_range=0.1, horizontal_flip=True, brightness_range=[0.2,1.5], fill_mode="nearest")
    loss = model.fit_generator(aug.flow(x_train, y_train, batch_size = 40), epochs = 50, validation_data = aug.flow(x_test, y_test, batch_size = 40))
    pd.DataFrame(loss.history).plot()
    model.save(save_model)
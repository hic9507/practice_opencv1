import os
import cv2
# import tensorflow as tf
import numpy as np
# import keras
from sklearn.model_selection import train_test_split

### 동영상 폴더
train_folder = 'D:/abnormal_detection_dataset/UBI_FIGHTS/videos/All/'
frame_folder = 'D:/abnormal_detection_dataset/UBI_FIGHTS/frames/'

### 프레임 추출
frame_list = []
cnt = 0
for file in os.listdir(train_folder):
    video = cv2.VideoCapture(file)
    ret, images = video.read()

    while video.isOpened():
        ret, images = video.read()

        if int(video.get(1)) % 10 == 0:
            cv2.imwrite(frame_folder + file + '_' + cnt + '.png', images)
            print('Saved frame number: ', str(int(video.get(1))))
            cnt += 1
    video.release()
    

### normal/abnormal 분리
for file_name in frame_folder:
    values = []
    labels = []

    if file_name[0:2] == 'F_':
        values.append(file_name)
        labels.append([1, 0])

    elif file_name[0:2] == 'N_':
        values.append(file_name)
        labels.append([0, 1])

merge = list(zip(values, labels))
shuffle(merge)

values, labels = zip(*merge)


### 모델 생성
model = Sequential()
input_tensor = Input(shape=(IMG_SIZE, IMG_SIZE, ColorChannels))
input_shape = (IMG_SIZE, IMG_SIZE, ColorChannels) # (128, 128, 3)

model.add(layers.Input(shape=(input_shape)))
model.add(layers.Conv2D(filters=64, kernel_size=(3, 3), padding='same', activation = 'relu'))
model.add(layers.MaxPooling2D(strides=(2,2)))

model.add(layers.Conv2D(filters=64, kernel_size=(3, 3), padding='same', activation = 'relu'))
model.add(layers.Dropout(0.2))
model.add(layers.MaxPooling2D(strides=(2, 2)))

model.add(layers.Conv2D(filters=128, kernel_size=(3, 3), padding='same', activation = 'relu'))
model.add(layers.Dropout(0.2))
model.add(layers.MaxPooling2D(strides=(2, 2)))

model.add(layers.Conv2D(filters=256, kernel_size=(3, 3), padding='same', activation='relu'))
model.add(layers.Dropout(0.2))
model.add(layers.MaxPooling2D(strides=(2, 2)))

model.add(layers.Conv2D(filters=256, kernel_size=(3, 3), padding='same', activation='relu'))
model.add(layers.Dropout(0.2))

model.add(layers.Flatten())
model.add(layers.Dense(1024, activation='relu'))
model.add(layers.Dropout(0.2))

model.add(layers.Dense(512, activation='relu'))

model.add(layers.Dense(1, activation='sigmoid'))
model = Model(inputs=model.input, outputs=model.output)

for layer in model.layers:
    layer.trainable = True

### 모델 컴파일
print('모델 컴파일 중')
model. compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

model.summary()


### 콜백 함수 정의
patience = 10

start_lr = 0.00001
min_lr = 0.00001
max_lr = 0.00005

batch_size = 32 #128


rampup_epochs = 5
sustain_epochs = 0
exp_decay = 0.0001

def lrfn(epoch):
    if epoch < rampup_epochs:
        return (max_lr - start_lr)/rampup_epochs * epoch + start_lr
    elif epoch < rampup_epochs + sustain_epochs:
        return max_lr
    else:
        return (max_lr - min_lr) * exp_decay**(epoch-rampup_epochs-sustain_epochs) + min_lr


class myCallback(Callback):
    def on_epoch_end(self, epoch, logs={}):
        if ((logs.get('accuracy')>=0.999)):
            print("\nLimits Reached cancelling training!")
            self.model.stop_training = True


end_callback = myCallback()

lr_callback = LearningRateScheduler(lambda epoch: lrfn(epoch), verbose=False)

early_stopping = EarlyStopping(patience = patience, monitor='val_loss',
                                 mode='min', restore_best_weights=True, 
                                 verbose = 1, min_delta = .00075)

PROJECT_DIR = MyDrive + '/RiskDetection'

lr_plat = ReduceLROnPlateau(patience = 2, mode = 'min')

# os.system('rm -rf ./logs/')

log_dir = "logs/fit/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
# tensorboard_callback = TensorBoard(log_dir = log_dir, write_graph=True, histogram_freq=1)

checkpoint_filepath = './checkpoint.h5'

model_checkpoints = ModelCheckpoint(filepath=checkpoint_filepath,
                                        save_weights_only=True,
                                        monitor='val_loss',
                                        mode='min',
                                        verbose = 1,
                                        save_best_only=True)


# callbacks = [end_callback, lr_callback, model_checkpoints, early_stopping, lr_plat]
callbacks = [model_checkpoints, early_stopping]


### 모델 핏
n_sample = int(len(frame_folder))
n_train = int(n_sample * 0.8)
n_test = n_sample - n_train

x_train, y_train, x_test, y_test = train_test_split(values, labels, test_size=0.2, shuffle=True, random_state=34)

history = model.fit(x_train ,y_train, epochs=epochs, callbacks=callbacks, validation_data = (x_test, y_test),
                        batch_size=batch_size)
model.load_weights(checkpoint_filepath)

plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('Train and Validation accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'valid'], loc='upper left')
plt.show()
# summarize history for loss
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Train and Validation loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'valid'], loc='upper left')
plt.show()

# Violence = "C:/Users/user/Desktop/download.mp4"
# print(print_results(Violence, limit=30))

# ### 16
# NonViolence = "D:/abnormal_detection_dataset/UBI_FIGHTS/videos/All/N_0_0_0_1_0.mp4"
# print(print_results(NonViolence, limit=50))
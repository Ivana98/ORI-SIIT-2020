import warnings
from datetime import datetime

from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Conv2D, BatchNormalization, MaxPooling2D, Dense, Dropout, Flatten
from keras.layers import Activation
import keras

warnings.filterwarnings("ignore")


# Constants

IMG_W, IMG_H = 64, 64
NUM_OF_CLASSES = 3
BATCH_SIZE = 32
EPOCHS = 30

train_dir = "../data/train_set"
valid_dir = "../data/valid_set"
test_dir = "../data/test_set"
save_path = "../data/saved_models"

# start timer
start = datetime.now()
start_time = start.strftime("%H:%M:%S")

# Load images
train_datagen = ImageDataGenerator(
    rescale=1. / 255,
    horizontal_flip=True,
    zoom_range=0.2
    )

valid_datagen = ImageDataGenerator(rescale=1. / 255)

test_datagen = ImageDataGenerator(rescale=1. / 255)

train_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=(IMG_W, IMG_H),
    batch_size=32,
    class_mode='categorical')

validation_generator = valid_datagen.flow_from_directory(
    valid_dir,
    target_size=(IMG_W, IMG_H),
    batch_size=32,
    class_mode='categorical')

test_generator = test_datagen.flow_from_directory(
    test_dir,
    target_size=(IMG_W, IMG_H),
    batch_size=32,
    class_mode='categorical')

# Model

model = Sequential()
model.add(Conv2D(64, kernel_size=(3, 3), input_shape=(IMG_W, IMG_H, 3)))
model.add(Activation("relu"))
model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(64, kernel_size=(3, 3)))
model.add(Activation("sigmoid"))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(128, kernel_size=(3, 3)))
model.add(Activation("relu"))
model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(128, kernel_size=(3, 3)))
model.add(Activation("sigmoid"))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())
model.add(Dense(128, activation="relu", kernel_regularizer=keras.regularizers.l2(0.001)))
model.add(Dropout(0.5))
model.add(Dense(64, kernel_regularizer=keras.regularizers.l2(0.001)))
model.add(Dense(NUM_OF_CLASSES, activation="softmax"))

model.summary()

# Compile model
model.compile(
    loss=keras.losses.categorical_crossentropy,
    optimizer=keras.optimizers.Adamax(),
    metrics=['accuracy']
)

fit_generator = model.fit_generator(
    generator=train_generator,
    validation_data=validation_generator,
    epochs=EPOCHS
)

try:
    save_path = save_path + "/11th_trial.h5"
    model.save_weights(save_path)
except:
    print("Could not save model.")

tested = model.evaluate(test_generator)

print("Tested:")
print(tested)

# Show results
# score = model.evaluate_generator(train_generator, verbose=0)

# print('Test loss:', score[0])
# print('Test accuracy:', score[1])

# end timer
print()
end = datetime.now()
end_time = end.strftime("%H:%M:%S")
print("Start Time =", start_time)
print("End Time =", end_time)
duration = end - start
print("Duration: ", duration)

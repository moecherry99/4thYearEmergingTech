# imports tf/kr
import tensorflow as tf
# import tensorflowjs as tfjs (not working)
import keras as kr

# split the mnist data into train and test
(train_img,train_label),(test_img,test_label) = kr.datasets.mnist.load_data()

# img shape
train_img = train_img.reshape([-1, 28, 28, 1])
test_img = test_img.reshape([-1, 28, 28, 1])
train_img = train_img/255.0
test_img = test_img/255.0

train_label = kr.utils.to_categorical(train_label)
test_label = kr.utils.to_categorical(test_label)

tf.compat.v1.enable_eager_execution()

# model creation
model = kr.Sequential([
    kr.layers.Conv2D(32, (5, 5), padding="same", input_shape=[28, 28, 1]),
    kr.layers.MaxPool2D((2,2)),
    kr.layers.Conv2D(64, (5, 5), padding="same"),
    kr.layers.MaxPool2D((2,2)),
    kr.layers.Flatten(),
    kr.layers.Dense(1024, activation='relu'),
    kr.layers.Dropout(0.2),
    kr.layers.Dense(10, activation='softmax')
])

# view model
model.summary()

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# 7 iterations and show accuracy
model.fit(train_img,train_label, validation_data=(test_img,test_label), epochs=7)

# save the model
model.save("model-9924.h5")

# convert model
# not working, grabbed file from https://github.com/bensonruan/Hand-Written-Digit-Recognition

# tfjs.converters.save_keras_model(model, 'static/models')
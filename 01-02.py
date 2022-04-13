# Упражнение 1. Предсказание цен на жилье

import tensorflow as tf
import numpy as np
from tensorflow import keras

def house_model(y_new):
    xs =  np.array([1, 2, 3, 4, 5, 6, 7], dtype=float)
    ys =  np.array([1, 1.5, 2.0, 2.5, 3, 3.5, 4], dtype=float)
    layer_0 = keras.layers.Dense(units=1, input_shape=[1])
    #layer_1 = keras.layers.Dense(units=3, input_shape=[1])
    #layer_2 = keras.layers.Dense(units=1, input_shape=[1])
    model = tf.keras.Sequential([layer_0]) #, layer_1, layer_2])
    model.compile(optimizer='sgd', loss='mean_squared_error')
    model.fit(xs, ys, epochs=50)
    #print("Layer variables look like this: {}".format(layer_0.get_weights()))
    return model.predict(y_new)[0]*100

prediction = house_model([7.0])
print(prediction)

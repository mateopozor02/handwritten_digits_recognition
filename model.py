import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras import backend as K

#Se carga el dataset de MNIST
(x_train, y_train), (x_test, y_test) = mnist.load_data()?
print(x_train.shape, y_train.shape)

#Preprocesamiento de datos. Se redimensionan las matrices del dataset 

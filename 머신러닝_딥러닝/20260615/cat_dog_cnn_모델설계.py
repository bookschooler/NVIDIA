from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.layers import Conv2D, MaxPooling2D

model = Sequential()
model.add( Conv2D( filters=16, kernel_size=(3,3), activation='relu', padding = 'valid', input_shape = (150, 150, 3)))
model.add ( MaxPooling2D(pool_size = (2,2)))
model.add( Conv2D( filters = 32, kernel_size=(3,3), activation='relu'))
model.add ( MaxPooling2D(pool_size = (2,2)))
model.add( Conv2D( filters = 64, kernel_size=(3,3), activation='relu'))
model.add ( MaxPooling2D(pool_size = (2,2)))
model.add( Flatten())
model.add( Dense( units = 512, activation='relu'))
model.add( Dense( units = 1, activation='sigmoid'))
model.summary()
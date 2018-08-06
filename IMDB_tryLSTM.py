# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 09:51:04 2018
@author: audrey roumieux
Projet:
Description:
"""
from keras.datasets import imdb
from keras.preprocessing.sequence import pad_sequences
from keras import models
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers.embeddings import Embedding

(X_train, Y_train), (X_test, Y_test) = imdb.load_data(num_words=12000)

pad_train =  pad_sequences(X_train)
pad_test = pad_sequences(X_test)

model = models.Sequential()
model.add(Embedding(100000, 32))
model.add(LSTM(32, dropout=0.2, recurrent_dropout=0.2))
model.add(Dense(1, activation='sigmoid'))

print(model.summary())
model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

model.fit(pad_train, Y_train, batch_size=64, epochs=5)
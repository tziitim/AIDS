#!/usr/bin/env python



import tensorflow

from settings import *

#from tensorflow.keras import layers
#import tensorflow.keras as keras
#from keras.models import Sequential
#from keras.layers import Dense, Activation

from keras.models import Sequential
from keras.layers import Dense, Input
from keras.layers import InputLayer


model = 0;

def AIPlayerChoice():
    model();
	

def InitAI():
    #print("Tensorflow Version: " + VERSION)
    print("TF.Keras Version" + tensorflow.keras.__version__)
    
    #model = tf.keras.Sequential([#Use a seqention model to get an output from 0-(n^M)
    #    layers.Dense(64,use_bias=True, activation = 'relu', inputshape = )
    #]);
    model = tensorflow.keras.Sequential();
    model.add(InputLayer(input_shape=(SIZE**D,)))
    model.add(Dense(9,use_bias=True,activation = 'relu'));#,input_dim=SIZE**D));
    model.add(Dense(9,use_bias=True,activation = 'relu'));
    model.add(Dense(9,use_bias=True,activation = 'relu'));
    model.add(Dense(9,use_bias=True,activation = 'relu'));
    model.add(Dense(9,use_bias=True,activation = 'relu'));
    model.add(Dense(9,use_bias=True,activation = 'relu'));
    
    model.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])
    
    import numpy as np
    
def TrainAI():
    model.fit();
    

def CloseAI():
    return;

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
from keras.models import Sequential
from keras.layers import InputLayer
from keras.layers import Dense, Input
from keras.layers.normalization import BatchNormalization





def AIPlayerChoice():
    return model();
    



def InitAI():
    #print("Tensorflow Version: " + VERSION)
    print("TF.Keras Version" + tensorflow.keras.__version__)
    
    ##model = tf.keras.Sequential([#Use a seqention model to get an output from 0-(n^M)
    ##    layers.Dense(64,use_bias=True, activation = 'relu', inputshape = )
    ##]);
    #model = tensorflow.keras.Sequential([Dense(32, input_shape=(784,))]);
    ##model.add(InputLayer(input_shape=(SIZE**D,)))
    #model.add(Dense(9,use_bias=True,activation = 'relu'));#,input_dim=SIZE**D));
    #model.add(Dense(9,use_bias=True,activation = 'relu'));
    #model.add(Dense(9,use_bias=True,activation = 'relu'));
    #model.add(Dense(9,use_bias=True,activation = 'relu'));
    #model.add(Dense(9,use_bias=True,activation = 'relu'));
    #model.add(Dense(9,use_bias=True,activation = 'relu'));
    #
    #model.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])
    
    input_shape = (SIZE**D, 1, 1)#3x3,or 4x4x4 or 7x7x7x7x7x7x7
    x = Input(input_shape)
    model = BatchNormalization(axis = 3)(x)
    
    model = Sequential()
    model.add(InputLayer(input_shape))
    model.add(BatchNormalization(axis = 3))
    
    model.add(Dense(9,use_bias=True,activation = 'relu'));
    model.add(Dense(9,use_bias=True,activation = 'relu'));
    model.add(Dense(9,use_bias=True,activation = 'relu'));
    model.add(Dense(9,use_bias=True,activation = 'relu'));
    model.add(Dense(9,use_bias=True,activation = 'relu'));
    model.add(Dense(9,use_bias=True,activation = 'relu'));
    
    model.add(Dense(1,use_bias=True,activation = 'softmax'));
    
    
    
    model.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])
    model.summary();
    
    

    
    return model;
    
    
    

def TrainAI(model):
    input_shape = (SIZE**D, 1, 1)#3x3,or 4x4x4 or 7x7x7x7x7x7x7
    x = Input(input_shape)
    #y = 
    import numpy as np
    model.fit(np.array({(1,2,1,2,1,2,0,1,0),(1,1,2,2,1,0,0,0,2),(1,1,0,1,2,2,0,0,2),(1,2,0,0,1,2,0,0,0),(1,2,2,2,1,1,1,0,2),(1,2,0,0,1,0,0,2,0),(1,2,1,1,2,0,2,0,0),(1,0,1,0,1,2,2,0,2),(2,0,1,0,2,0,1,2,1)}),{8,7,2,8,7,8,7,1,5});
    return model;
    
    

def CloseAI():
    return;




if __name__ == '__main__':
    import sys
    model =TrainAI(InitAI());
    sys.exit(0);

#!/usr/bin/env python



import tensorflow
import random
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

import numpy as numpy



def AIPlayerChoice(Matrix):
    
    
    global sess
    global model
    global RMAX
    
    if model == None:
        InitAI();
    
    
    
    init_op = tensorflow.global_variables_initializer();
    
    
    sess.run(init_op);
    
    grid = numpy.array([numpy.array(Matrix).ravel()]);
    
    prediction = model.predict(grid);
    
    return round(prediction[0][0]);
    



def InitAI():
    
    global model
    global input_shape
    global sess
    
    #print("Tensorflow Version: " + VERSION)
    print("TF.Keras Version" + tensorflow.keras.__version__)
    
    sess = tensorflow.Session();
    tensorflow.keras.backend.set_session(sess);
    
    
    model = Sequential()
    model.add(Dense(81,use_bias=True,activation = 'relu',input_dim=9));
    model.add(Dense(81,use_bias=True,activation = 'relu'));
    model.add(Dense(81,use_bias=True,activation = 'relu'));
    model.add(Dense(81,use_bias=True,activation = 'relu'));
    model.add(Dense(81,use_bias=True,activation = 'relu'));
    model.add(Dense(1,use_bias=True,activation = 'relu'));
    
    
    
    model.compile(optimizer='rmsprop', loss='mean_squared_error', metrics=['accuracy'])
    model.summary();
    
    model = TrainAI(model);
	
    
    return model;
    
    
    

def TrainAI(model):
    global input_shape
    
    #9x1x1,or 4x1x1
    x = Input(input_shape)
    
    #(1,1,2,2,1,0,0,0,2),(1,1,0,1,2,2,0,0,2),(1,2,0,0,1,2,0,0,0),(1,2,2,2,1,1,1,0,2),(1,2,0,0,1,0,0,2,0),(1,2,1,1,2,0,2,0,0),(1,0,1,0,1,2,2,0,2),(2,0,1,0,2,0,1,2,1)}),{8,7,2,8,7,8,7,1,5}
    import numpy as np
    
    samples = np.array(
            [
            
                [1,1,2,
                 2,1,0,
                 0,0,2],
                [1,1,0,
                 1,2,2,
                 0,0,2],
                [1,2,0,
                 0,1,2,
                 0,0,0],
                [1,2,2,
                 2,1,1,
                 1,0,2],
                [1,2,0,
                 0,1,0,
                 0,2,0]
                
            ]);
            
            
    moves = np.array([7,6,8,7,8])
    
    
    model.fit(samples, moves,epochs = 100,verbose = 2);
    return model;
    
def CloseAI():
    return;




if __name__ == '__main__':
    import sys
    import numpy as numpy
    global sess
    global model
    
    print("Init AI...");
    
    model = InitAI();
    
    test = [
            [1,1,2,2,1,0,0,0,2]
           ];
    
    
    print("Initializing all variables...");
    init_op = tensorflow.global_variables_initializer();
    
    
    sess.run(init_op);
    prediction = model.predict(numpy.array(test));
    print(prediction[0]);
    
    sys.exit(0);

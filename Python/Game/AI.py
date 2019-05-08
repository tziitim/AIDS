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





def AIPlayerChoice(Matrix):
    
    global model
    
    if model == None:
        print("Model is NONE, re-initing...");
        model = InitAI();
    
    #2d Matrix to ... THAT: [[[1,1,2,2,1,0,0,0,2]]]
    
    
    
    
    MatrixasTensor = tensorflow.convert_to_tensor([[[1,1,2,2,1,0,0,0,2]]]);
    
    if MatrixasTensor == None:
        print("Failed to convert Matrix to a tensor!");
        return None;
    
    return model(MatrixasTensor);
    



def InitAI():
    
    global model
    global input_shape
    global sess
    
    #print("Tensorflow Version: " + VERSION)
    print("TF.Keras Version" + tensorflow.keras.__version__)
    
    sess = tensorflow.Session();
    tensorflow.keras.backend.set_session(sess);
    
    
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
    
    
    #x = Input(input_shape)
    #model = BatchNormalization(axis = 3)(x)
    
    model = Sequential()
    model.add(InputLayer(input_shape))
    
    #model.add(tensorflow.keras.layers.Flatten)
    
    #model.add(BatchNormalization(axis = 3))
    
    //model.add(tensorflow.keras.layers.Flatten())
    
    model.add(Dense(9,use_bias=True,activation = 'relu'));
    model.add(Dense(9,use_bias=True,activation = 'relu'));
    model.add(Dense(9,use_bias=True,activation = 'relu'));
    model.add(Dense(9,use_bias=True,activation = 'relu'));
    model.add(Dense(9,use_bias=True,activation = 'relu'));
    model.add(Dense(9,use_bias=True,activation = 'relu'));
    
    #model.add(Dense(1,use_bias=True,activation = 'softmax'));
    
    
    
    model.compile(optimizer='rmsprop', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    model.summary();
    
    model = TrainAI(model);
	
    
    return model;
    
    
    

def TrainAI(model):
    global input_shape
    
    #9x1x1,or 4x1x1
    x = Input(input_shape)
    
    #(1,1,2,2,1,0,0,0,2),(1,1,0,1,2,2,0,0,2),(1,2,0,0,1,2,0,0,0),(1,2,2,2,1,1,1,0,2),(1,2,0,0,1,0,0,2,0),(1,2,1,1,2,0,2,0,0),(1,0,1,0,1,2,2,0,2),(2,0,1,0,2,0,1,2,1)}),{8,7,2,8,7,8,7,1,5}
    import numpy as np
    model.fit([[ [[[1,1,2,2,1,0,0,0,2]]] , [[[1,1,0,1,2,2,0,0,2]]] ]], [[ [[[8]]] , [[[7]]]  ]],epochs = 300,verbose = 1);
    return model;
    
def CloseAI():
    return;




if __name__ == '__main__':
    import sys
    
    global sess
    
    print("Init AI...");
    
    model = InitAI();
    
    test = [[[1,1,2,2,1,0,0,0,2]]];
    
    
    print("Initializing all variables...");
    tensorflow.global_variables_initializer();
    
    print("Converting model input to float32 version")
    floatingtest = tensorflow.cast(test,tensorflow.float32);
    
    print("Convert float32 model input to float32 matrix");
    MatrixasTensor = tensorflow.convert_to_tensor(floatingtest);
    
    print("Calling model");
    tensor = model(MatrixasTensor);
    
    
    if sess == None:
        print("Tensorflow session is null")
        sess = tensorflow.keras.backend.get_session();
        if sess == None:
            print("Keras backend session was also null!");
            sess = tensorflow.Session();
            if sess == None:
                print("SESS STILL NULL!!!! WHY DOST THOU DO THIS UNTO ME!!!")
                sys.exit(1);
        
    #print("Starting Coordinator");
    #coord = tensorflow.train.Coordinator()
    #print("Initailizing threads");
    #threads = tensorflow.train.start_queue_runners(sess=sess,coord=coord)
    
    print("Evaluating Tensor");
    output = tensor.eval(session=sess)
    
    #print("Requesting stop via Coordinator");
    #coord.request_stop();
    #print("Joining threads...");
    #coord.join(threads);
    
    print("Tensoflow did a thingity!!!!!! :)!!!!! " + str(output) + "\n");

    
    
    sys.exit(0);

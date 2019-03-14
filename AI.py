#!/usr/bin/env python



import tensorflow as tf
from tensorflow.keras import layers



def AIPlayerChoice():
    model();
	

def InitAI():
    print("Tensorflow Version: " + tf.VERSION)
    print("TF.Keras Version" + tf.keras.__version__)
    
    model = tf.keras.Sequential([#Use a seqention model to get an output from 0-(n^M)
        layers.Dense(64, activation = 'relu', inputshape = )
        
    

def CloseAI():
		

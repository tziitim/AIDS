#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  thingity.py
#  
#  Copyright 2019 Tim's Laptop <Tim's Laptop@LAPTOP-7R2QALN5>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  


from keras.models import Sequential
from keras.layers import InputLayer
from keras.layers import Dense, Input
from keras.layers.normalization import BatchNormalization

input_shape = (75, 75, 3)
x = Input(input_shape)
model = BatchNormalization(axis = 3)(x)

model = Sequential()
model.add(InputLayer(input_shape))
model.add(BatchNormalization(axis = 3))




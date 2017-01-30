#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 16:38:42 2017

@author: wangbeanz
"""
'''
This is a theano practice file.
Tutorial link: http://speech.ee.ntu.edu.tw/~tlkagk/courses/MLDS_2015_2/Lecture/Deep%20More%20(v2).ecm.mp4/index.html
'''

import theano
import theano.tensor as T
import numpy as np
import random

x = T.vector()
w = T.vector()
b = T.scalar()

z = T.dot(w, x) + b
y = 1 / (1 + T.exp(-z))

neuron = theano.function(
        inputs=[x, w, b],
        outputs=[y])

# we assume that we know the real w and b here.
w = [-1, 1]
b = 0
for i in range(100):
    x = [random.random(), random.random()]
    print(x)
    print(neuron(x, w, b))
    
    
# the model parameters are usually stored as shared variables.
x = T.vector()
# set the initial value of the shared variables.
w = theano.shared(np.array([1., 1.]))
b = theano.shared(0.)

z = T.dot(w, x) + b
y = 1 / (1 + T.exp(-z))

# the function can access the shared variables.
neuron = theano.function(
        inputs=[x],
        outputs=[y])

print(w.get_value())
w.set_value([0., 0.])

for i in range(100):
    x = [random.random(), random.random()]
    print(x)
    print(neuron(x))
    

# single neuron: training
x = T.vector()
w = theano.shared(np.array([-1., 1.]))
b = theano.shared(0.)

z = T.dot(w, x) + b
y = 1 / (1 + T.exp(-z))

neuron = theano.function(
        inputs=[x],
        outputs=[y])

y_hat = T.scalar()
cost = T.sum((y - y_hat) ** 2)  # define cost.

dw, db = T.grad(cost, [w, b])  # computing gradients

# declare a function for computing gradients.
# updates = "a list of pairs"
# Each pair is in the form of (shared-variable, an expression)
gradient = theano.function(
        inputs=[x, y_hat],
        updates=[(w, w-0.1*dw), (b,b-0.1*db)])

x = [1, -1]
y_hat = 1
for i in range(100):
    print(neuron(x))
    gradient(x, y_hat)
    print(w.get_value(), ', ', b.get_value())
    
    
    


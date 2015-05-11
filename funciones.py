# -*- encoding: utF-8 -*-
from math import cos
from math import pi

__author__ = 'Freddy'

def fun2(vector):
    d=4
    f2 = 10*d + sumatoria(vector)
    return f2
def sumatoria(v):
    s=0
    for i in range(1,5):
        s=s+(v[i-1]**2)-10*cos(2*pi*v[i-1])
    return s

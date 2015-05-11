# -*- encoding: utF-8 -*-
import random
from math import cos,sin
from math import pi
''' ok '''
__author__ = 'fredy'


def aleatorios(m,M,d):
    vector = []
    for i in range(d):
        vector.append(random.uniform(m,M))
    #print vector
    return vector

def evaluar(v):
    fx = 0.5 + (cos(sin(abs(v[0]**2-v[1]**2))-0.5))/((1+0.001*(v[0]**2+v[1]**2))**2)
    return fx

def Mutar(v,Q):
    hijo = []
    for i in range(len(v)):
        hijo.append(v[i]+random.uniform(0,1)*Q)
    return hijo
def comparar(ap_pa,ap_hijo):
    if ap_hijo<ap_pa:
        return True
    else:
        return False

def modificar_exitos(e,Q,n):
    float(e)
    float(Q)
    C=1
    if e/n == 0.5:
        return Q
    elif e/n < 0.5:
        return Q*C
    else:
        return Q/C

def main():
    generaciones = 10000
    d=2
    numerito = 20
    m=-100
    M=100
    padre=aleatorios(m,M,d)
    #Evaluar la función de X
    aptitud_padre=evaluar(padre)
    print "Padre: \n"+"Vector: "+ str(padre) + "\tAptitud: " + str(aptitud_padre)
    #sigma
    Q=0.1
    exitos = 0
    hijo = Mutar(padre,Q)
    aptitud_hijo = evaluar(hijo)
    print "Hijo: \n"+"Vector: "+ str(hijo) + "\tAptitud: " + str(aptitud_hijo)
    if comparar(aptitud_padre,aptitud_hijo):
        exitos  = exitos +1
        padre = hijo[:] #sustituimos al padre
        aptitud_padre=aptitud_hijo
    else:
        exitos = exitos
    g=0
    while g != generaciones:
        hijo = Mutar(padre,Q)
        aptitud_hijo = evaluar(hijo)
        if comparar(aptitud_padre,aptitud_hijo):
            exitos  = exitos +1
            padre = hijo[:] #sustituimos al padre
            aptitud_padre = aptitud_hijo
        else:
            padre = padre[:]
            aptitud_padre = aptitud_padre
            exitos = exitos
        if g%numerito ==0:
            Q=modificar_exitos(exitos,Q,numerito)
            exitos=0
        g = g+ 1
    print "Final: \n"+"Vector: "+ str(padre) + "\tAptitud: " + str(aptitud_padre)

main()
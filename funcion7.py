# -*- encoding: utF-8 -*-
import random
from math import sin,sqrt,cos
''' ok '''

__author__ = 'fredy'


def aleatorios(m,M,d):
    vector = []
    for i in range(d):
        vector.append(random.uniform(m,M))
    return vector

def sumatoria_dos(v,m):
    suma=0
    for i in range(1,m):
        suma = suma + (i*cos((i+1)*v[1]+i))
    return suma

def sumatoria_uno(v,m):
    suma=0
    for i in range(1,m):
        suma = suma + (i*cos((i+1)*v[0]+i))
    return suma

def evaluar(vector):
    m=6
    fx= - sumatoria_uno(vector,m) * sumatoria_dos(vector,m)

    return fx

def Mutar(v,Q):
    hijo = []
    for i in range(len(v)): hijo.append(v[i]+random.uniform(0,1)*Q)
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
    generaciones = 100000
    d=2
    numerito = 20
    m=-10
    M=10
    padre=aleatorios(m,M,d)

    #Evaluar la función de X
    aptitud_padre=evaluar(padre)
    print "Padre: \n"+"Vector: "+ str(padre) + "\tAptitud: " + str(aptitud_padre)
    #sigma
    Q=0.1
    exitos = 0
    hijo = Mutar(padre,Q)
    aptitud_hijo = evaluar(hijo)
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
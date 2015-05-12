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
    return vector
def sumatoria(v):
    sumi = 0
    a=[[-32,-16,0,16,32,-32,-16,0,16,32,-32,-16,0,16,32,-32,16,0,16,32,-32,-16,0,16,32],
       [-32,-32,-32,-32,-32,-16,-16,-16,-16,-16,0,0,0,0,0,16,16,16,16,16,32,32,32,32,32,]]
    for i in range(1,26):
        sumi = sumi + (1/(i+pow((v[0]-a[0][i-1]),6)+pow((v[1]-a[1][i-1]),6)))
    return sumi
def evaluar(v):
    fx = pow((0.002 + sumatoria(v)),-1)
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
    C=0.9
    if e/n == 0.5:
        return Q
    elif e/n < 0.5:
        return Q*C
    else:
        return Q/C
def Escribir(out,cadena):
    out.write(cadena)
    out.write('\n')
    print cadena

def main():
    outfile=open('funcion1.txt','w')
    a="--------------------Funcion 1-----------------------\n"
    Escribir(outfile,a)
    generaciones = 10000
    d=2
    numerito = 20
    m=-65.536
    M=65.536
    padre=aleatorios(m,M,d)
    #Evaluar la función de X
    aptitud_padre=evaluar(padre)
    a="Padre: \n"+"Vector: "+ str(padre) + "\tAptitud: " + str(aptitud_padre)
    Escribir(outfile,a)
    #sigma
    Q=0.9
    exitos = 0
    hijo = Mutar(padre,Q)
    aptitud_hijo = evaluar(hijo)
    #print "Hijo: "+ str(hijo) + "\tAptitud: " + str(aptitud_hijo)
    a="Hijo:"+ str(hijo) + "\tAptitud: " + str(aptitud_hijo)
    Escribir(outfile,a)
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
        a="Generacion: "+str(g)+" vector"+ str(padre) + "\tAptitud: " + str(aptitud_padre) +"  sigma: "+str(Q)
        #print "Generacion: "+str(g)+" vector"+ str(padre) + "\tAptitud: " + str(aptitud_padre) +"  sigma: "+str(Q)+"\n"
        Escribir(outfile,a)
    outfile.close()


main()
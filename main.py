# -*- encoding: utF-8 -*-
from decimal import Decimal

__author__ = 'Freddy'
import random
from funciones import *

def Sol_ale(min,max,tam):
    vector = []
    for i in range(tam):
        vector.append(random.uniform(min,max))
    return vector
def Evaluar(ale):
    fun=fun2(ale)
    return fun

def N(tam,Q):
    n=[]
    for i in range(tam):
        n.append(random.uniform(0,1)*Q)
    return n

def Mutar(ale,n):
    xi=[]
    for i in range(len(ale)):
        xi.append(ale[i]+n[i])
    return xi

def imprimir(g,v,a,e):
    print "Generacion:"+str(g)+"\tVector:"+str(v)+"\tAptitud:"+str(a)+"\tExitos:"+str(e)

def exitos(eo,ei,e):
    if len(ei)==0:
        return e
    elif ei<eo:
        return e+1

def comparar(eo,ei,E,xi,ale):
    #print "Padre: "+str(eo)+"\n"
    #print "Hijo: "+ str(ei)+"\n"
    if eo <ei:
        #print "Gano padre"
        return E,eo,ale
    else:
        #print "Gano Hijo"
        return E+1,ei,xi
def Modificar_Sigma(E,Q):
    var=5
    float(var)
    float(E)
    C=0.1
    if E/var == 0.2:
        #print "Se conserva Sigma\n"
        #print "Sigma anterior:" + str(Q) + "\tSigma nuevo:"+ str(Q)
        return Q
    elif E/var < 0.2:
        #print "Se multiplica Sigma"
        #print "Sigma anterior:" + str(Q) + "\tSigma nuevo:"+ str(Q*C)
        return Q*C
    elif E/var >0.2:
        #print "Se divide Sigma"
        #print "Sigma anterior:" + str(Q) + "\tSigma nuevo:"+ str(Q/C)
        return Q/C

def main():
    generaciones=100000
    d=0 #numero de veces que quiero que se verifique sigma
    maximo=10
    x=0
    Q=0.1 #Q = Sigma
    g=0 #generacion
    E=0
    tam = 4
    min=-5.12
    max=5.12
    #Generar numeros aleatorios del tamaño tam,
    ale=Sol_ale(min,max,tam)
    #Evaluar.
    eo=Evaluar(ale) #evaluacion inicial
    '''
    donde:
     g = numero de generación.
     ale = vector solucion aletorio
     eo = evaluación inicial 0
     E = numero de éxitos.
    '''
    imprimir(g,ale,eo,E)
    raw_input("Presiona enter para continuar...")
    #Establecer Q
    g=1
    while g!=generaciones:
        n=N(tam,Q)
        xi=Mutar(ale,n)
        #print "mutado:"+str(xi)+"\n"
        #print "\n"
        ei = Evaluar(xi)
        #print "evaluacion_mutado: "+str(ei)+"\n"
        E,eo,ale=comparar(eo,ei,E,xi,ale)
        #imprimir(g,ale,eo,E)
        if g % maximo== 0:
            #Modificar Sigma.
            Q=Modificar_Sigma(E,Q)
            E=0
        else:
            d=d+1
        g=g+1
        #raw_input("Espera")
    imprimir(g,ale,eo,E)

 #   while e!=10:2






main()

#Parametros
#aptitud
#N° Generación.
'''EE- miu, lambda
lambda <= miu
lambda <= miu


60 >= miu , lambda >=20

Viernes 8 de mayo estrategia evolutiva 1+1
'''
#### 7 mayo EE - 1+1 generar archivo lo mejor que se genera
### 14 mayo EEalpha estategia miu  + lambda
####29 Mayo imagenes blanco y negro

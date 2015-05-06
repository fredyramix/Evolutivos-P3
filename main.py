# -*- encoding: utF-8 -*-
__author__ = 'Freddy'
import random

def Sol_ale(min,max,tam):
    vector = []
    for i in range(tam):
        vector.append(random.uniform(min,max))
    return vector
def Evaluar(ale):
    x=sum(ale)
    fun = ((x**4)-(16*(x**2))+(5*x))/2
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
    if eo < ei:
        return E,eo,ale
    else:
        return E+1,ei,xi
def Modificar_Sigma(E,Q):
    var=5
    float(var)
    float(E)
    C=0.1
    if E/var == 0.2:
        print "Se conserva Sigma\n"
        print "Sigma anterior:" + str(Q) + "\tSigma nuevo:"+ str(Q)
        return Q
    elif E/var < 0.2:
        print "Se multiplica Sigma"
        print "Sigma anterior:" + str(Q) + "\tSigma nuevo:"+ str(Q*C)
        return Q*C
    elif E/var >0.2:
        print "Se divide Sigma"
        print "Sigma anterior:" + str(Q) + "\tSigma nuevo:"+ str(Q/C)
        return Q/C

def main():
    generaciones=10000
    x=0
    Q=0.1 #Q = Sigma
    g=0 #generacion
    E=0
    tam=int(raw_input("Ingrese el tamano del vector:\n"))
    print "Ingrese el intervalo:\n"
    min = int(raw_input("min:\n"))
    max= int(raw_input("max:\n"))
    #Generar numeros aleatorios del tamaño tam,
    ale=Sol_ale(min,max,tam)
    #Evaluar.
    eo=Evaluar(ale) #evaluacion inicial
    imprimir(g,ale,eo,E)
    raw_input("Espera")
    #Establecer Q
    d=0 #numero de veces que quiero que se verifique sigma
    while g!=generaciones:
        n=N(tam,Q)
        xi=Mutar(ale,n)
        ei = Evaluar(xi)
        E,e,x=comparar(eo,ei,E,xi,ale)
        g=g+1
        imprimir(g,x,e,E)
        if d == 19:
            #Modificar Sigma.
            Q=Modificar_Sigma(E,Q)
            d=0
            E=0
        else:
            d=d+1

 #   while e!=10:





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

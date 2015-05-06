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
def Modificar_Sigma():
    pass

def main():
    x=0
    Q=0.1 #Q = Sigma
    g=0 #generacion
    E=0
    tam=int(raw_input("Ingrese el tamano del vector:\n"))
    print "Ingrese el intervalo\n:"
    min = int(raw_input("min:\n"))
    max= int(raw_input("max:\n"))
    #Generar numeros aleatorios del tamaño tam,
    ale=Sol_ale(min,max,tam)
    #Evaluar.
    eo=Evaluar(ale) #evaluacion inicial
    imprimir(g,ale,eo,E)
    raw_input("Espera")
    #Establecer Q
    while g!=100:
        n=N(tam,Q)
        xi=Mutar(ale,n)
        ei = Evaluar(xi)
        E,eo,x=comparar(eo,ei,E,xi,ale)
        g=g+1
        imprimir(g,x,ei,E)
        if E == 10:
            #Modificar Sigma.
            Q=Modificar_Sigma()
            E=0


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

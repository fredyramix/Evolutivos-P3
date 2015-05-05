# -*- encoding: utF-8 -*-
__author__ = 'Freddy'
import random

def Sol_ale(min,max,tam,vector):
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


def main():
    x=0
    #Q = Sigma
    Q=0.1
    vector = []
    tam=int(raw_input("Ingrese el tamano del vector:\n"))
    print "Ingrese el intervalo\n:"
    min = int(raw_input("min:\n"))
    max= int(raw_input("max:\n"))
    #Generar numeros aleatorios del tamaño tam,
    ale=Sol_ale(min,max,tam,vector)
    #Evaluar.
    g=0
    E=0

    evaluado=Evaluar(ale)
    print "Generacion:"+str(g)+"\tVector:"+str(ale)+"\tAptitud:"+str(evaluado)+"\tExitos:"+str(E)
    raw_input("Espera")
    #Establecer Q
    n=N(tam,Q)
    xi=Mutar(ale,n)
    print "Elemento mutado:\n"
    print str(xi)

    print "Evaluar Hijo\n"
    evalhijo = Evaluar(xi)
    print str(evalhijo)



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

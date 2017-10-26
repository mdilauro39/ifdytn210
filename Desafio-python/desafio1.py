import random

def numram(a):
    contador=0
    lista=[]
    while contador < (a-1):
        numeros = random.randint(10,99)
        lista.append(numeros)
        contador=contador+1
    lista.append(random.randint(100,199))
    return lista

print numram(10)
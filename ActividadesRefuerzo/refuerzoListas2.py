import random

lista1= list()
lista2= list()
lista3= list()
lista4= list()
lista5= list()


def llenar_lista():
    lista = list()
    cont = 20
    while (len(lista)) < cont:
        lista.append(random.randint(0, 9))
    return lista

def calcular_ventanas(lista):
    cont=1
    recorrido=0
    while recorrido <= (5*cont)-1:
        cont+=1

lista1=llenar_lista()
lista2=llenar_lista()
lista3=llenar_lista()
lista4=llenar_lista()
lista5=llenar_lista()



print(lista1)
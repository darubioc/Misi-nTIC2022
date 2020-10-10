import random

lista1= list()
lista2= list()
lista3= list()
lista4= list()
lista5= list()
promsAzules = list()
promsVerdes = list()
promsNaranja = list()
promsGris = list()

def llenar_lista():
    lista = list()
    cont = 20
    while (len(lista)) < cont:
        lista.append(random.randint(0, 9))
    return lista

def calcular_ventanas(lista,ventana):
    rango=ventana
    cont=1
    prom=0 
    recorrido=0
    sumat=0
    while  cont*rango<=len(lista):
        while recorrido <= (rango*cont)-1:
            sumat+=lista[recorrido]
            recorrido+=1
        prom=sumat/rango
        if cont==1:
            promsAzules.append(prom)
        elif cont==2:
            promsVerdes.append(prom)
        elif cont==3:
            promsNaranja.append(prom)
        elif cont==4:
            promsGris.append(prom)
        sumat=0
        prom=0
        cont+=1

lista1=llenar_lista()
lista2=llenar_lista()
lista3=llenar_lista()
lista4=llenar_lista()
lista5=llenar_lista()

calcular_ventanas(lista1,5)
calcular_ventanas(lista2,5)
calcular_ventanas(lista3,5)
calcular_ventanas(lista4,5)
calcular_ventanas(lista5,5)
print(lista1)
print(promsAzules,promsVerdes,promsNaranja,promsGris)

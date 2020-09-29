import random
lista = [0]
lista_copia =[-1]
#Creación de método que llenará la lista de manera manual o automática con números al azar
def llenar_lista():
    ciclo=True
    cont = 0
    while ciclo:
        llenado = input("Digite 1 si desea llenar la lista manualmente. \n"
                        "Digite 2 si desea generar numeros aleatorios.\n\n")

        if llenado =="1":
            control_valor=True
            while control_valor:
                valr = int(input("Digite un valor entre 0 y 9 para añadir a la lista.\n"+
                             "Digite -1 para terminar el llenado manual de la lista."))
                if valr>=0 & valr<=9:
                    #Momento específico donde agregamos valores manualmente haciendo uso de .append(x)
                    lista.append(valr)
                    cont +=1
                    print("Hay "+ str(len(lista)) + " elementos en la lista.")
                elif valr == -1:
                    control_valor=False
                else:
                    print("Digite un valor válido (entre -1 y cont=09)")
            ciclo = False

        elif llenado =="2":
            print(len(lista))
            if len(lista) > 1:
                tam_old=len(lista)
                tam = int(input("¿Cuántos valores desea agregar a la lista?"))
                while (len(lista)) <= tam_old+tam:
                    lista.append(random.randint(0, 9))
            else:
                tam = int(input("¿Cuántos valores desea para la lista?"))
                while int(len(lista))<=tam-1:
                    lista.append(random.randint(0,9))
            ciclo = False

        else:
            print("Digite un valor  valido..")



def ver_listas():
    print("\nLa lista base:")
    print(lista)

    print("\nLa lista copia:")
    print(lista_copia)

def eliminar_todo():
    for i in range(len(lista)):
        print(lista)
        del(lista[0])

def ordenar():
    op = int(input("Digite 1 si desea en orden creciente o 2 para decreciente"))
    if op ==1:
        lista.sort()
    elif op ==2:
        lista.sort(reverse=True)
    else:
        print("La opción digitada no fue válida.")

def busqueda(n):
    #Buscamos el parámetro en la lista, de no estar devolvemos -1
    if n in lista:
        return lista.index(n)
    else:
        return -1


#Función principal, ciclo while para simular el menú
while True:
    opcion = input("\nDigite el entero de su elección: \n"
                   "1 : Crear lista o agregar elementos.\n"
                   "2 : Ver lista.\n"
                   "3 : Eliminar todos los valores.\n"
                   "4 : Ordenar.\n"
                   "5 : Buscar valores.\n"
                   "6 : Extracción de elementos en lista base hacia copia.\n"
                   "7 : Invertir elementos.\n"
                   "8 : Copiar lista.\n"
                   "9 : Contar elementos.\n"
                   "10 : Insertar elementos.\n"
                   "11 : Unir la lista copia a la lista base.\n"
                   "12 : Seek & destroy (Destruye el primer elemento encontrado).\n"
                   "13 : Salir.\n\n"
                   )

    if opcion == "1":
        llenar_lista()

    elif opcion == "2":
        ver_listas()

    elif opcion == "3":
        eliminar_todo()
        print("Lista base limpiada, pulse una tecla para eliminar.")

    elif opcion == "4":
        ordenar()

    elif opcion == "5":
        busq = int(busqueda(int(input("Digite el valor entero a buscar en el arreglo: "))))
        if  busq>=0:
            print("La posición del valor en el arreglo es: "+str(busq))
        elif busq==-1:
            print("El valor dado no existe en el arreglo.")
        else:
            print("Opción no válida.")


    elif opcion == "6":
        busq = int(busqueda(int(input("Digite el valor entero a buscar en el arreglo: "))))
        if busq >= 0:
            print("La posición del valor en el arreglo es: " + str(busq))
            if lista_copia[0]==-1:
                #Eliminamos de la lista el valor en la posición del arreglo y lo devolvemos para
                #asignarle el primer valor a la lista_copia
                lista_copia[0]=lista.pop(busq)
            else:
                #Eliminamos de la lista el valor de la posición 'busq' y la retorna para añadir
                #dicho valor a la lista_copia
                lista_copia.append(lista.pop(busq))
        elif busq == -1:
            print("El valor dado no existe en el arreglo.")
        else:
            print("Opción no válida.")

    elif opcion == "7":
        lista.sort(reverse=True)

    elif opcion == "8":
        lista_copia=lista.copy()

    elif opcion == "9":
        print("La lista base tiene: "+str(len(lista))+" elementos")

    elif opcion == "10":
        lista.insert(int(input("Digite la posición donde desea insertar el elemento.")),
                     int(input("Digite el valor de 0 a 9 que desea insertar.")))

    elif opcion == "11":
        lista.extend(lista_copia)

    elif opcion == "12":
        busq = int(input("Digite el valor entero que desea destruir: "))
        if busq in lista:
            lista.remove(busq)
        else:
            print("El elemento no está en la lista")

    elif opcion == "13":
        break

    else:
        print("Digita un valor válido")
    input("Pulse enter para continuar...")
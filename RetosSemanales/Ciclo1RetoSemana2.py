#Diego Andres Rubio Casallas C.C.: 1032493492
datos=[
    ["Francisco Mesa", 32, 3, 'M',0, 0.0],
    ["Juan Juzga",45,2,'M',0, 0.0],
    ["Ines Marin", 68, 4, 'F',0, 0.0],
    ["Julio Calderon", 23, 3, 'M',0, 0.0],
    ["Clara Arias", 35, 1, 'M', 0, 0.0],
    ["Daniel Rodriguez", 56, 2, 'M', 0, 0.0],
    ["Claudia Buitrago", 75, 3, 'M', 0, 0.0],
    ["Fernando Sanchez", 87, 1, 'M', 0, 0.0],
    ["David Robledo", 43, 1, 'M', 0, 0.0],
    ["Marta Aldana", 53, 4, 'M', 0, 0.0],
    ["Paula Barreto", 22, 2, 'M', 0, 0.0],
    ["Ana Cañon", 18, 3, 'M', 0, 0.0],
    ["Lizeth Puentes", 62, 1, 'M', 0, 0.0],
    ["Deicy Castillo", 34, 2, 'M', 0, 0.0],
    ["Lorena Saenz", 71, 4, 'M', 0, 0.0]
]
salariosCopia=list()
edadesCopia=list()
salario=877802

def calcular_salarios():
    i=0
    for i in range(len(datos)):
        datos[i][4]=datos[i][2]*salario

def imprimir():
    imp = ""
    for i in range(len(datos)):
        imp+=str(i+1)+". "
        for j in range(6):
            imp+=(str(datos[i][j])+"\t")
        print(imp)
        imp=""

def porcentajesSalarios():
    i = 0
    total = 0
    for i in range(len(datos)):
        total+=datos[i][4]
    print("El total de la nómina de la compañía es: "+str(total))
    i = 0
    for i in range(len(datos)):
        datos[i][5] = str(round((datos[i][4]/total)*100,2))+"%"
def ordenarnombre():
    datos.sort(key=lambda x:x[0])
def copiarSalarios():
    global salariosCopia
    for i in range(len(datos)):
        salariosCopia.append(datos[i][4])
    salariosCopia.sort()
    print(salariosCopia)
    print("El menor salario es: "+str(salariosCopia[0])+"\nEl mayor salario es: "+str(salariosCopia[14]))

def copiarEdad():
    global edadesCopia
    for i in range(len(datos)):
        edadesCopia.append(datos[i][1])
    edadesCopia.sort()
    print(edadesCopia)
    print("La menor edad es: "+str(edadesCopia[0])+"\nLa mayor edad es: "+str(edadesCopia[14]))


calcular_salarios()
porcentajesSalarios()
imprimir()
print("\nOrdenada por nombre:")
ordenarnombre()
imprimir()
print("\nOrdenada por salarios (menor a mayor)")
copiarSalarios()
print("\nOrdenada por edades (menor a mayor)")
copiarEdad()
#print(datosCopia)



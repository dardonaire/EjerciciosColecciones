
sw = 1
listaNotas = []   #Aca se crea una lista vacia llamada listanotas. Aqui es donde se iran guardando todas las notas que el usuario ingrese

print("Presione 1 para ingresar notas")
print("Presione cualquier tecla para salir")
op = int(input("Seleccione opción: "))
if(op == 1):
    while sw == 1:
        try:
            print("--" * 30)
            nota = int(input("Incorpore su nota, si desea salir, presione 0: "))   
        
            if (nota != 0):
                listaNotas.append(nota) #Cada vez que el usuario ingresa una nueva nota valida (por ejemplo un 7)
                #listaNotas.append(7) toma ese numero y lo guarda en una lista. Si la lista tenia [5,6], después del append
                #quedará como [5,6,7]

                print(f"Sus notas cargadas son: {listaNotas}")
                print(f"Cantidad de notas cargadas: {len(listaNotas)}") #Si tu lista tiene las notas [5,6,7], al ejecutar len(listanotas)
                #el resultado sera 3, por que hay exactamente tres notas cargadas
                print(f"Su promedio de notas es: {sum(listaNotas)/len(listaNotas)}") #La funcion sum toma los numeros adentro de la lista y los suma entre si. Si la lista tiene
                #[5,6,7], sum() hara la operacion 5 + 6 + 7, devolviendote un total de 18
                #le cuenta cuantas notas hay, en el caso del ejemplo son 3
                #el / divide el resultado de la suma por el total de elementos

            else:
                print("Adios")
                sw = 0

        except ValueError:
            print("Error ingrese número")   

else:
    print("Adios")
    sw = 0
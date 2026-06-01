
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
                listaNotas.append(nota)
                print(f"Sus notas cargadas son: {listaNotas}")
                print(f"Cantidad de notas cargadas: {len(listaNotas)}")
                print(f"Su promedio de notas es: {sum(listaNotas)/len(listaNotas)}")

            else:
                print("Adios")
                sw = 0

        except ValueError:
            print("Error ingrese número")   

else:
    print("Adios")
    sw = 0
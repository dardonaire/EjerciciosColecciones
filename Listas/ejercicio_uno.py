
sw = 1
listaNotas = []

print("Presione 1 para ingresar notas")
print("Presione cualquier tecla para salir")
op = int(input("Seleccione opción"))
if(op == 1):
    while sw == 1:
        try:
            print("--" * 30)
            nota = int(input("Incorpore su nota, si desea salir, presione 0: "))
        
            if (nota != 0):
                listaNotas.append(nota)
                print(f"Sus notas cargadas son: {listaNotas}")

            else:
                print("Adios")
                sw = 0

        except ValueError:
            print("Error ingrese número")   

else:
    print("Adios")
    sw = 0
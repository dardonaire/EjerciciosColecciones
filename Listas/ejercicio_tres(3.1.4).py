curso = []

print("Presione 1 para ingresar alumno")
print("Presione cualquier otra tecla para salir")

op = input("Ingrese opcion: ")

if op == "1":
    contador = 0
    opc = ""
    while opc != "n" and contador < 30:

        nombre = input("Ingrese el nombre del alumno: ")
        direc = input("Ingrese la dirección del alumno: ")
        tel = input("Ingrese el teléfono del alumno: ")

        alumno = [nombre, direc, tel]
        curso.append(alumno)
        contador += 1

        if contador == 30:
            opc = "n"
            print("")
        else:
            opc = input("Desea agregar otro alumno (s/n): ")
            print("")
        for alum in curso:
            print(f"Nombre: {alum} ")

        
        
        
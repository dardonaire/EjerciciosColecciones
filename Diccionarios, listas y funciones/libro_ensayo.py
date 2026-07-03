
def mostrar_menu():
    print("======== MENÚ PRINCIPAL =====")
    print("1. Agregar libro ")
    print("2. Buscar libro ")
    print("3. Elimnar libro ")
    print("4. Registrar préstamos")
    print("5. Mostrar libros")
    print("6. Salir")
    print("==============================")

def opcion_selec():
    while True:
        try:
            op = int(input("Seleccione opcion: "))
        except ValueError:
            print("Ingrese opcion entre 1 y 6")

def agregar_libro(lista):
    titulo = input("Ingrese nombre del libro")
    if not validar_texto(titulo):
        print("Error, no puede estar en blanco")
        return
    autor = input("Ingrese autor: ")

    if not validar_texto(autor):
        print("Error, no puede estar en blanco")
        return
    while True:
        try:
            anio = int(input("Ingrese año del libro:  "))
            if  not validar_anio(anio):
                print("Error, el año debe estar entre 1000 y 2025")
                return
        except ValueError:
            print("Error, el año debe estar entre 1000 y 2025")
            return
        break
    
    libro = {
        "titulo" : titulo.strip(),
        "autor" : autor.strip(),
        "anio" : anio,
        "prestado" : False

    }

    libros.append(libro)
    print(f"libro {titulo} agregado con exito ")

def validar_texto(valor):
    return len(valor.strip()) > 0

def validar_anio(valor):
    return 1000 <= valor <= 2025

def buscar_libro(libros, titulo):
    for i, libro in enumerate(libros):
        if libro["titulo"] == titulo:
            return i

    return -1
def registrar_prestamo(libros):
    for libro in libros:
        if libro["anio"] >= 2000:
            libro["prestado"] = True
        else:
            libro["prestado"] = False

def mostrar_libros(libros): #Aca verificar q la lista no este vacia
    registrar_prestamo(libros)
    if len(libros) == 0:
        print("No se encuenran libros registrados")
        return
    print("==== Lista de libros ====")
    for libro in libros:
        print(f"Titulo: {libro['titulo']}")
        print(f"Autor: {libro['autor']}")
        print(f"Año: {libro['anio']}")

    if libro["prestado"]:
        print("Estado: Disponible para prestamo")
    else:
        print("Estado: Solo consulta en sala")
            

#Codigo principal
libros = []
while True:
    mostrar_menu()

    op = opcion_selec ()
    if op == 1:
        agregar_libro(libros)

    elif op == 2:
        titulo_buscar = input("Ingrese titulo a buscar: ")
        pos = buscar_libro(libros, titulo_buscar)
        if pos != -1:
            libro = libros[pos]
            print(f"Nombre del libro: {libro['titulo']}")
            print(f"Autor: {libro['autor']}")
            print(f"Año: {libro['anio']}")
            print(f"Estado: {libro['prestado']}")
        else:
            print(f"El libro {titulo_buscar} no se encuentra registrado")
        
    elif op == 3:
        titulo = input("Ingrese libro a eliminar")
        pos = buscar_libro(libros, titulo)
        if pos != -1:
            libros.pop(pos)
            print(f"Libro {titulo} eliminado con exito")
        else:
            print(f"El libro {titulo} no se encuentra registrado")

    elif op == 4:
        registrar_prestamo(libros)
    
    elif op == 5:
        mostrar_libros(libros)
    
    elif op == 6:
        print("Gracias por ocupar el registro")
        break
         
    else:
        print("Ingrese opcion entre 1 y 6")
    
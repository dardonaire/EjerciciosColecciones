
def menu_mostrar ():
    print("===== Lista de productos ====")
    print("1. Agregar libro")
    print("2. Buscar libro")
    print("3. Eliminar libro")
    print("4. Registrar préstamos")
    print("5. Mostrar libros")
    print("6. Salir")

def selec_op():
    while True:
        try:
            op =  int(input("Seleccione opción: "))
            if op < 0 or op > 6:
                print("Error, ingrese opción válida")
            else:
                return op
        except ValueError:
            print("error")
def validar_titulo(titulo):
    if titulo.strip() == "":
        return False
    else:
        return True

def validar_autor(autor):
    if autor.strip() == "":
        return False
    else:
        return True
def validar_anio(anio):
    try:
        anio = int(anio)
        if anio > 2025 and anio < 1000:
            return False
        else:
            return True
    except ValueError:
        return False

def agregar_libro(lista):
    titulo = input("Ingrese titulo del libro: ")
    autor = input("Ingrese autor del libro: ")
    anio = int(input("Ingrese año del libro: "))

    titulo_valido = validar_titulo(titulo)
    autor_valido = validar_titulo(autor)
    anio_valido = validar_anio(anio)

    if titulo_valido == True and autor_valido == True and anio_valido == True:
        libros = {
            "titulo" : titulo,
            "autor" : autor,
            "anio" : int(anio),
            "estado": False
        }

        lista.append(libros)
        print("Libro agregado con exito")
    else:
        print("El producto no se pudo registrar")

def buscar_libro(lista, titulo ):
    for indice, libro in enumerate (lista): #por cada posicion, y articulo en la lista enumerada (lista)
        if libro ["titulo"] == titulo:
            return indice
    return -1 # Si no encuentra devolver -1
    
    

    
#====Codigo principal===
lista_libros = []
while True:
    menu_mostrar()

    opcion_elegida = selec_op()

    if opcion_elegida == 1:
        agregar_libro(lista_libros)

    elif opcion_elegida == 2:

        titulo_buscado = input("Ingrese el titulo del nombre que desea buscar: ")
        posicion = buscar_libro(lista_libros, titulo_buscado) #posicion es el numero del dicionario junto con todos sus datos

        if posicion != -1:
            print(f"El libro se encontro en la posicion {posicion}")

            libro_encontrado = lista_libros[posicion]

            print(f"Titulo: {libro_encontrado['nombre']}")
            print(f"Autor: {libro_encontrado['autor']}")
            print(f"Año: {libro_encontrado['anio']}")

            if libro_encontrado['estado']:
                print("Estado: Disponible para prestamo")
            else:
                print("Estado: Solo consulta en sala")
            
        else:
            print(f"EL libro {titulo_buscado} no se encuentra registrado")
            
    elif opcion_elegida == 3:

        libro_eliminar = input("Ingrese libro a eliminar: ")

        posicion = buscar_libro(lista_libros, libro_eliminar)

        if posicion != -1:
            lista_libros.pop(posicion)
            print(f"Libro {libro_eliminar} eliminado con exito")
        else:
            print(f"El libro {libro_eliminar} no se encuentra registrado")





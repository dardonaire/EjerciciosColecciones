
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
            "ano" : anio,
            "disponible": False
        }

        lista.append(libros)
        print("Libro agregado con exito")
    else:
        print("El producto no se pudo registrar")

def buscar_producto(lista, nombre ):
    for posicion, libro in enumerate (lista):
        if posicion -1

    
#====Codigo principal===
lista_libros = []
while True:
    menu_mostrar()

    opcion_elegida = selec_op()

    if opcion_elegida == 1:
        agregar_libro(lista_libros)

    elif opcion_elegida == 2:
        titulo_buscado = input("Ingrese el titulo del nombre que desea buscar: ")
        posicion = buscar_libro(lista_libros, titulo_buscado)



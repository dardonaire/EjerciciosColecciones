def mostrar_menú():
    print("=========MENÚ PRINCIPAL=======")
    print("1.Agregar Producto")
    print("2. Buscar producto")
    print("3. Eliminar producto")
    print("4. Actualizar disponibilidad")
    print("5. Mostrar productos")
    print("6. Salir")

def selec_op():
    while True:
        try:
            op = int(input("Seleccione una opción: "))
            if op > 6 or op < 0:
                print("Ingrese un número entre 1 y 5")
            else:
                return op
        except ValueError:
            print("Ingrese un número")

def validar_nombre(nombre):
    if nombre.strip() == "":
        return False
    else:
        return True

def validar_precio(precio):
    try:
        precio == float(precio)
        if precio <= 0:
            return False
        else:
            return True
    except ValueError:
        return False
    
def validar_stock(stock):
    try:
        stock == int(stock)
        if stock < 0:
            return False
        else:
            return True
    except ValueError:
        return False

def agregar_producto(lista):
    
    nombre_producto = input("Ingrese nombre del producto: ")
    
    precio_producto = float(input("Ingrese precio del producto: "))

    stock_producto = int(input("Ingrese stock del producto: "))

    posicion = buscar_producto(lista, nombre_producto)

    if posicion != -1:
        print("Producto ya existente")
        return
    
    nombre_valido = validar_nombre(nombre_producto)

    precio_valido = validar_precio(precio_producto)

    stock_valido = validar_stock(stock_producto)
    
    if nombre_valido == True and precio_valido == True and stock_valido == True:
        productos = {
            "nombre": nombre_producto,
            "precio" : precio_producto,
            "stock" : stock_producto,
            "disponible" : False
        }

        lista.append(productos)
        print("Producto agregado correctamente")
    else:
        print("El producto no cumple alguna condición")

def buscar_producto(lista, nombrebuscado):
    for posicion, producto in enumerate (lista): #producto es el diccionario
        if producto ["nombre"] == nombrebuscado:
            return posicion
    return -1

def actualizar_producto(lista):
    for producto in lista:
        if producto["stock"] > 0:
            producto["disponible"] = True
        else:
            producto["disponible"] = False
def mostrar_producto(lista):
    if len(lista) == 0:
        print("No hay productos registrados")
        return
    actualizar_producto(lista)

    print("=== Lista de productos ===")
    for producto in lista:
        print(f"Nombre: {producto['nombre']}")
        print(f"Precio: {producto['precio']} ")
        print(f"Stock: {producto['stock']}")

        if producto["disponible"]:
            print("Estado: Disponible")
        else:
            print("Estado: Sin stock")


#********Codigo Principal*********
lista_productos = []

while True:

    mostrar_menú()

    opcion_elegida = selec_op()

    if opcion_elegida == 1:

        agregar_producto(lista_productos)
    
    elif opcion_elegida == 2:

        producto_buscar = input("Ingrese producto a buscar: ")

        posicion = buscar_producto(lista_productos, producto_buscar)

        if posicion != -1:
            print(f"Producto {producto_buscar} fue encontrado en la posición {posicion}") 

            producto_encontrado = lista_productos[posicion]

            print(f"Nombre: {producto_encontrado['nombre']}")  
            print(f"Precio: {producto_encontrado['precio']}")  
            print(f"Stock:  {producto_encontrado['stock']}")

            if producto_encontrado['disponible']:
                print("Esta dosponible?: Si esta disponible ")
            else:
                print("Esta disponible?: No esta disponible")
        else:
            print(f"El producto {producto_buscar} no esta registrado")

    elif opcion_elegida == 3:
        productoeliminar = input("Ingrese producto a eliminar: ")

        posicion = buscar_producto(lista_productos, productoeliminar)

        if posicion != -1:
            lista_productos.pop(posicion)

            print(f"Producto {productoeliminar} eliminado con existo")
        else:
            print(f"Producto {productoeliminar} no encontrado")
    
    elif opcion_elegida == 4:
        actualizar_producto(lista_productos)
    
    elif opcion_elegida == 5:
        mostrar_producto(lista_productos)
    
    elif opcion_elegida == 6:
        print("Gracias por usar el sistema de inventario. Hasta pronto")
        break



'''
"Mouse": [10, 15000]
"Teclado": [5, 25000]
"Monitor": [3, 180000]
'''

def agregar_producto(productos):

    nombre_producto = input("Ingrese nombre de producto: ")
    if len(nombre_producto) <= 0:
        print("El nombre del producto no puede estar vacio")
        return
    if nombre_producto in productos:
        print("Producto ya existente")
        return
    
    while True:
        try:
            stock_producto = int(input("Ingrese stock: "))
            break
        except ValueError:
            print("Error, deber ser numeros ")

    if stock_producto < 0:
        print("Error, debe ser un número mayos o igual a 0")
        return
    
    while True:
        try:
            precio_producto = int(input("Ingrese precio del producto: "))
            break
        except ValueError:
            print("Error, deber ser numeros ")

    if precio_producto <= 0:
        print("Error, el precio debe ser mayor a 0")
        return
    else:
        productos[nombre_producto] = [stock_producto, precio_producto]
        print("Producto agregado correctamente")

def mostrar_productos(productos):
    
    print(productos [0][1][2])

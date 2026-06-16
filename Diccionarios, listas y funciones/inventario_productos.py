import funciones_inventario as fni

productos = {}

while True:
    print("==========Menú Principal=========")
    print("=" * 30)
    print("!. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Producto más caro")
    print("5. Salir")
    print("=" * 30)

    while True:
        try:
            op= int(input("Seleccione opción: "))
            break
        except ValueError:
            print("Error, ingrese opcion entre 1 y 5")
        
    if op == 1:
        fni.agregar_producto(productos)
    elif op == 2:
        fni.mostrar_productos(productos)
        
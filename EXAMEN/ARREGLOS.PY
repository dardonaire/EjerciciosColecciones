
def leer_opcion():
    while True:
            print("========== MENÚ PRINCIPAL ==========") 
            print("1. Unidades por tipo de arreglo")
            print("2. Búsqueda de arreglos por rango de precio")
            print("3. Actualizar precio de arreglo")
            print("4. Agregar arreglo")
            print("5. Eliminar arreglo")
            print("6. Salir")
            print("=====================================")

    
            try:
                op = int(input("Ingrese opcion seleccionada: "))
                if op <= 0 or op > 6:
                    print("Debe seleccionar una opción válida")
                else:
                    return op
                    print("Debe seleccionar una opción válida")

            except ValueError:
                print("Debe seleccionar una opción válida")

def validar_texto(texto):
    return len(texto.strip()) > 0
            
def unidades_tipo(tipo_buscado, dicc_arreglos, dicc_bodega):
    tipo_buscado = tipo_buscado.strip().lower()
    contador_arreglos = 0

    for codigo_arreglo, datos in dicc_arreglos.items():
        if tipo_buscado == datos[1]:
            for codigo_arreglo_bodega, datos_bodega in dicc_bodega.items():
                if codigo_arreglo == codigo_arreglo_bodega:
                    contador_arreglos += datos_bodega[1]
                    break
    
    print(f"La cantidad de arreglos del tipo {tipo_buscado} es {contador_arreglos}")


def busqueda_precio(p_min,p_max,dicc_arreglos, dicc_bodega):

    lista_arreglos_precio = []

    for codigo_arreglo_bodega, datos_bodega in dicc_bodega.items():
        precio = datos_bodega[0]
        if precio <= p_max and precio >= p_min and datos_bodega[1] > 0:
            for codigo_arreglo, datos_arreglo in dicc_arreglos.items():
                if codigo_arreglo == codigo_arreglo_bodega:
                    lista_arreglos_precio.append(f"{datos_arreglo[0]} -- {codigo_arreglo}")
                    break
    
    if len(lista_arreglos_precio) > 0:
        lista_arreglos_precio.sort()

        for arreglo in lista_arreglos_precio:
            print(arreglo)
    else:
        print("No hay arreglos en ese rango de precios")


#CÓDIGO PRINCIPAL
arreglos = {
            'FLO1': ['Ramo Primavera', 'ramo', 'rosado', 'M', True,'primavera'],
            'FLO2': ['Caja Elegante', 'caja', 'blanco', 'L', True, 'todoaño'],
            'FLO3': ['Ramo Solar', 'ramo', 'amarillo', 'S', False, 'verano'],
            'FLO4': ['Centro Mesa', 'centro', 'rojo', 'M', True, 'todo año'],
            'FLO5': ['Ramo Bosque', 'ramo', 'verde', 'L', False, 'otoño'],
            'FLO6': ['Caja Noche', 'caja', 'morado', 'M', True, 'invierno'],
            }

bodega = {
        'FLO1': [15990, 8],
        'FLO2': [29990, 3],
        'FLO3': [9990, 12],
        'FLO4': [24990, 5],
        'FLO5': [19990, 0],
        'FLO6': [22990, 6],
        }

while True:

        op_selec = leer_opcion()

        if op_selec == 1:
            tipo_buscar = input("Ingrese tipo de arreglo: ")
            unidades_tipo(tipo_buscar, arreglos, bodega)

        elif op_selec == 2:
            try:
                precio_minimo = int(input("Ingrese precio minimo a buscar: "))
                precio_maximo = int(input("Ingrese precio mayor a buscar: "))
                if precio_minimo >= 0 and precio_maximo >= 0 and precio_minimo <= precio_maximo:
                    busqueda_precio(precio_minimo,precio_maximo,arreglos,bodega)
                else:
                    print("Debe ingresar valores enteros")
            except ValueError:
                print("Debe ingresar valores enteros")

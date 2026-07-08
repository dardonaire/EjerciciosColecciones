
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
            op = int(input("Ingrese opcion: "))
            if op <= 0 or op > 6:
                print("Nopo weon, como s te ocurre")
            else:
                return op
        except ValueError:
                print("Nopo weon, como s te ocurre")

def unidades_tipo(tipo_buscar,dicc_arreglos,dicc_bodega):
  
    contador_arreglos = 0
    for codigo in dicc_arreglos:
        datos_arreglo = dicc_arreglos[codigo][1]
        if datos_arreglo == tipo_buscar.strip().lower():
            unidades = dicc_bodega[codigo][1]
            contador_arreglos += unidades

    if contador_arreglos == 0:
        print("No hay arreglos disponibles")
    else:
        print(f"El total de tipos de arreglo {tipo_buscar} es de {contador_arreglos}")
    
def busqueda_precio(p_minimo, p_maximo, dicc_arreglos, dicc_bodega):
    lista_arreglos = []
    try:

        p_minimo = int(p_minimo)
        p_maximo = int(p_maximo)
        
        for codigo in dicc_bodega:
            precio = dicc_bodega[codigo][0]
            unidades = dicc_bodega[codigo][1]
            if p_minimo <= precio <= p_maximo and unidades != 0:
                lista_arreglos.append(f"{dicc_arreglos[codigo][0]} -- {codigo}")
            
        
        if len(lista_arreglos) == 0:
            print("No hay arreglos en ese rango de precios")
        else:
            lista_arreglos.sort()
            print(f"Los arreglos encontrados son: {lista_arreglos}")

    except ValueError:
        print("ingrese valores entero")

def buscar_codigo(codigo,dicc_bodega):
    

        

#Codigo principal

arreglos = {
            'FLO1': ['Ramo Primavera', 'ramo', 'rosado', 'M', True,'primavera'],
            'FLO2': ['Caja Elegante', 'caja', 'blanco', 'L', True, 'todo año'],
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
    op = leer_opcion()

    if op == 1:
        tipo_arreglo = input("Ingrese tipo de arreglo: ").strip().lower()
        unidades_tipo(tipo_arreglo,arreglos,bodega)
    elif op == 2:
        while True:
                precio_minimo = input("Ingrese precio minimo: ").strip()
                precio_maximo = input("Ingrese precio maximo: ").strip()
                try:
                    precio_minimo = int(precio_minimo)
                    precio_maximo = int(precio_maximo)
    
                    busqueda_precio(precio_minimo, precio_maximo, arreglos, bodega)
                    break
                
                except ValueError:
                    print("Debe ingresar valores enteros")
    elif op == 3:
        codigo_arreglo = input("Ingrese codigo nuevo: ").strip().upper()
        nuevo_precio = input("Ingrese nuevo precio: ").strip()
            
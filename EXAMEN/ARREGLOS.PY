
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

def buscar_codigo(codigo,dicc_bodega):

    for codigo_bodega in dicc_bodega.keys():
        if codigo == codigo_bodega:
            return True
    return False

def actualizar_precio(codigo_buscado, nuevo_precio,dicc_bodega):
    if buscar_codigo(codigo_buscado,dicc_bodega):
        lista_datos = dicc_bodega[codigo_buscado]
        lista_datos[0] = nuevo_precio
        return True
    else:
        return False

def validar_texto(texto):
    if len(texto.strip()) > 0:
        return True
    return False

def validar_codigo(codigo, dicc_bodega):
    if validar_texto(codigo) and not buscar_codigo(codigo,dicc_bodega):
        return True
    return False

def validar_tamaño(tamaño):
    tamaño = tamaño.strip().upper()
    if tamaño in ['S','M','L']:
        return True
    return False


def validar_precio(precio):
    try:
        precio = int(precio)
        return precio > 0
        
    except ValueError:
        return False

def validar_unidades(unidades):
    try:
        unidades = int(unidades)
        return unidades >= 0
        
    except ValueError:
        return False


def agregar_arreglo(codigo,nombre_arreglo,tipo_arreglo,color_principal,tamaño_arreglo,incluye_tarjeta,temporada,precio,unidades,dicc_arreglos,dicc_bodega):
    booleano_tarjeta =  True if incluye_tarjeta.strip().lower() == "s" else False
    if not buscar_codigo(codigo,dicc_bodega):
        dicc_arreglos[codigo] = [nombre_arreglo.strip(),tipo_arreglo.strip().upper(),color_principal.strip(),tamaño_arreglo.strip().upper(),booleano_tarjeta,temporada.strip()]
        dicc_bodega[codigo] = [int(precio),int(unidades)]
        return True
    return False

def eliminar_codigo(codigo_buscado,dicc_arreglo,dicc_bodega):
    if buscar_codigo(codigo_buscado, dicc_bodega):
        del dicc_arreglo[codigo_buscado]
        del dicc_bodega[codigo_buscado]
        return True
    return False
    


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

        elif op_selec == 3:
            while True:
                    codigo_arreglo = input("Ingrese código del arreglo: ").strip().upper()
                    while True:
                            try:
                                nuevo_precio = int(input("Ingrese nuevo precio: "))
                                if nuevo_precio <= 0:
                                    print("Ingrese precio mayor a 0")
                                else:
                                    break

                            except ValueError:
                                print("Debe ingresar valores enteros positivo")
                    actualizado = actualizar_precio(codigo_arreglo, nuevo_precio,bodega)   
                    if actualizado:
                        print("Precio actualizado")
                    else:
                        print("Codigo no existe")

                    agregar_precio = input("¿Desea agregar otro precio? (s/n): ").lower()
                    if agregar_precio == "s":
                        continue
                    else:
                        break

        elif op_selec == 4:

            codigo = input("Ingrese codigo del arreglo: ").strip().upper()
            nombre = input("Ingrese nombre del arreglo: ")
            tipo = input("Ingrese tipo del arreglo: ")
            color_principal = input("Ingrese color del arreglo: ")
            tamaño = input("Ingrese tamaño del arreglo (S, M o L): ")
            tarjeta = input("¿Desea añadir tarjeta?(s/n): ")
            temporada = input("Ingrese temporada del arreglo: ")
            precio = input("Ingrese precio precio del arreglo: ")
            unidades = input("Ingrese unidades: ")

            todo_bien = True
            if not validar_codigo(codigo,bodega):
                print("error,ingrese codigo")
                todo_bien = False
            if not validar_texto(nombre):
                print("error,ingrese nombre")
                todo_bien = False
            if not validar_texto(tipo):
                print("error,ingrese tipo")
                todo_bien = False
            if not validar_texto(color_principal):
                print("error,ingrese color")
                todo_bien = False
            if not validar_tamaño(tamaño):
                print("error,ingrese tamaño")
                todo_bien = False
            if not validar_texto(temporada):
                print("error,ingrese temporada")
                todo_bien = False
            if not validar_precio(precio):
                print("error,ingrese precio")
                todo_bien = False
            if not validar_unidades(unidades):
                print("error,ingrese unidades")
                todo_bien = False

            
            if todo_bien:
                agregar_arreglo(codigo,nombre,tipo,color_principal,tamaño,tarjeta,temporada,precio,unidades,arreglos,bodega)
                print("Arreglo agregado")
            else:
                print("El codigo ya existe")
        
        elif op_selec == 5:

            codigo_eliminar = input("Ingrese codigo a eliminar").upper()
            codigo_existe = eliminar_codigo(codigo_eliminar, arreglos,bodega)

            if codigo_existe:
                print("Arreglo eliminado")
            else:
                print("El codigo no existe")


        elif op_selec == 6:
            print("Saliendo...")
            break

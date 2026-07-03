
def mostrar_menu():
    print("=" *20)
    print("======= MENÚ PRINCIPAL =======")
    print("1. AGREGAR EMPLEADO")
    print("2. BUSCAR EMPLEADO")
    print("3. ELIMINAR EMPLEADO")
    print("4. CALCULAR BONOS")
    print("5. MOSTRAR EMPLEADOS")
    print("6. SALIR")
    print("=" *20)

def escoger_op():
    while True:
        try:
            op = int(input("Ingrese opcion: "))
            break
        except ValueError:
            print("Error, ingrese un número")
    return op
def agregar_empleado(lista):

    nombre = input("Ingrese nombre del empleado: ")
    if not validar_texto(nombre):
        print("No puede estar la casilla vacia")
        return
    
    cargo = input("Ingrese cargo del empleado: ")
    if not validar_texto(cargo):
        print("No puede estar la casilla vacia")
        return
    while True:
        try:
            salario = int(input("Ingrese salario del empleado: "))
            if not validar_anio(salario):
                print("Error, debe ser un numero mayor que cero")
                return
            break
        except ValueError:
            print("Error, debe ser un número ")
    empleados = {
        "nombre" : nombre.strip(),
        "cargo" : cargo.strip(),
        "salario": salario,
        "bono" : False
    }
    
    lista.append(empleados)
    print(f"El empleado {nombre} agregado con exito")



    
def validar_texto(texto):
    return len(texto.strip()) > 0 #Return true

def validar_anio(valor):
    return 0 < valor
def buscar_empleado(lista, nombre):
    for i, empleado in enumerate(lista):
        if empleado["nombre"] == nombre:
            return i
    return -1
def calcular_bonos(lista):
    for empleado in lista:
        if empleado["salario"] < 800000:
            empleado["salario"] == True
        else:
            empleado["salario"] == False

def mostrar_empleados(lista):
    calcular_bonos(lista)
    if len(lista) == 0:
        print("No se encuentran empleados registrados")
        return
    print("==== LISTA DE EMPLEADOS ====")
    for empleado in lista:
        print(f"Nombre: {empleado['nombre']}")
        print(f"Cargo: {empleado['cargo']}")
        print(f"Salario: {empleado['salario']}")
        
        if empleado['bono']:
            print(f"Bono: Recibe bono")
        else:
            print("Bono: Sin bono")





#Codigo principal

lista_empleados = []

while True:
    mostrar_menu()

    op = escoger_op()

    if op == 1:
        agregar_empleado(lista_empleados)
    
    elif op == 2:
        nombre_buscar = input("Ingrese nombre de empleado a buscar: ")
        pos = buscar_empleado(lista_empleados,nombre_buscar)

        if pos != -1:
            empleado_encontrado = lista_empleados[pos]
            print(f"Nombre empleado: {empleado_encontrado['nombre']}")
            print(f"Cargo empleado: {empleado_encontrado['cargo']}")
            print(f"Salario empleado: {empleado_encontrado['salario']}")
            print(f"Bono: {empleado_encontrado['bono']}")
        
        else:
            print(f"No se encuentra el empleado {nombre_buscar} registrado ")

    elif op == 3:
        nombre = input("Ingrese nombre de empleado a eliminar: ")
        pos = buscar_empleado(lista_empleados, nombre)

        if pos != -1:

            lista_empleados.pop(nombre)
            print(f"Empleado {nombre} eliminado con exito")
        else:
            print(f"El empleado {nombre} no se encuentra registrado")
    elif op == 4:
        calcular_bonos(lista_empleados)
        print("Bonos calculados")
    
    elif op == 5:
        calcular_bonos(lista_empleados)
    elif op == 6:
        print("Saliendo")

    else:
        print("Error, ingrese opcion entre 1 y 6")
        break








    
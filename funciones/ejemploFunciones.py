#Funciones

def sumarDosNumeros():
    #Esta funcion permite sumar dos numeros, ingresados dentro de la funcion

    num1 = int(input("Ingrese número 1: "))
    num2 = int(input("Ingrese número 2: "))

    suma = num1 + num2

    print(f"La suma de {num1} + {num2} es  = {suma}")

def sumar(a,b) :
    #Esta funcion permite sumar dos números ingresados por parametros


    suma = a + b
    return suma

#linea principal
sumarDosNumeros()

res = sumar(4,5)
print(res)

num1 = int(input("Número 1: "))
num2 = int(input("Número 2: "))
res = sumar(num1, num2)
print("La suma es:",res)

import funcionesDetalle as fn
# from funcionesDetalle import sumar  (Es lo mismo que arriba , se llama directamente)

#linea principal
fn.sumarDosNumeros()

res = fn.sumar(4,5)
print(res)

num1 = int(input("Número 1: "))
num2 = int(input("Número 2: "))
res = fn.sumar(num1, num2)
print("La suma es:",res)

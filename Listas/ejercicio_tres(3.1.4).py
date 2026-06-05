import random
arreglo = []

for ciclo in range(50):
    aleatorio = random.randint(1,1000)
    arreglo.append(aleatorio)

print("")
print("Arreglo Original")
print(arreglo)
print("")

largo_arreglo = len(arreglo)

for i in range(largo_arreglo - 1):
    for j in range(largo_arreglo - 1 - i):
        if arreglo[j] > arreglo[j+1]:
            temporal = arreglo[j]
            arreglo[j] = arreglo[j+1]
            arreglo[j+1] = temporal

print("")
print("Arreglo Ordenando")
print(arreglo)

if largo_arreglo % 2 == 0:
    mediana = (arreglo[int(largo_arreglo/2) -1]) + arreglo[int(largo_arreglo/2)] /2
else:
    mediana = (arreglo[round(int(largo_arreglo/2))])
print("Mediana: ",mediana)

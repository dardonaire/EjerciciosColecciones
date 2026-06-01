sw = 1
listaSuper = []
valorSuper = []

print("Presione 1 para ingresar los productos del súper")
print("Presione cualquier numero para salir")

op = int(input("seleccione opción: "))

if op == 1:
    while sw == 1:
        try:
            print("-" * 50 )
            producto = input("Incorpore su producto, para salir, presione 0: ")
            if producto != "0":
                listaSuper.append(producto)
                valorProducto = int(input(f"Incorpore el valor del {producto}: "))
                valorSuper.append(valorProducto)
                print("-" * 20, "Detalle Boleta", "-" * 20)
                for i in listaSuper:
                    print(i)
                print(f"Cantidad de productos comprodos: {len(listaSuper)}")
                print(f"Total: {sum(valorSuper)}")
                print("-" * 20, "Detalle Boleta", "-" * 20)


            else:
                print("Adios")
                sw = 0

        except:
            print("Ingreso erroneo")
else:
    print("Adios")
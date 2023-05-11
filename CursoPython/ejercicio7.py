i = 0
mayor = None
while i < 5:
    numero = int(input("Ingrese un numero: "))
    if i == 0 or numero > mayor:
        mayor = numero
    i += 1
print(f"El mayor numero es {mayor}")

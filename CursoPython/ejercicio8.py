lista = []
total = 0
promedio = None
for i in range(5):
    numero = int(input("ingrese un numero"))
    lista.append(numero)
print(lista)
for numero in lista:
    total = total + numero
    promedio = total / len(lista)
print(total)
print(promedio)

numeros = [3, 5, 2, 8, 1, 9, 4, 2, 2,7,4,9,10]
pares = []
impares= []
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else :
        impares.append(numero)
print(impares)
print(pares)
print(f"en la lista hay {len(pares)} pares y {len(impares)} impares")
if(len(pares)) > len(impares):
    print("los pares son más")
elif(len(impares)) > len(pares):
    print("los impares son más")
else:
    print("son iguales")
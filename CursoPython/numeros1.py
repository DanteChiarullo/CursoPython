numeros = [23,-14,0,0,21,-9,-5,34,89]
ContNeg = 0
ContPos =0 
ContCeros = 0
for numero in numeros:
    if(numero == 0):
        ContCeros += 1
    elif (numero > 0):
        ContPos += 1
    else:
        ContNeg += 1
print("Ceros: " , ContCeros)
print("Positivos: " , ContPos)
print("Negativos: " , ContNeg)
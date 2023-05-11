nota = int(input("Ingrese una nota 0-10: "))
while nota > 10 or nota < 0:
    print("Nota invalida vuelva a ingresar")
    nota = int(input("vuelva a ingresar una nota :"))
print(f"su nota: {nota}")


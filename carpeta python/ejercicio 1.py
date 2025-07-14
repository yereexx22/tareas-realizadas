acumulador = 0
valor = 0
while valor != 9999:
    valor = int(input("Ingrese un valor (9999 para terminar): "))
    if valor != 9999:
        acumulador += valor

print(f"Valor acumulado: {acumulador}")

if acumulador == 0:
    print("El valor es cero.")
elif acumulador > 0:
    print("El valor es mayor a cero.")
else:
    print("El valor es menor a cero.")
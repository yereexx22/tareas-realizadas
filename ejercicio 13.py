suma_ultimos = 0

for i in range(10):
    numero = float(input(f"Número {i+1}: "))
    if i >= 5:
        suma_ultimos += numero

print("Suma de los últimos 5 números:", suma_ultimos)
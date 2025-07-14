def analizar_valores():
    negativos = 0
    positivos = 0
    multiplos_15 = 0
    suma_pares = 0

    print("Ingrese 10 números enteros:")

    for i in range(1, 11):
        valor = int(input(f"Valor {i}: "))
        
        if valor < 0:
            negativos += 1
        elif valor > 0:
            positivos += 1

        if valor % 15 == 0:
            multiplos_15 += 1

        if valor % 2 == 0:
            suma_pares += valor

    print("\nResultados:")
    print("Cantidad de negativos:", negativos)
    print("Cantidad de positivos:", positivos)
    print("Cantidad de múltiplos de 15:", multiplos_15)
    print("Suma de los números pares:", suma_pares)

analizar_valores()
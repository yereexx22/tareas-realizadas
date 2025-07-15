def mostrar_tabla():
    numero = int(input("Ingrese un número del 1 al 10: "))

    if 1 <= numero <= 10:
        print(f"\nTabla del {numero}:")
        for i in range(1, 13):
            resultado = numero * i
            print(f"{numero} x {i} = {resultado}")
    else:
        print("El número debe estar entre 1 y 10.")

mostrar_tabla()

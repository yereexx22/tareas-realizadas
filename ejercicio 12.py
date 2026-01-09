def calcular_superficie(base, altura):
    return (base * altura) / 2

def analizar_triangulos():
    cantidad = int(input("¿Cuántos triángulos vas a ingresar?: "))
    contador_mayores_12 = 0

    for i in range(cantidad):
        print(f"\nTriángulo {i+1}")
        base = float(input("Base: "))
        altura = float(input("Altura: "))

        superficie = calcular_superficie(base, altura)
        print("Base:", base)
        print("Altura:", altura)
        print("Superficie:", superficie)

        if superficie > 12:
            contador_mayores_12 += 1

    print("\nCantidad de triángulos con superficie mayor a 12:", contador_mayores_12)

analizar_triangulos()
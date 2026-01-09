def clasificar_triangulos():
    cantidad = int(input("¿Cuántos triángulos vas a ingresar?: "))

    equilateros = 0
    isosceles = 0
    escalenos = 0

    for i in range(cantidad):
        print(f"\nTriángulo {i+1}")
        lado1 = float(input("Lado 1: "))
        lado2 = float(input("Lado 2: "))
        lado3 = float(input("Lado 3: "))

        if lado1 == lado2 == lado3:
            print("Tipo: Equilátero")
            equilateros += 1
        elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
            print("Tipo: Isósceles")
            isosceles += 1
        else:
            print("Tipo: Escaleno")
            escalenos += 1

    print("\nResumen:")
    print("Equiláteros:", equilateros)
    print("Isósceles:", isosceles)
    print("Escalenos:", escalenos)

    # Identificar el tipo con menor cantidad
    menor_tipo = "Equiláteros"
    menor_cantidad = equilateros

    if isosceles < menor_cantidad:
        menor_tipo = "Isósceles"
        menor_cantidad = isosceles
    if escalenos < menor_cantidad:
        menor_tipo = "Escalenos"
        menor_cantidad = escalenos

    print("Tipo con menor cantidad:", menor_tipo)

clasificar_triangulos()
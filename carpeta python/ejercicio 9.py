def cargar_lista(nombre):
    print(f"\nCargando {nombre}")
    datos = []
    for i in range(15):
        valor = float(input(f"{nombre} - valor {i+1}: "))
        datos.append(valor)
    return datos

def comparar_listas():
    lista1 = cargar_lista("Lista 1")
    lista2 = cargar_lista("Lista 2")

    suma1 = sum(lista1)
    suma2 = sum(lista2)

    print(f"\nSuma total de Lista 1: {suma1}")
    print(f"Suma total de Lista 2: {suma2}")

    if suma1 > suma2:
        print("La Lista 1 tiene un valor acumulado mayor.")
    elif suma2 > suma1:
        print("La Lista 2 tiene un valor acumulado mayor.")
    else:
        print("Las dos listas tienen la misma suma.")

comparar_listas()
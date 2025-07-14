total_altura = 0
i = 0
cantidad = int(input("Ingrese la altura totales de la gente\n "))

while i < cantidad:
    altura = float(input(f"Ingrese la altura de la persona {i+1} en metros "))
    total_altura += altura
    i += 1

promedio = total_altura / cantidad
print(f"La altura promedio es: {promedio} metros")
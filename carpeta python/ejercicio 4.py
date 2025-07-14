probados = 0
no_aprobados = 0

for i in range(10):
    nota = float(input(f"Ingrese la nota del alumno {i+1}: "))
    if nota >= 7:
        aprobados += 1
    else:
        no_aprobados += 1

print(f"Cantidad de alumnos con nota mayor o igual a 7: {aprobados}")
print(f"Cantidad de alumnos con nota menor a 7: {no_aprobados}")
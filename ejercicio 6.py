cantidad_empleados = int(input("¿Cuántos empleados hay? "))
sueldos_bajos = 0
sueldos_altos = 0
gasto_total = 0

for _ in range(cantidad_empleados):
    sueldo = float(input("Ingrese sueldo del empleado: "))
    gasto_total += sueldo

    if 100 <= sueldo <= 300:
        sueldos_bajos += 1
    elif sueldo > 300:
        sueldos_altos += 1

print("Empleados que cobran entre 100 y 300:", sueldos_bajos)
print("Empleados que cobran más de 300:", sueldos_altos)
print("Total que gasta la empresa en sueldos", gasto_total)
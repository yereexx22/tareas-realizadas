cuenta = 0

while cuenta >= 0:

    cuenta = int(input("por favor ingresa el valor detu cuenta corriente y terminamos cuando coloques un negativo"))
    if cuenta >= 0:
        
        saldo = float(input("Ingrese saldo actual: "))
        print(f"Cuenta ingresada: {cuenta}, Saldo: {saldo}\n")
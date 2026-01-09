suma_acreedores = 0
cuenta = int(input("ingrese el saldo se la cuenta\n"))

while cuenta >= 0:
    saldo = float(input("saldo total"))
    print("Cuenta:", cuenta)
    if saldo > 0:
        print("Estado: Acreedor")
        suma_acreedores += saldo
    elif saldo < 0:
        print("Estado: Deudor\n")
    else:
        print("Estado: Nulo\n")

print(f" saldos acreedores totales {suma_acreedores}" )
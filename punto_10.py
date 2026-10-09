#retiro de dinero   

while True:
    saldo = float(input("ingrese el valor del saldo: "))
    retiro = float(input("ingrese el valor del retiro: "))

    if saldo < 0 or retiro <= 0:
        print("el saldo no puede ser negativo y el retiro debe ser mayor a 0")
        
    if retiro <= saldo:
        saldo_restante = saldo - retiro
        print(f"retiro exitoso por:{retiro}")
        print(f"tu saldo restante es:{saldo_restante}")
        break
    else :
            print("retiro no valido fondos insuficente")
            print(f"tu saldo actual es de:{saldo} y deseas retirar:{retiro}")
            

Numero_secreto = 10
intentos = 0 

while intentos < 5:
    N = int(input("Adivina el numero secreto del 1 al 20: "))
    intentos = intentos + 1

    if N == Numero_secreto:
        print("Felicidades adivinaste el número secreto")
        break

    elif N < Numero_secreto:
        print ("El número secreto es mayor.")
        print ("Te quedan", 5 - intentos, "intentos")

    else:
        print("El número secreto es menor")
        print("El numeros secreto era:", Numero_secreto)
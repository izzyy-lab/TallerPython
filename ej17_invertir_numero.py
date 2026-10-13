# Ejercicio 17: Invertir un numero
numero = int(input("Ingrese un entero positivo: "))

if numero <= 0:
    print("Debe ser un entero positivo")
else:
    copia = numero
    invertido = 0
    while copia > 0:
        ultimo = copia % 10
        invertido = invertido * 10 + ultimo
        copia = copia // 10
    print("El numero invertido es:", invertido)

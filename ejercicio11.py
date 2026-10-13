#Ejercicio 11: Tablas de multiplicar. Solicitar un número y mostrar su tabla de multiplicar del 1 al 10 mediante un ciclo.

number = int(input("Ingrese un número para mostar su tabla de multiplicar del 1 al 10: "))
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


for i in lista:
    print(f"{number} x {i} = {i*number}")
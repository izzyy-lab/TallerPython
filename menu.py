import runpy

ciclo = True 
while(ciclo):
    print(f"===== TALLER DE ALGORITMOS =====")
    print(f"1. Ejercicio del integrante 1(Felipe)")
    print(f"2. Ejercicio del integrante 2(Mariana)")
    print(f"3. Ejercicio del integrante 3(Vicente)")
    print(f"4. Ejercicio del integrante 4(Emanuel)")
    print(f"5. Ejercicio del integrante 4(Emanuel)")
    print(f"6. Salir")
    opcion = int(input(f"Seleccione una opción: "))
    if opcion == 1:
        runpy.run_path("ejercicio11.py")
    elif opcion == 2:
        runpy.run_path("repaso.py")
    elif opcion == 3:
        runpy.run_path("punto25.py")
    elif opcion == 4:
        runpy.run_path("repaso2.py")
    elif opcion == 5:
        runpy.run_path("ej17_invertir_numero.py")
    elif opcion == 6:
        print("opción válida, saliendo del menú")
        ciclo = False 
    else: 
        print("Opción no válida")
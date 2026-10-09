#25 Buscar nombres. Crear una lista con 10 nombres de aprendices. 
#Solicitar un nombre y verifica si existe, indicando su posicion.

listaNombres = ["Vicente","Emanuel","Felipe","Andrés","Mariana",
"Santiago","Ana","Juan","Esteban","Pablo"]


while(True):
    contador = 0
    for nombre in listaNombres:
        print(f"{contador}. {nombre}")
        contador += 1
        
    nombreAprendiz = input("\nIngrese el nombre de aprendiz (Inicial en mayuscula): ")
    
    indice = listaNombres.index(nombreAprendiz)

    if nombreAprendiz in listaNombres:
        print(f"\nEl aprendiz se encuenta en la posicion: {indice}")
    else: 
        print(f"\nEl aprendiz no se encuenta en la lista")
    
    continuar = int(input("\nDesea continuar? (1. SI - 2. NO) "))
    if continuar != 1:
        break
    else:
        continue
        
    


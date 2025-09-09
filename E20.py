
lista_numeros = []

diccionario_estadisticas = {
    "numeros": lista_numeros,
    "suma": 0,
    "promedio": 0,
    "numero_max": 0,
    "numero_min": 0
}

print(lista_numeros)

def pedir_numeros():
    usuario = ""
    
    while usuario != "fin":
        usuario = input("Ingresa numeros: ")
        
        if usuario == "fin":
            break
        
        elif usuario.isdigit():
            numeros = int(usuario)
            lista_numeros.append(numeros)
            
        else:
            print("Solo se aceptan numeros")
pedir_numeros()
print(lista_numeros)

def calcular_estadisticas(lista_numeros):
    
    suma = 0
    promedio = 0
    numero_max = 0
    numero_min = 0
    
    for number in lista_numeros:
        suma += number
        
        diccionario_estadisticas["suma"]= suma
        
    promedio = suma / len(lista_numeros)
        
    diccionario_estadisticas["promedio"] = promedio
        
    numero_max = max(lista_numeros)
    numero_min = min(lista_numeros)
        
    diccionario_estadisticas["numero_max"] = numero_max
    diccionario_estadisticas["numero_min"] = numero_min
        
    return suma, promedio, numero_max, numero_min
    
suma, promedio, numero_max, numero_min = calcular_estadisticas(lista_numeros)
print("Suma:", suma)
print("Promedio:", promedio)
print("Numero_max:", numero_max)
print("Numero_min:", numero_min)
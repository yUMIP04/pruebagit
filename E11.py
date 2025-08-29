usuario = input("Ingresa varias frases: ").replace(",", "").replace(".", "").replace("$", "").lower().split()

diccionario = {
    "palabras_unicas": set(),
    "numeros_ordenados": [],
    "palabras_largas": [],
    
    "Total_palabras":len(usuario),
    "num_mayor":0,
    "num_menor": 0
    
}

numero_max = 0
numero_min= 0


for frases in usuario:
    
    if usuario.count(frases) == 1 and not frases.isdigit():
        
        diccionario["palabras_unicas"].add(frases)
        
    if frases.isdigit():
        
        numeros = int(frases)
        
        diccionario["numeros_ordenados"].append(numeros)
        diccionario["numeros_ordenados"] = sorted(diccionario["numeros_ordenados"])
        
        numero_max = max(diccionario["numeros_ordenados"])
        numero_min = min(diccionario["numeros_ordenados"])
        
        diccionario["num_mayor"] = numero_max
        diccionario["num_menor"] = numero_min
        
    if len(frases) > 6:
        
        diccionario["palabras_largas"] = frases
        
print(diccionario)
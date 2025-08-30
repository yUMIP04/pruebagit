diccionario = {
    "palabras_unicas": set(),
    "empezando_vocal": 0,
    "empezando_consonante": 0,
    "numeros": [],
    "maximo_minimo":(None, None),
    "Promedio_numeros": 0.0,
    "frase_invertida": ""
}

numero_max = 0
numero_min = 0

usuario = ""
while usuario != "fin":
 usuario = input("Ingresa varias frases: ").replace(",", "").replace(".", "").replace("$", "").lower()
 
 if usuario == "fin":
     break
 
 palabras = usuario.split()

 for frases in palabras :
    
    if palabras.count(frases) == 1 and not frases.isdigit():
        diccionario["palabras_unicas"].add(frases)
        
    if frases.startswith("a") or  frases.startswith("e") or  frases.startswith("i") or  frases.startswith("o") or  frases.startswith("u") and not frases.isdigit():
        
        diccionario["empezando_vocal"]+=1  
        
    else:
        diccionario["empezando_consonante"] += 1
        
    if frases.isdigit():
        
        numeros = int(frases)
        
        diccionario["numeros"].append(numeros)
        
        numero_max = max(diccionario["numeros"])
        numero_min = min(diccionario["numeros"])
        
        diccionario["maximo_minimo"] = (numero_max, numero_min)
        
        promedio = sum(diccionario["numeros"])/len(diccionario["numeros"])
        
        diccionario["Promedio_numeros"] = promedio
        
    diccionario["frase_invertida"] = usuario[::-1]
print(diccionario)

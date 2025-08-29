usuario = input("Ingresa varias frases: ").lower().replace(",", "").replace(".", "").replace(";", "").split()

diccionario = {
    "cantidad_palabras_unicas": set(),
    "cantidad_numeros_enteros": [],
    "Numerominimo_Numeromaximo": (None , None),
    "palabras_vocal": [],
    "palabras_que_terminen_consonante": []
}

numero_max = 0
numero_min = 0

for frases in usuario:
    
    if usuario.count(frases) == 1 and not frases.isdigit():
        
        diccionario["cantidad_palabras_unicas"].add(frases)
        
    if frases.isdigit():
        
        numeros = int(frases)
        
        diccionario["cantidad_numeros_enteros"].append(numeros)
        
        numero_max= max(diccionario["cantidad_numeros_enteros"])
        numero_min = min(diccionario["cantidad_numeros_enteros"])
        
        diccionario["Numerominimo_Numeromaximo"]= (numero_min, numero_max)
        
    if frases.startswith("a") or frases.startswith("e") or frases.startswith("i") or frases.startswith("o") or frases.startswith("u"):
        
        diccionario["palabras_vocal"].append(frases) 
        
    if not frases.endswith(("a", "e", "i", "o", "u")) and not frases.isdigit():
        diccionario["palabras_que_terminen_consonante"].append(frases)
        
print(diccionario)
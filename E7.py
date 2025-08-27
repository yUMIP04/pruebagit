usuario = input("Ingresa varias frases: ").replace(";", "").replace("$", "").replace(",", "").replace(".", "").lower().split()

diccionario = {
    "total_palabras": 0,
    "Palabras_unicas": set(),
    "Vocal_Inicio": 0,
    "Palabra_mas larga": ""
}

for frases in usuario:
    
    diccionario["total_palabras"] += 1
    
    if usuario.count(frases) == 1:
        
        diccionario["Palabras_unicas"].add(frases)
        
    if frases.startswith("a") or  frases.startswith("e") or  frases.startswith("i") or  frases.startswith("o") or  frases.startswith("u"):
        
        diccionario["Vocal_Inicio"] += 1
        
    if len(frases) > len(diccionario["Palabra_mas larga"]):
        diccionario["Palabra_mas larga"] = frases
             
print(diccionario)
    
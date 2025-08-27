usuario = input("ingresa 3 frases: ").lower().replace(",", "").replace(".", "").split()

diccionario = {
    "palabras_unicas":set(),
    "total_palabras": 0,
    "contiene_python": False
}

for frases in usuario:
    
    if usuario.count(frases) == 1:
        
        diccionario["palabras_unicas"].add(frases)
        
    diccionario["total_palabras"] += 1
    
    if frases in "python":
        
        diccionario["contiene_python"] = True
        
print(diccionario)
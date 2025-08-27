usuario = input("Ingresa un texto grande: ").lower().replace(",", "").replace(".", "").replace("$", "").split()

diccionario = {
    "palabras_repetida" : set(),
    "palabras_solo_una_vez" : 0
}

for frases in usuario:
    
    if usuario.count(frases) == 2:
        
        diccionario["palabras_repetida"].add(frases)
        
    if usuario.count(frases) == 1:
        
        diccionario["palabras_solo_una_vez"] += 1
        
print(diccionario)
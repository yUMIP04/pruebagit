usuario = input("Ingresa varias frases: ").lower().replace(",", "").replace(".", "").split()

diccionario = {
    "Palabras_unicas": 0,
    "numeros_mayores_100": 0,
    "palabras_terminan_vocal": 0
}

for frases in usuario:
    
    if usuario.count(frases) == 1: 
        diccionario["Palabras_unicas"] += 1
        
    if frases.isdigit() and int(frases) > 100:
        diccionario["numeros_mayores_100"] += 1
        
    if frases.endswith("a") or  frases.endswith("e") or  frases.endswith("i") or  frases.endswith("o") or  frases.endswith("u"):
        
        diccionario["palabras_terminan_vocal"] += 1
        
print(diccionario)
usuario = input("Ingresa varias frases: ")

diccionario = {
    "frase": "",
    "palabras_mas_5": "",
    "pares": [],
    "impares": []
}

diccionario["frase"] = usuario

for frases in usuario.replace(",", "").replace(".", "").lower().split():
    
    if len(frases) > 5:
        
        diccionario["palabras_mas_5"] = frases
        
    if frases.isdigit() and int(frases) % 2 == 0:
        diccionario["pares"] = int(frases)
        
    else:
        diccionario["impares"] = frases
        
        
print(diccionario)
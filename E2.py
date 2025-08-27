usuario = input("Ingresa frases: ").replace("$", "").replace(";", "").replace(",", "").replace(".", "").lower().split()

diccionario ={
    "vocal_empezar": [],
    "numeros_mayores_100": [],
    "precios_mayores_200": []
}

for frases in usuario:
    
    if frases.startswith("a") or frases.startswith("e") or frases.startswith("i") or frases.startswith("o") or frases.startswith("u"):
        
        diccionario["vocal_empezar"].append(frases)
        
    if frases.isdigit() and int(frases) > 100:
        
        diccionario["numeros_mayores_100"].append(frases)
        
    if frases.isdigit() and int(frases) > 200:
        
        diccionario["precios_mayores_200"].append(frases)
        
print(diccionario)
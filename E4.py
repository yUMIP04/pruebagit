usuario = input("Ingresa varias frases: ").replace("$", "").replace(",", "").replace(".", "").lower().split()

diccionario = {
    "palabras_con_a": [],
    "palabras_largas": [],
    "numeros_pares": [],
    "precios_mayores_a_500": []
} 

for frases in usuario:
    
    if frases.startswith("a"):
        diccionario["palabras_con_a"].append(frases)
        
    if len(frases) > 7:
        diccionario["palabras_largas"].append(frases)
        
    if frases.isdigit() and int(frases) % 2 == 0:
        diccionario["numeros_pares"].append(frases)
        
    if frases.isdigit() and int(frases) > 500:
        
        diccionario["precios_mayores_a_500"].append(frases)
        
print(diccionario)
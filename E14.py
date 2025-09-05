usuario = ""

diccionario = {
    "frase": [],
    "vocales": 0,
    "numeros_mayores_50": [],
    "suma": 0,
    "max_min": (None, None)
}

num_max = 0
num_min = 0

while usuario != "fin":
    
    usuario = input("ingresa varias frases: ").lower().replace(",", "").replace(".", "").replace("?", "").replace("!", "")
    
    if usuario == "fin":
        
        break
    diccionario["frase"].append(usuario)
   
    palabras = usuario.split()
 
    for frases in palabras:
    
     if frases.startswith(("a", "e", "i", "o", "u")) and not frases.isdigit():
        
        diccionario["vocales"] += 1
        
     if frases.isdigit() and int(frases) > 50:
        
        numeros = int(frases)
        
        diccionario["numeros_mayores_50"].append(numeros)
        
        suma = sum(diccionario["numeros_mayores_50"])
        diccionario["suma"] = suma
        
        num_max = max(diccionario["numeros_mayores_50"])
        num_min = min(diccionario["numeros_mayores_50"])
        
        diccionario["max_min"] = (num_max, num_min)
print(f"La frase es: {diccionario['frase']}")      
print(f"Vocales en la frase: {diccionario['vocales']}")
print(f"Numeros mayores a 50: {diccionario['numeros_mayores_50']}")
print(f"La suma: {diccionario['suma']}")
print(f"El maximo y minimo: {diccionario['max_min']}")

list_frases = []

diccionario = {
   
   "palabras_unicas": set(),
   "empieza_vocal": 0,
   "empiezan_consonante": 0,
    "numeros":[],
    "maximo_minimo_promedio": (None, None, None),
    
}

numero_max = 0
numero_min = 0

usuario = ""

while usuario != "fin":
    
    usuario= input("Ingresa frases: ").lower().replace(",", "").replace(".", "").strip()
    
    if usuario == "fin":
        
               
        break
    list_frases.append(usuario) 
    palabras = usuario.split()
    
    for frases in palabras:
        
        if palabras.count(frases) == 1 and not frases.isdigit():
            
            diccionario["palabras_unicas"].add(frases)
            
        if frases.startswith("a") or frases.startswith("e") or frases.startswith("e") or frases.startswith("i") or frases.startswith("o") or frases.startswith("u") and not frases.isdigit():
            
            diccionario["empieza_vocal"] += 1  
            
        else:
            
            diccionario["empiezan_consonante"] += 1
            
        if frases.isdigit():
            
            numeros = int(frases)
            
            diccionario["numeros"].append(numeros)
            
            numero_max = max(diccionario["numeros"])
            numero_min = min(diccionario["numeros"])
            
            promedio = (sum(diccionario["numeros"]))/len(diccionario["numeros"])
            
            diccionario["maximo_minimo_promedio"] = (numero_max, numero_min, promedio)
            
print(f"Las palabras unicas son: {diccionario['palabras_unicas']}")
print(f"Cantidad de palabras con vocales: {diccionario['empieza_vocal']}")
print(f"Cantidad de palabras con consonantes: {diccionario['empiezan_consonante']}")
print(f"Lista de numeros: {diccionario['numeros']}")
print(f"Maximo, minimo y el promedio: {diccionario['maximo_minimo_promedio']}")

print(f"Lista de todas las frases:{list_frases}")
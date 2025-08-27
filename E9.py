usuario = input("Ingresa frases con numeros mezclados: ").lower().replace("$", "").replace(",", "").replace(".", "").split()

diccionario = {
    
    "Cantidad_numeros": 0,
    "Suma total": 0,
    "Promedio": 0,
    "Maximo_minimo": (None, None)
}

minimo = None
maximo = None

for frases in usuario:
    
    if frases.isdigit():
        
        number = int(frases)
        
        diccionario["Cantidad_numeros"]+= 1
        
        diccionario["Suma total"] += number
        
        promedio = (diccionario["Suma total"])/ diccionario["Cantidad_numeros"]
        
        diccionario["Promedio"] = promedio
        
    if minimo is None or number < minimo:
        
        minimo = number
        
    if maximo is None or number > Maximo:
         Maximo = number
         
         diccionario["Maximo_minimo"] = (Maximo, minimo)
         
        
print(diccionario)
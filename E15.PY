usuario = ""
list_frases = []

diccionario = {
    "frases": set(),
    "numeros": [],
    "max_min": (None, None),
    "palabras_ordenadas": []
}

num_max = 0
num_min = 0

while usuario != "fin":
    
    usuario = input("Ingresa varias frases: ").lower().replace(",", "").replace("$", "").replace(".", "")
    
    if usuario == "fin":
        break
    list_frases.append(usuario)
    
    
    for frases in usuario.split():
        diccionario["frases"].add(frases)
        
        if frases.isdigit():
            numeros = int(frases)
            diccionario["numeros"].append(numeros)
            
            num_max= max(diccionario["numeros"])
            num_min = min(diccionario["numeros"])
            
            diccionario["max_min"] = (num_max, num_min)
            
            
        diccionario["palabras_ordenadas"] = sorted(list_frases)
    
  
while True:
    print("1.Ver todas las frases")
    print("2.Ver solo numeros y estadisticas globales como min y max")
    print("3.Ver palabras unicas ordenadas alfabeticamente")
    print("4.Salir")
    option = input("Elige una de las opciones: ")
    
    
    if option == "1":
        print(diccionario["frases"])
        
    if option == "2":
       print(diccionario["numeros"])
       
    elif option == "min y max":
        print(diccionario["max_min"])
       
    if option == "3":
        print(diccionario["palabras_ordenadas"]) 
        
    if option == "4":
        
        print("saliendo del programa")
        break
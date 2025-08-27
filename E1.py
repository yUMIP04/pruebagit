usuario= input("Escribe una serie de frases: ").lower().split()

diccionario = {
    "vocal": [],
    "numero": [],
    "mayor_a_100": []
}

for frases in usuario:
   frases = frases.replace(",", "")
    
   if frases.startswith("a") or frases.startswith("e") or frases.startswith("i") or frases.startswith("o") or frases.startswith("u") :
        diccionario["vocal"].append(frases)
        
        
   if frases.isdigit() and int(frases) < 100:
        diccionario["numero"].append(frases)
        
   if frases.isdigit() and int(frases) > 100:
       
      diccionario["mayor_a_100"].append(int((frases)))             
print(diccionario)
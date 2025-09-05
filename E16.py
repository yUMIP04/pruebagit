import os

diccionario = {
    "total_frases": 0,
    "total_palabras": 0,
    "palabras_unicas": set(),
    "numeros": [],
    "numero_max":None,
    "numero_min":None,
    "Promedio_de_numeros": 0.0,
    "palabra_mas_larga": ""
    
}
list_frases = []
usuario = ""
numero_max = 0
numero_min = 0

while usuario != "fin":
    
    usuario = input("Ingresa varias frases: ").lower().replace(",", "").replace(".", "").replace("$", "").replace("!", "").replace("?", "").replace("¡", "").replace(";", "")
    
    if usuario == "fin":
        
        break
    list_frases.append(usuario)
    
    for frases in usuario.split():
        
        diccionario["total_frases"] += 1
        
        if usuario.count(frases) == 1:
            diccionario["palabras_unicas"].add(frases)
        
        if frases.isdigit():
            numeros = int(frases)
            
            diccionario["numeros"].append(numeros)
            
            numero_max = max(diccionario["numeros"])
            numero_min = min(diccionario["numeros"])
            
            diccionario["numero_max"] = numero_max
            diccionario["numero_min"] = numero_min
            
            promedio = (sum(diccionario["numeros"]))/len(diccionario["numeros"])
            
            diccionario["Promedio_de_numeros"]=promedio
            
        if len(frases) > len(diccionario["palabra_mas_larga"]):
            diccionario["palabra_mas_larga"]=frases
            
        
        for palabras in frases.split():
            diccionario["total_palabras"] += 1
print(diccionario["palabra_mas_larga"])  


while True:
    print("1.Todas las frases.")
    print("2.Lista de numeros,total,promedio,mayor,menor.")
    print("3.Palabras unicas en orden alfabetico.")
    print("4.Guardar resultados en un archivo y hacer break.")
    option= input("Elige una opcion: ")  
    
    if option == "1":
        
        print(sorted(list_frases))
        
    if option == "2":
        
        print(diccionario["numeros"])
        
    elif option == "total":
        print(f"El total de palabras: {diccionario["total_frases"]}")
        print(f"El total de palabras: {diccionario["total_palabras"]}")
        print(f"Palabra mas larga: {diccionario['palabra_mas_larga']}")
        
    elif option == "promedio":
         print(f"El promedio es: {diccionario["promedio"]}")
         
    elif option == "mayor":
         print(f"El numero mayor: {diccionario["numero_max"]}")
         print(f"El numero menor: {diccionario["numero_min"]}")
         
    if option == "4":
        
        with open("archivo_pruieba.txt", "a") as f:
            f.write(str(diccionario))
            break             
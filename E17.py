
def pedir_frases():
    frases = []
    
    usuario = ""
    while usuario != "fin":
        usuario = input("Ingresa varias frases: ").lower().replace(",", "").replace(".", "").replace("$", "")
        
        if usuario == "fin":
            break
        frases.append(usuario)
    return frases
        
        
def procesar_frases(frases):
    estadisticas = {
        "frases": frases,
        "numeros": [],
        "palabras_unicas": set(),
        "palabra_mas_larga": "",
        "palabra_mas_corta": ""
    }
    
    todas_las_palabras = []
    
    for frase in frases:
        palabras = frase.split()
        todas_las_palabras.extend(palabras)
        
        for palabra in palabras:
            if palabra.isdigit():
                numeros = int(palabra)
                
                estadisticas["numeros"].append(numeros)
                
                for palabra in todas_las_palabras:
                    if todas_las_palabras.count(palabra) == 1:
                        
                        estadisticas["palabras_unicas"].add(palabra)
                        
                        if estadisticas["palabra_mas_larga"] == "" or len(palabra) > len(estadisticas["palabra_mas_larga"]):
                            estadisticas["palabra_mas_larga"]=palabra
                            
                            if estadisticas["palabra_mas_corta"] == "" or len(palabra) < len(estadisticas["palabra_mas_corta"]):
                                estadisticas["palabra_mas_corta"] = palabra
                                
                                return estadisticas

def mostrar_menu(estadisticas):
    
    while True:
        print("1.Ver todas las frases procesadas")
        print("2.Ver solo numeros")
        print("3.Ver palabras unicas y ordenadas alfabeticamente")
        print("4.Salir")
        
        option= input("Elige una de las opciones: ")
        
        if option == "1":
            
            print(estadisticas["frases"])
            
        if option == "2":
            print(estadisticas["numeros"])
            
        if option == "3":
            print(sorted(estadisticas["palabras_unicas"]))
            print(estadisticas["palabra_mas_larga"])
            print(estadisticas["palabra_mas_corta"])
            
        if option == "4":
            
            print("Saliendo del programa...")
            break
frases = pedir_frases()
estadisticas = procesar_frases(frases)
mostrar_menu(estadisticas)

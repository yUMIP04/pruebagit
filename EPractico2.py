usuario = input("Ingresa frases con numeros: ").replace(",", "").replace(".", "").lower().split()

lista_numbers = []

numero_max = 0
numero_min = 0

for numeros in usuario:
    
    if numeros.isdigit():
        
        numbers = int(numeros)
        
        lista_numbers.append(numbers)
        
if lista_numbers:
    
    numero_max = max(lista_numbers)
    numero_min = min(lista_numbers)
    
else:
    print("No hay numeros en las frases")
        
print(f"La lista es: {lista_numbers}")
print(f"El numero mayor es: {numero_max}")
print(f"El numero menor es: {numero_min}")
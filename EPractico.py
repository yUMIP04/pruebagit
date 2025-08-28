usuario = input("Ingresa una frase: ").replace(",", "").replace(".", "").lower().split()

numeros =[]

numero_max = 0
numero_min = 0

for number in usuario:
    
    if number.isdigit():
        
        numero = int(number)
        
        numeros.append(numero)
        
if numeros :
    numero_max = max(numeros)
    numero_min = min(numeros)
    
    print(f"El numero mayor es:{numero_max}")
    print(f"El numero menor es:{numero_min}")
    
else:
    print("No hay numeros en la frase")
        
        
        
print(numeros)


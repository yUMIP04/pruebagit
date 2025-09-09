usuario = input("Ingresa varios numeros: ").split(",")

lista = []

for numbers in usuario:
    numbers = numbers.strip()
    if numbers.isdigit():
        number = int(numbers)
        lista.append(number)
        
def funcion_lista(lista: list):
    suma = 0
    promedio = 0
    maximo = 0
    minimo = 0
    
    suma = sum(lista)    
    promedio = suma / len(lista)
    maximo = max(lista)
    minimo = min(lista)
        
    return suma, promedio, maximo, minimo

suma, promedio, maximo, minimo = funcion_lista(lista)

print("suma:", suma )
print("promedio:", promedio )
print("maximo:", maximo)
print("minimo:", minimo )
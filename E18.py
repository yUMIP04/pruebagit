
def suma(a:int, b:int):
    resultado = a + b
    
    return resultado


def sumar_lista(lista:list):
    suma = 0
    
    for number in lista:
        suma += number
        
    return suma

lista = [1, 2, 3, 4, 5]
x = sumar_lista(lista)
print(x)
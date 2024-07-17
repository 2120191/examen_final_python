"""
crear una funcion que haciendo uso del metodo filter me filtre los numeros primos de una lista pasada por parametros
"""


def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def filtrar_primos(lista):
    return list(filter(es_primo, lista))

# Lista de ejemplo
numeros = [2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filtrar números primos de la lista
primos = filtrar_primos(numeros)

print('Números primos en la lista:', primos)
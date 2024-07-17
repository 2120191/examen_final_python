"""
crear un funcion que reciba como parametro una lista de numeros y me retorne dos valores el numero menor y el numero mayor en un diccionario
ejem:
entrada: [4,7,10,4,1,0]
salida : {menor:0,mayor:10}
"""

def encontrar_menor_mayor(lista):
    menor = min(lista)
    mayor = max(lista)
    return {'menor': menor, 'mayor': mayor}

# Lista de números de ejemplo
numeros = [4, 7, 10, 4, 1, 0]

# Encontrar el número menor y mayor
resultado = encontrar_menor_mayor(numeros)

print(resultado)

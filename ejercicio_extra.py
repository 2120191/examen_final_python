"""
Crear un diccionario de 5 registros de tiendas comerciales
y crear las siguientes funciones para el procesamiento de su informacion
1. funcion que me permita editar el nombre de una las tiendas comerciales
2. funcion que me permita actualizar el horario de atencion.
3. funcion que me permita eliminar una tienda comercial.
"""
tiendas = {
    'tienda1': {'nombre': 'Tienda A', 'ubicacion': 'Centro', 'productos': ['ropa', 'accesorios']},
    'tienda2': {'nombre': 'Tienda B', 'ubicacion': 'Norte', 'productos': ['electrodomesticos', 'tecnologia']},
    'tienda3': {'nombre': 'Tienda C', 'ubicacion': 'Sur', 'productos': ['alimentos', 'bebidas']},
    'tienda4': {'nombre': 'Tienda D', 'ubicacion': 'Este', 'productos': ['juguetes', 'libros']},
    'tienda5': {'nombre': 'Tienda E', 'ubicacion': 'Oeste', 'productos': ['muebles', 'decoracion']}
}

def editar_tienda(tienda, atributo, nuevo_valor):
    tiendas[tienda][atributo] = nuevo_valor

def actualizar_tienda(tienda, nuevos_productos):
    tiendas[tienda]['productos'] = nuevos_productos

def eliminar_tienda(tienda):
    del tiendas[tienda]
editar_tienda('tienda1', 'ubicacion', 'Este')

actualizar_tienda('tienda3', ['ropa', 'accesorios', 'calzado'])

eliminar_tienda('tienda5')

print(tiendas)

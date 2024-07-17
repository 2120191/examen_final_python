"""
crear un diccionario que tenga dos registros de un alumo
1. crear un funcion que me imprima los registro,
2. crear una funcion que me ´permita editar uno de los campos del registro
"""

registro_alumnos = {
    'alumno1': {'nombre': 'Juan Perez', 'edad': 20, 'curso': 'Matematicas'},
    'alumno2': {'nombre': 'Maria Lopez', 'edad': 22, 'curso': 'Fisica'}
}
def imprimir_registro(registro):
    for key, value in registro.items():
        print(f'{key}: {value}')

def editar_registro(registro, alumno, atributo, nuevo_valor):
    registro[alumno][atributo] = nuevo_valor
imprimir_registro(registro_alumnos)
editar_registro(registro_alumnos, 'alumno1', 'curso', 'Biologia')
imprimir_registro(registro_alumnos)
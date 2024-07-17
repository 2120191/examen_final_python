"""
Crear una funcion que me me retorne un diccionario con los datos personales de un alumno
ejm:
entrada: ("jose","alvarez","30","APSTI","III")
salida: {nombre:"jose",apellido:"alvarez",edad:"30",programa_estudio:"APSTI",semestre:"III"}
"""

nombre="jose"
apellido="alvarez"
edad=30
curso="apsti"
periodo="III"
def persona(nom,ape,edad,cur,peri):
    return {
    #   "nombre":nom
    #   "apellido":ape
    #   "edad":edad
    #   "curso":cur
    #   "periodo":peri
    }
    return dict(
        nombre=nom,
        apellido=ape,
        edad=edad,
        curso=cur,
        periodo=peri,
    )
print(persona(nombre,apellido,edad,curso,periodo))

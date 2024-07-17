"""
crear un diccionario que tenga dos registros de un alumo
1. crear un funcion que me imprima los registro,
2. crear una funcion que me permita editar uno de los campos del registro
"""
registro_alumnos={
    1: {
        "nombre":"bretmer",
        "apellido":"condori",
        "edad":19
    },
    2: {
        "nombre":"percy",
        "apellido":"yarihuaman",
        "edad":21
    }
}

def imprimir_registros(registro_alumnos):
    for id_registro,datos in registro_alumnos.items():
        print(id_registro,datos)

def editar_registro(registro_alumnos, id_alumno, campo, nuevo_valor):
    if id_alumno in registro_alumnos:
        if campo in registro_alumnos[id_alumno]:
            registro_alumnos[id_alumno][campo] = nuevo_valor
            print(f"Registro actualizado: id {id_alumno}, {campo} cambiado a {nuevo_valor}")
        
imprimir_registros(registro_alumnos)
editar_registro(registro_alumnos,1, "edad",20)

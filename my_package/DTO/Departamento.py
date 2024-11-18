class Departamento():

    def __init__(self, nombre, ubicacion, gerente, id = 'NO ID'):
        self.nombre_departamento = nombre
        self.ubicacion_departamento = ubicacion
        self.gerente_departamento = gerente
        self.id = id

    def __str__(self):
        if self is None:
            return " No hay departamentos con ese id "
        else:
            return f''' ID               : {self.id}
NOMBRE           : {self.nombre_departamento}
UBICACION        : {self.ubicacion_departamento}
GERENTE          : {self.gerente_departamento}
======================================='''
class Departamento():

    def __init__(self, nombre, ubicacion, gerente):
        self.nombre_departamento = nombre
        self.ubicacion_departamento = ubicacion
        self.gerente_departamento = gerente

    def __str__(self):
        return f'{self.nombre_departamento}, {self.ubicacion_departamento} GERENTE: {self.gerente_departamento}'
class Proyecto():
    def __init__(self, nombre, descripcion, fecha, id_depto):
        self.nombre_proyecto = nombre
        self.descripcion_proyecto = descripcion
        self.fecha_inicio_proyecto = fecha
        self.id_depto = id_depto

    def __str__(self):
        return f"NOMBRE PROYECTO: {self.nombre_proyecto}\nDESCRIPCION: {self.descripcion_proyecto}\nINICIO: {self.fecha_inicio_proyecto}\n DEPTO ID: {self}"
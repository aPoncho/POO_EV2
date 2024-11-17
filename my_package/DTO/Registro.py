class Registro():
    def __init__(self, fecha, horas, descripcion, id_empleado = 'NO ID', id_registro = 'NO ID'):
        self.fecha_registro = fecha
        self.cantidad_horas = horas
        self.descripcion_registro = descripcion
        self.id_empleado = id_empleado
        self.id = id_registro

    def __str__(self):
        return f" ID : {self.id} - FECHA : {self.fecha_registro} - CANTIDAD DE HORAS TRABAJADAS : {self.cantidad_horas} - DESCRIPCION : {self.descripcion_registro} - ID EMPLEADO VINCULADO : {self.id_empleado}"
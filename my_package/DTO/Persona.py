class Persona():
    def __init__(self, nombre, apellido, correo):
        #atributos que quizas deberian ser "protected (_atributo)"
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo

    def __str__(self):
        return f'''
NOMBRE           : {self.nombre}
APELLIDO         : {self.apellido}
CORREO           : {self.correo}'''
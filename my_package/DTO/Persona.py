class Persona():
    def __init__(self, run, nombre, apellido, direccion, fono, correo):
        #atributos que quizas deberian ser "protected (_atributo)"
        self.run = run
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion
        self.fono = fono
        self.correo = correo

    def __str__(self):
        return f'''RUN              : {self.run}
NOMBRE           : {self.nombre}
APELLIDO         : {self.apellido}
DIRECCION        : {self.direccion}
FONO             : {self.fono}
CORREO           : {self.correo}'''
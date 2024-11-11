#clase de prueba aun no implementada
#clase padre, usuario y empleado heredaran de esta
class Persona():
    def __init__(self, run, nombre, apellido, direccion, correo, telefono):
        #atributos que quizas deban ser "protected (_atributo)"
        self.run = run
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion
        self.fono = telefono
        self.correo = correo
from my_package.DTO.Persona import Persona

class Usuario(Persona):
    def __init__(self, run, nombre, apellido, direccion, fono, correo, username, password, tipo_usuario):
        super().__init__(run, nombre, apellido, direccion, fono, correo)
        #atributos deberian privados (no se puede acceder a ellos fuera de la clase)
        self.username = username
        self.pasword_hash = password
        self.tipo_usuario = tipo_usuario

    def __str__(self):
        datos = super().__str__()
        return f"Usuario: {self.username} \n {datos}"



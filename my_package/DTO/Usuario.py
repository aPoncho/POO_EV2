from my_package.DTO.Persona import Persona

class Usuario(Persona):
    def __init__(self, run, nombre, apellido, direccion, fono, correo, id, password):
        super().__init__(run, nombre, apellido, direccion, fono, correo)
        #atributos deberian privados (no se puede acceder a ellos fuera de la clase)
        self.id = id
        self.pasword = password

    def __str__(self):
        datos = super().__str__()
        return f"Usuario: {self.id} \n {datos}"



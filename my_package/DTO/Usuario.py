from my_package.DTO.Persona import Persona
#clase no implementada
#subclase de Persona

class Usuario(Persona):
    def __init__(self, run, nombre, apellido, direccion, fono, correo, id, password):
        super().__init__(run, nombre, apellido, direccion, fono, correo)
        #atributos privados (no se puede acceder a ellos fuera de la clase)
        self.id = id
        self.pasword = password

    def __str__(self):
        datos = super().__str__()
        return f"Usuario: {self.id} \n {datos}"

    #Setters and getters para setear y obtener valores de los atributos
    # def setId(self, new_id):
    #     self.__id = new_id
    
    #def getId(self):
    #    return self.__id
    
    # def setPassword(self, new_password):
    #     self.__pasword = new_password
    
    # def getPassword(self):
    #     return self.__pasword
    
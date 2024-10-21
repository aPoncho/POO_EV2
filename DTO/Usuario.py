#clase no implementada
#subclase de Persona

class Usuario():
    def __init__(self, id, password):
        #atributos privados (no se puede acceder a ellos fuera de la clase)
        self.__id = id
        self.__pasword = password

    #Setters and getters para setear y obtener valores de los atributos
    def setId(self, new_id):
        self.__id = new_id
    
    def getId(self):
        return self.__id
    
    def setPassword(self, new_password):
        self.__pasword = new_password
    
    def getPassword(self):
        return self.__pasword
from my_package.DTO.Persona import Persona
from my_package.DAO.Conexion import Conexion
import bcrypt

host='localhost'
user='userempresa'
password='V3ntana.13'
db='empresa'

class Usuario(Persona):
    def __init__(self, nombre, apellido, correo, username, password_hash, tipo_usuario):
        super().__init__(nombre, apellido, correo)
        #atributos deberian privados (no se puede acceder a ellos fuera de la clase)
        self.username = username
        self.password_hash = password_hash
        self.tipo_usuario = tipo_usuario

    def __str__(self):
        datos = super().__str__()
        return f"Usuario: {self.username} -- {self.tipo_usuario} -- {self.nombre} {self.apellido}"

    @staticmethod
    def login(username, password):
        host='localhost'
        user='userempresa'
        con_password='V3ntana.13'
        db='empresa'
        try:
            #FIIIIIIXXXX
            con = Conexion(host, user, con_password, db)
            usuario_data = con.obtener_usuario(username)
            print(usuario_data)
            if usuario_data:
                hashed_password = usuario_data[2].encode('utf-8')
                
                if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
                    return Usuario(
                        nombre = usuario_data[3],
                        apellido = usuario_data[4],
                        correo = usuario_data[5],
                        username = usuario_data[1],
                        password_hash = usuario_data[2],
                        tipo_usuario = usuario_data[6]
                    )
            else:
                input('usuario no encontrado')    
                return None
        except:
            print ('ERROR')
            return None
        
    @staticmethod
    def registrar_usuario(username, password, nombre, apellido, email, tipo_usuario):
        try:
            host='localhost'
            user='userempresa'
            password_con='V3ntana.13'
            db='empresa'
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

            nuevo_usuario = Usuario(nombre, apellido, email, username, hashed_password, tipo_usuario)

            con = Conexion(host, user, password_con, db)
            exito = con.agregarUsuario(nuevo_usuario.username, nuevo_usuario.password_hash.decode('utf-8'), 
                                    nuevo_usuario.nombre, nuevo_usuario.apellido, 
                                    nuevo_usuario.correo, nuevo_usuario.tipo_usuario)

            if exito:
                print("¡Usuario registrado exitosamente!")
                return nuevo_usuario
            
            else:
                print("Error al registrar el usuario.")
                return None
        except:
            print('Error inesperado, revise la conexion con la base de datos')

     
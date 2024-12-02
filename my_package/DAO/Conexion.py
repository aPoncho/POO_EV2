import pymysql
import bcrypt

class Conexion:
    def __init__(self, host, user, password, db):
        self.db = pymysql.connect(
            host=host,
            user=user,
            password=password,
            db=db)
        self.cursor = self.db.cursor()

    def ejecuta_query(self, sql):
        self.cursor.execute(sql)
        return self.cursor

    def desconectar(self):
        self.db.close()

    def commit(self):
        self.db.commit()

    def rollback(self):
        self.db.rollback()

    def obtener_usuario(self, username):
        try:
            sql = f"SELECT * FROM usuarios WHERE username = '{username}'"
            cursor = self.ejecuta_query(sql)
            datos = cursor.fetchone()
            return datos
        except Exception as e:
            print(e)

    def agregarUsuario(self, username, password_hash, nombre, apellidos, email, tipo_usuario):
        
        try:
            sql = f"INSERT INTO usuarios (username, password_hash, nombre, apellido, correo, tipo_usuario)" \
                f"VALUES ('{username}', '{password_hash}', '{nombre}', '{apellidos}', '{email}', '{tipo_usuario}')"
            self.ejecuta_query(sql)
            self.commit()
            return True
        except Exception as e:
            input(f"Error al ejecutar la consulta. Error: {e} ")
            self.rollback()
            return False
        

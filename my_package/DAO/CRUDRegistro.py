from my_package.DAO.Conexion import Conexion



host='localhost'
user='userempresa'
password='V3ntana.13'
db='empresa'


class GestionRegistros():
    def __init__(self, registros):
        self.registros = registros
    
    def agregar(r):
        try:
            con= Conexion(host, user, password, db)
            sql= "INSERT INTO registro_de_tiempo SET Fecha_r='{}', Cantidad_horas={}, Descripcion_r='{}', ID_EMPLEADO={}".format(r.fecha_registro, r.cantidad_horas, r.descripcion_registro, r.id_empleado)
            con.ejecuta_query(sql)
            con.commit()
            input("\n\n Datos Ingresados Satisfactoreamente")
            con.desconectar()
        except Exception as i:
            print(i)


    def eliminar(id):
        try:
            con=Conexion(host, user, password, db)
            sql= "DELETE FROM registro_de_tiempo WHERE ID_reg_tiempo={}".format(id)
            con.ejecuta_query(sql)
            con.commit()
            input("\n \n Registro de tiempo Elimindado satisfactoreamente")
            con.desconectar()
        except Exception as i:
            print(i)


    def editar(r):
        try:
            con=Conexion(host, user, password, db)
            sql="UPDATE registro_de_tiempo SET Fecha_r={}, Cantidad_horas='{}', Descripcion_r='{}', ID_EMPLEADO={} WHERE ID_reg_tiempo={} ".format(r[1],r[2],r[3],r[4],r[0])
            con.ejecuta_query(sql)
            con.commit()
            input("\n \n Datos modificados satisfactoreamente")
            con.desconectar()
        except Exception as i:
            print(i)



    def obtener_todos():
        try:
            con=Conexion(host, user, password, db)
            sql= "SELECT * FROM registro_de_tiempo"
            cursor=con.ejecuta_query(sql)
            datos=cursor.fetchall()
            con.desconectar()
            return datos
        except Exception as i:
            con.rollback()
            print(i)


    def obtener_uno(id):
        try:
            con=Conexion(host, user, password, db)
            sql="select * from registro_de_tiempo where ID_reg_tiempo={}".format(id)
            cursor=con.ejecuta_query(sql)
            datos=cursor.fetchone()
            con.desconectar()
            return datos
        except Exception as i:
            con.rollback()
            print(i)


    def consulta_empleado(id):
        try:
            con=Conexion(host, user, password, db)
            sql="select * from registro_de_tiempo where ID_EMPLEADO={}".format(id)
            cursor=con.ejecuta_query(sql)
            datos=cursor.fetchall()
            con.desconectar()
            return datos
        except Exception as i:
            con.rollback()
            print(i)

    def consulta_cantidad(id):
        try:
            con=Conexion(host, user, password, db)
            sql="select COUNT(*) cantidad from registro_de_tiempo where ID_EMPLEADO={}".format(id)
            cursor=con.ejecuta_query(sql)
            datos=cursor.fetchone()
            con.desconectar()
            return datos
        except Exception as i:
            con.rollback()
            print(i)

    def eliminar_registro_empleado(id):
        try:
            con=Conexion(host, user, password, db)
            sql= "DELETE FROM registro_de_tiempo WHERE ID_EMPLEADO={}".format(id)
            con.ejecuta_query(sql)
            con.commit()
            input("\n \n Registro de tiempo Elimindado satisfactoreamente")
            con.desconectar()
        except Exception as i:
            print(i)
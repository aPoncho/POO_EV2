from DAO.Conexion import Conexion



host='localhost'
user='userempresa'
password='V3ntana.13'
db='empresa'



def agregar(r):
    try:
        con= Conexion(host, user, password, db)
        sql= "INSERT INTO registro_de_tiempo SET Fecha_r={}, Cantidad_horas={}, Descripcion_r='{}'".format(r.fecha_registro, r.cantidad_horas, r.descripcion_registro)
        con.ejecuta_query(sql)
        con.commit()
        input("\n\n Datos Ingresados Satisfactoreamente")
        con.desconectar()
    except Exception as i:
        print(i)


def eliminar(id):
    try:
        con=Conexion(host, user, password, db)
        sql= "DELETE FROM registro_de_tiempo WHERE id={}".format(id)
        con.ejecuta_query(sql)
        con.commit()
        input("\n \n Cliente Elimindado satisfactoreamente")
    except Exception as i:
        print(i)


def mostrartodos():
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


def consultaparticular(id):
    try:
        con=Conexion(host, user, password, db)
        sql="select * from registro_de_tiempo where id={}".format(id)
        cursor=con.ejecuta_query(sql)
        datos=cursor.fetchone()
        con.desconectar()
        return datos
    except Exception as i:
        con.rollback()
        print(i)
from DAO.Conexion import Conexion



host='localhost'
user='userempresa'
password='V3ntana.13'
db='empresa'



def agregar(p):
    try:
        con= Conexion(host, user, password, db)
        sql= "INSERT INTO proyectos SET Nombre_p='{}', Descripcion_p='{}',Fecha_inicio_p='{}'".format(p.nombre_proyecto,p.descripcion_proyecto,p.fecha_inicio_proyecto)
        con.ejecuta_query(sql)
        con.commit()
        input("\n\n Datos Ingresados Satisfactoreamente")
        con.desconectar()
    except Exception as i:
        print(i)


def eliminar(id):
    try:
        con=Conexion(host, user, password, db)
        sql= "DELETE FROM proyectos WHERE id={}".format(id)
        con.ejecuta_query(sql)
        con.commit()
        input("\n \n Cliente Elimindado satisfactoreamente")
    except Exception as i:
        print(i)


def mostrartodos():
    try:
        con=Conexion(host, user, password, db)
        sql= "SELECT * FROM proyectos "
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
        sql="select * from proyectos where id={}".format(id)
        cursor=con.ejecuta_query(sql)
        datos=cursor.fetchone()
        con.desconectar()
        return datos
    except Exception as i:
        con.rollback()
        print(i)
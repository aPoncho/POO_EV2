from DAO.Conexion import Conexion



host='localhost'
user='userempresa'
password='V3ntana.13'
db='empresa'



def agregar(d):
    try:
        con= Conexion(host, user, password, db)
        sql= "INSERT INTO departamentos VALUES Nombre_d='{}', Ubicacion_d='{}',Gerente_d='{}'".format(d.nombre_departamento, d.ubicacion_departamento, d.gerente_departamento)
        con.ejecuta_query(sql)
        con.commit()
        input("\n\n Datos Ingresados Satisfactoreamente")
        con.desconectar()
    except Exception as i:
        print(i)


def eliminar(id):
    try:
        con=Conexion(host, user, password, db)
        sql= "DELETE FROM departamentos WHERE id={}".format(id)
        con.ejecuta_query(sql)
        con.commit()
        input("\n \n Cliente Elimindado satisfactoreamente")
    except Exception as i:
        print(i)


def mostrartodos():
    try:
        con=Conexion(host, user, password, db)
        sql= "SELECT * FROM departamentos "
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
        sql="select * from resgistro_de_tiempo where id={}".format(id)
        cursor=con.ejecuta_query(sql)
        datos=cursor.fetchone()
        con.desconectar()
        return datos
    except Exception as i:
        con.rollback()
        print(i)
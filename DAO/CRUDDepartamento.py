from DAO.Conexion import Conexion



host='localhost'
user='userempresa'
password='V3ntana.13'
db='empresa'



def agregar(d):
    try:
        con= Conexion(host, user, password, db)
        sql= "INSERT INTO departamentos SET Nombre_d='{}', Ubicacion_d='{}',Gerente_d='{}'".format(d.nombre_departamento, d.ubicacion_departamento, d.gerente_departamento)
        con.ejecuta_query(sql)
        con.commit()
        input("\n\n Datos Ingresados Satisfactoreamente")
        con.desconectar()
    except Exception as i:
        print(i)


def eliminar(id):
    try:
        con=Conexion(host, user, password, db)
        sql= "DELETE FROM departamentos WHERE ID_departamento={}".format(id)
        con.ejecuta_query(sql)
        con.commit()
        input("\n \n Departamento Elimindado satisfactoreamente")
    except Exception as i:
        print(i)


def editar(d):
    try:
        con=Conexion(host, user, password, db)
        sql="UPDATE departamentos SET Nombre_d='{}', Ubicacion_d='{}', Gerente_d='{}' WHERE ID_departamento={} ".format(d[1],d[2],d[3],d[0])
        con.ejecuta_query(sql)
        con.commit()
        input("\n \n Datos modificados satisfactoreamente")
        con.desconectar()
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
        sql="select * from departamentos where ID_departamento={}".format(id)
        cursor=con.ejecuta_query(sql)
        datos=cursor.fetchone()
        con.desconectar()
        return datos
    except Exception as i:
        con.rollback()
        print(i)
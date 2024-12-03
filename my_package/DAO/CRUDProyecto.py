from my_package.DAO.Conexion import Conexion



host='localhost'
user='userempresa'
password='V3ntana.13'
db='empresa'


class GestionProyectos():
    def __init__(self, proyectos):
        self.proyectos = proyectos

    def agregar(p):
        try:
            con= Conexion(host, user, password, db)
            sql= "INSERT INTO proyectos SET Nombre_p='{}', Descripcion_p='{}',Fecha_inicio_p='{}', ID_DEPARTAMENTO={}".format(p.nombre_proyecto,p.descripcion_proyecto,p.fecha_inicio_proyecto,p.id_depto)
            con.ejecuta_query(sql)
            con.commit()
            input("\n\n Datos Ingresados Satisfactoreamente")
            con.desconectar()
        except Exception as i:
            print(i)


    def eliminar(id):
        try:
            con=Conexion(host, user, password, db)
            sql= "DELETE FROM proyectos WHERE ID_proyecto={}".format(id)
            con.ejecuta_query(sql)
            con.commit()
            input("\n \n Proyecto Elimindado satisfactoreamente")
        except Exception as i:
            print(i)


    def editar(p):
        try:
            con=Conexion(host, user, password, db)
            sql="UPDATE proyectos SET Nombre_p='{}', Descripcion_p='{}', Fecha_inicio_p={}, ID_DEPARTAMENTO={} WHERE ID_proyecto={} ".format(p[1],p[2],p[3],p[4],p[0])
            con.ejecuta_query(sql)
            con.commit()
            input("\n \n Datos modificados satisfactoreamente")
            con.desconectar()
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
            sql="select * from proyectos where ID_proyecto={}".format(id)
            cursor=con.ejecuta_query(sql)
            datos=cursor.fetchone()
            con.desconectar()
            return datos
        except Exception as i:
            con.rollback()
            print(i)

        
    def consulta_dpto(id):
        try:
            con=Conexion(host, user, password, db)
            sql="select * from proyectos where ID_DEPARTAMENTO={}".format(id)
            cursor=con.ejecuta_query(sql)
            datos=cursor.fetchone()
            con.desconectar()
            return datos
        except Exception as i:
            con.rollback()
            print(i)
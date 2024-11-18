from my_package.DAO.Conexion import Conexion



host='localhost'
user='userempresa'
password='V3ntana.13'
db='empresa'

class GestionDepartamentos():

    def __init__(self, departamentos):
        self.departamentos = departamentos

    def __str__(self):
        if self.departamentos == None:
            return "No hay empleados en la base de datos"
        else:
            string = '''================================\nMUESTRA DE TODOS LOS DEPARTAMENTOS \n================================\n'''
            for dato in self.departamentos:
                depto = " ID : {} - NOMBRE : {} - UBICACION: {} - GERENTE : {} \n\n".format(dato[0], dato[1], dato[2], dato[3])
                string += depto
            return string
        
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


    def obtener_todos():
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


    def obtener_uno(id):
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

    def consulta_parcial(cant):
        try:
            con=Conexion(host, user, password, db)
            sql="select * from departamentos"
            cursor= con.ejecuta_query(sql)
            datos=cursor.fetchmany(cant)
            con.desconectar()
            return datos
        except Exception as i:
            con.rollback()
            print(i)

    def cantidad_empleados(id_depto):
        try:
            con=Conexion(host, user, password, db)
            sql= "Select count(ID_empleado) From empleados WHERE Departamento_e={}".format(id_depto)
            valor = con.ejecuta_query(sql)
            ct_depto = valor.fetchone()[0]
            return ct_depto
        except Exception as i:
            print(i)


    def cantidad_proyectos(id_depto):
        try:
            con=Conexion(host, user, password, db)
            sql= "Select count(ID_proyecto) From proyectos WHERE ID_departamento={}".format(id_depto)
            valor = con.ejecuta_query(sql)
            ct_depto_p = valor.fetchone()[0]
            return ct_depto_p
        except Exception as i:
            print(i)


    def elim_depto_empleado(id_empleado):
        try:
            con=Conexion(host, user, password, db)
            sql= "Delete From departamentos WHERE Departamento_e={}".format(id_empleado)
            con.ejecuta_query(sql)
            con.commit()
            input("\n \n Empleados Elimindados satisfactoreamente")
        except Exception as i:
            print(i)
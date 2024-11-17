from my_package.DAO.Conexion import Conexion



host='localhost'
user='userempresa'
password='V3ntana.13'
db='empresa'

class GestionEmpleados():

    def __init__(self, empleados):
        self.empleados = empleados

    def __str__(self):
        if len(self.empleados) == 0:
            return "No hay empleados"
        else:
            string = '''================================\nMUESTRA DE TODOS LOS EMPLEADOS \n================================\n'''
            for dato in self.empleados:            
                empleado = '''ID : {} - RUN : {} - NOMBRE : {} - APELLIDO : {} - DIRECCION : {} - FONO : {} - CORREO : {} - CARGO : {} - SALARIO : {} - DEPARTAMENTO : {} \n\n'''.format(dato[0], dato[1], dato[2], dato[3], dato[4], dato[5], dato[6], dato[7], dato[8], dato[9])
                string += empleado 
            return string   

    def agregar(e):
        try:
            con= Conexion(host, user, password, db)
            sql= "INSERT INTO empleados SET RUT_e='{}', Nombre_e='{}', Apellido_e='{}', Direccion_e='{}',"\
            "Fono_e={},Correo_e='{}',Cargo_e='{}',Salario_e={} ,Departamento_e={}".format(e.run,e.nombre,e.apellido,e.direccion,e.fono,e.correo,e.cargo,e.salario,e.depto)
            con.ejecuta_query(sql)
            con.commit()
            input("\n\n Datos Ingresados Satisfactoreamente")
            con.desconectar()
        except Exception as i:
            print(i)
            input("presione una tecla...")
        
    def editar(e):
        try:
            con=Conexion(host, user, password, db)
            sql="UPDATE empleados SET RUT_e='{}', Nombre_e='{}', Apellido_e='{}', Direccion_e='{}', Fono_e={}, Correo_e='{}',"\
                "Cargo_e='{}',Salario_e={},Departamento_e={} WHERE ID_empleado={} ".format(e[1],e[2],e[3],e[4],e[5],e[6],e[7],e[8],e[9],e[0])
            con.ejecuta_query(sql)
            con.commit()
            input("\n \n Datos modificados satisfactoreamente")
            con.desconectar()
        except Exception as i:
            print(i)

    def eliminar(id):
        try:
            con=Conexion(host, user, password, db)
            sql= "DELETE FROM empleados WHERE ID_empleado={}".format(id)
            con.ejecuta_query(sql)
            con.commit()
            input("\n \n Empleado Elimindado satisfactoreamente")
        except Exception as i:
            print(i)

    def obtener_todos():
        try:
            con=Conexion(host, user, password, db)
            sql= "SELECT * FROM empleados "
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
            sql="select * from empleados where ID_empleado={}".format(id)
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
            sql="select * from empleados"
            cursor= con.ejecuta_query(sql)
            datos=cursor.fetchmany(cant)
            con.desconectar()
            return datos
        except Exception as i:
            con.rollback()
            print(i)


    def consulta_dpto(id):
        try:
            con=Conexion(host, user, password, db)
            sql="select * from empleados where Departamento_e={}".format(id)
            cursor=con.ejecuta_query(sql)
            datos=cursor.fetchone()
            con.desconectar()
            return datos
        except Exception as i:
            con.rollback()
            print(i)

    def cantidad_registros(id_depto):
        try:
            con=Conexion(host, user, password, db)
            sql= "Select count(ID_reg_tiempo) From registro_de_tiempo WHERE ID_EMPLEADO={}".format(id_depto)
            valor = con.ejecuta_query(sql)
            ct_depto_e = valor.fetchone()[0]
            return ct_depto_e
        except Exception as i:
            print(i)
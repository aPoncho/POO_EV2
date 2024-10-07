from DAO.Conexion import Conexion



host='localhost'
user='userempresa'
password='V3ntana.13'
db='empresa'


def agregar(e):
    try:
        con= Conexion(host, user, password, db)
        sql= "INSERT INTO empleados SET RUT_e='{}', Nombre_e='{}', Apellido_e='{}', Direccion_e='{}',"\
        "Fono_e={},Correo_e='{}',Cargo_e='{}',Salario_e={} ,Departamento_e='{}'".format(e.run,e.nombre,e.apellido,e.direccion,e.fono,e.correo,e.cargo,e.salario,e.depto)
        con.ejecuta_query(sql)
        con.commit()
        input("\n\n Datos Ingresados Satisfactoreamente")
        con.desconectar()
    except Exception as i:
        print(i)
    
def editar(e):
    try:
        con=Conexion(host, user, password, db)
        sql="UPDATE empleados SET RUT='{}', Nombre_e='{}', Apellido_e='{}', Direccion_e='{}', Fono_e={}, Correo_e='{}',"\
            "Cargo_e='{}',Salario_e={},Departamento_e='{}' WHERE id={} ".format(c[1],c[2],c[3],[4],c[5],c[6],c[7],c[8],c[9],c[0])
        con.ejecuta_query(sql)
        con.commit()
        input("\n \n Datos modificados satisfactoreamente")
        con.desconectar()
    except Exception as e:
        print(e)

def eliminar(id):
    try:
        con=Conexion(host, user, password, db)
        sql= "DELETE FROM empleados WHERE id={}".format(id)
        con.ejecuta_query(sql)
        con.commit()
        input("\n \n Empleado Elimindado satisfactoreamente")
    except Exception as i:
        print(i)

def mostrartodos():
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

def consultaparticular(id):
    try:
        con=Conexion(host, user, password, db)
        sql="select * from empleados where id={}".format(id)
        cursor=con.ejecuta_query(sql)
        datos=cursor.fetchone()
        con.desconectar()
        return datos
    except Exception as i:
        con.rollback()
        print(i)

def consultaparcial(cant):
    try:
        con=Conexion(host, user, password, db)
        sql="select * from empleados"
        cursor= con.ejecuta_query(sql)
        datos=cursor.fetchmany(size-cant)
        con.desconectar()
        return datos
    except Exception as i:
        con.rollback()
        print(i)



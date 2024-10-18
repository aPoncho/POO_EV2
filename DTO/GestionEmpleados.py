import DAO.CRUDEmpleado
import time

class GestionEmpleados():
    def __init__(self):
        self.empleados = DAO.CRUDEmpleado.obtener_todos()

    def __str__(self):  
        string = '''================================
 MUESTRA DE TODOS LOS EMPLEADOS 
================================\n'''
        for dato in self.empleados:            
            empleado = '''ID : {} - RUN : {} - NOMBRE : {} - APELLIDO : {} - DIRECCION : {} - FONO : {} - CORREO : {} - CARGO : {} - SALARIO : {} - DEPARTAMENTO : {} 
            --------------------------------------------------------------------------------------------------------------------------------------------------------\n'''.format(dato[0], dato[1], dato[2], dato[3], dato[4], dato[5], dato[6], dato[7], dato[8], dato[9])
            string += empleado 
        return string        
    
    def agregar_empleado(self):
        DAO.CRUDEmpleado.agregar(self)

    def mostrar_uno():
        while True:
            try:
                op = int(input("Ingrese valor del ID del empleado que desea Mostrar los Datos : "))
            except ValueError:
                print("Ingrese un numero.")
                time.sleep(2)
                continue
            break        
        empleado = DAO.CRUDEmpleado.obtener_uno(op) 
        return "ID : {} - RUN : {} - NOMBRE : {} - APELLIDO : {} - DIRECCION : {} - FONO : {} - CORREO : {} - CARGO : {} - SALARIO : {} - DEPARTAMENTO : {}".format(empleado[0], empleado[1], empleado[2], empleado[3], empleado[4], empleado[5], empleado[6], empleado[7], empleado[8], empleado[9]) 
    
    def mostrar_parcial():
        cantidad = int(input("\nIngrese la Cantidad de Empleados a Mostrar : "))
        datos = DAO.CRUDEmpleado.consulta_parcial(cantidad)
        return datos
    
    def eliminar_uno():
        while True:
            try:
                eliminar = int(input("Ingrese valor de ID del Empleado que desea Eliminar : "))
            except ValueError:
                print("Ingrese un numero.")
                time.sleep(1)
            DAO.CRUDEmpleado.eliminar(eliminar)
            break
    
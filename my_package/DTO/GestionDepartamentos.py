import my_package.DAO.CRUDDepartamento as CRUDDepartamento
import time

#ESTO DEBE MOVERSE A AL DAO!!!!

class GestionDepartamentos():
    def __init__(self):
        self.departamentos = CRUDDepartamento.obtener_todos()

    def __str__(self):  
        if len(self.departamentos) == 0:
            print("No hay departamentos")
        else:
            string = '''================================\nMUESTRA DE TODOS LOS DEPARTAMENTOS \n================================\n'''
            for dato in self.departamentos:            
                empleado = ''' ID : {} - NOMBRE : {} - UBICACION: {} - GERENTE : {} 
                --------------------------------------------------------------------------------------------------------------------------------------------------------\n'''.format(dato[0], dato[1], dato[2], dato[3])
                string += empleado 
            return string       
        
    def agregar(depto):
        CRUDDepartamento.agregar(depto)

    def mostrar_uno(op):       
        empleado = CRUDDepartamento.obtener_uno(op)
        return empleado
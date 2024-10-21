import DAO.CRUDDepartamento
from DTO.Departamento import Departamento
import time

class GestionDepartamentos():
    def __init__(self, deptos):
        self.departamentos = [DAO.CRUDDepartamento.obtener_todos()]

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
        DAO.CRUDDepartamento.agregar(depto)

    # def mostrar_uno(self):
    #     while True:
    #         try:
    #             op = int(input("Ingrese valor del ID del departamento que desea obtener los Datos : "))
    #         except ValueError:
    #             print("Ingrese un numero.")
    #             time.sleep(2)
    #             continue
    #         break        
    #     datos = self.departamentos[op] 
    #     return datos
    def getDepartamentos(self):
        return self.departamentos
    
    def mostrar_uno_test():
        while True:
            try:
                op = int(input("Ingrese valor del ID del departamento que desea obtener los Datos : "))
            except ValueError:
                print("Ingrese un numero.")
                time.sleep(2)
                continue
            break
        datos = DAO.CRUDDepartamento.obtener_todos()
        departamentos = GestionDepartamentos(datos)
        print(departamentos)
        
        for dato in departamentos:
            print(dato)
            depto = Departamento(dato[0], dato[1], dato[2], dato[3])

            if depto.id == op:
                return print(depto)

            else:
                return print(f'{depto} no coincide')    

   
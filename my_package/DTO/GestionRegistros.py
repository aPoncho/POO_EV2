import my_package.DAO.CRUDRegistro as CRUDRegistro

#ESTO DEBE MOVERSE A AL DAO!!!!

class GestionRegistros():
    def __init__(self):
        self.registros = CRUDRegistro.obtener_todos()

    def __str__(self):
        if len(self.registros) == 0:
            print("No hay registros")
        else:
            string = '''================================\nMUESTRA DE TODOS LOS REGISTROS \n================================\n'''
            for dato in self.registros:            
                empleado = ''' ID : {} - FECHA : {} - CANTIDAD DE HORAS TRABAJADAS : {} - DESCRIPCION : {} - ID EMPLEADO VINCULADO : {} 
                --------------------------------------------------------------------------------------------------------------------------------------------------------\n'''.format(dato[0], dato[1], dato[2], dato[3], dato[4])
                string += empleado 
            return string   
        
    def obtener_por_empleado(id):
        datos = CRUDRegistro.consulta_empleado(id)
        return datos
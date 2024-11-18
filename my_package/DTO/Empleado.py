from my_package.DTO.Persona import Persona
class Empleado(Persona):

    def __init__(self, run, nombre, apellido, direccion, fono, correo, cargo, salario, depto, id = 'NO ID'):
        super().__init__(run, nombre, apellido, direccion, fono, correo)
        self.cargo = cargo
        self.salario = salario
        self.depto = depto
        self.id = id

    def __str__(self):
        datos = super().__str__()
        return f'''
=====================================
   MUESTRA DE DATOS DEL EMPLEADO     
======================================
ID               : {self.id}
{datos}
CARGO            : {self.cargo}
SALARIO          : {self.salario}
ID DEPTO VINCULADO  : {self.depto}
======================================='''


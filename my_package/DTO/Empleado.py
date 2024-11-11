
#se debe implementar clase padre "Persona" para poder usar polimorfismo (quizas en forma de saludo?)
class Empleado():

    def __init__(self, run, nombre, apellido, direccion, fono, correo, cargo, salario, depto, id = 'NO ID'):
        self.id = id
        self.run = run
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion
        self.fono = fono
        self.correo = correo
        self.cargo = cargo
        self.salario = salario
        self.depto = depto

    def __str__(self):
        
        return f'''
=====================================
   MUESTRA DE DATOS DEL EMPLEADO     
======================================
ID               : {self.id}
RUN              : {self.run}
NOMBRE           : {self.nombre}
APELLIDO         : {self.apellido}
DIRECCION        : {self.direccion}
FONO             : {self.fono}
CORREO           : {self.correo}
CARGO            : {self.cargo}
SALARIO          : {self.salario}
ID DEPTO VINCULADO  : {self.depto}
======================================='''
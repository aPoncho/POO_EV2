import os
import time
import DAO.CRUDEmpleado

class Empleado():

    def __init__(self, run, nombre, apellido, direccion, fono, correo, cargo, salario, depto):
        self.run = run
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion
        self.fono = fono
        self.correo = correo
        self.cargo = cargo
        self.salario = salario
        self.depto = depto

    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido}, {self.cargo}"
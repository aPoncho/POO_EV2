import os
from time import sleep
from getpass import getpass
from my_package.DTO.Usuario import Usuario
from my_package.DAO.Conexion import Conexion
from getpass import getpass

host='localhost'
user='userempresa'
password='V3ntana.13'
db='empresa'

def menu_login():
    while True:
        os.system('cls')
        opcion = input("""
                ================================
                    M E N Ú  P R I N C I P A L
                ================================
                        1.- LOGIN
                        2.- REGISTRO
                        3.- SALIR
                ================================""")
        
        if opcion == '1':
            ingreso = login()
            if ingreso == True:
                return True

        elif opcion == '2':
            registrar_usuario()
        elif opcion == '3':
            confirm = input("¿Está seguro que desea salir? si/no")
            if confirm.lower() == 'si':
                print('Hasta luego!')
                sleep(1)
                break
            else:
                continue
        else:
            print("Opcion fuera de rango")


    
def login():
    print("================================")
    print("       LOGIN DE USUARIO       ")
    print("================================")
    while True:
        try:
            username = input("Ingrese nombre de usuario: ")
            password = getpass("Ingrese contraseña: ")
            user = Usuario.login(username, password)            
            if user:
                logged = True
                input(f"Bienvenido/a {user}")
                return True
            else:
                return False

        except:
            input("ERROR")


def registrar_usuario():
    
    
    while True:
        os.system("cls")
        print("================================")
        print("      REGISTRO DE USUARIO       ")
        print("================================")
        host='localhost'
        user='userempresa'
        password='V3ntana.13'
        db='empresa'
        username = input('Ingrese nombre de usuario')
        con = Conexion(host, user, password, db)
        usuario_existente = con.obtener_usuario(username)

        if usuario_existente:
            print("nombre de usuario ya existe")
            seguir = input("¿Desea continuar? Si/No")
            if seguir.lower() == "no":
                break
            else:
                continue
        while True:
            clave1 = getpass("Ingrese contraseña: ")
            clave2 = getpass("Vuelva a escribir la contraseña: ")
            if clave1 == clave2:
                password = clave1
                break
            else:
                print("Las contraseñas no coinciden, reintente")
        
        while True:
            nombre = input('Ingrese nombre: ')
            apellido = input('Ingrese apellido: ')
            if nombre == '' or apellido == '':
                print("nombre y/o apellido no validos")
                continue
            elif nombre.isalpha() == False or apellido.isalpha() == False:
                print("nombre y/o apellido no validos")
                continue
            else:
                break
        while True:
            correo = input('Ingrese correo: ')
            if not correo.endswith("@gmail.com"):
                print('Debe ingresar un correo válido, usando el formato "@gmail.com"')
                continue
            else:
                break

        os.system("cls")
        print("-------- TIPOS DE USUARIOS --------")
        print("     1.- Administrador")
        print("     2.- Usuario")    
        while True:
            try:
                tipo = input("Ingrese numero de opción: ")
                if tipo == '1':
                    tipo = "administrador"
                    break
                elif tipo == '2':
                    tipo = "usuario"
                    break
                else:
                    print("seleccione una opcion valida (1 o 2)")
                    continue
            except:
                print("Numero no valido")
                continue

        user = Usuario.registrar_usuario(username, password, nombre, apellido, correo, tipo)
        break

        

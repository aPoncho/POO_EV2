import os
import time

#import my_package.Modules.Proyectos as modulo_proyectos
import my_package.Modules.Registros as modulo_registros
import my_package.Modules.Departamentos as modulo_departamentos
import my_package.Modules.Empleados as modulo_empleados
import my_package.Modules.Login as modulo_login
import my_package.Modules.Proyectos as modulo_proyectos

def menuprincipal():

    while (True):
        os.system('cls')
        print("===============================")
        print("   M E N Ú  P R I N C I P A L  ")
        print("===============================")
        print("       1.- EMPLEADOS           ")
        print("       2.- PROYECTOS           ")
        print("       3.- REGISTROS           ")
        print("       4.- DEPARTAMENTOS       ")
        print("       5.- SALIR               ")
        print("===============================")
        try:
            op = int(input(" INGRESE OPCION : "))
        except ValueError:
            print("Debe ingresar un número.")
            time.sleep(1)
            os.system("cls")
            continue
        if op == 1:
            modulo_empleados.menuempleados()
        elif op == 2:
            modulo_proyectos.menuproyectos()
            #input("No implementado")
        elif op == 3:
            modulo_registros.menuregistros()
        elif op == 4:
            modulo_departamentos.menudepartamentos()
        elif op == 5:
            op2 = input("DESEA SALIR [SI/NO] :")
            if op2.lower() == "si":
                break
                #exit()
            elif op2.lower() == "no":
                print("Volviendo al menu..")
                time.sleep(1)
                os.system("cls")
                continue
            else:
                print("Opción no válida.")
                time.sleep(1)
                os.system("cls")
                continue
        else:
            print("Opción Fuera de Rango")
            time.sleep(2)
            os.system("cls")

# ----MENU PRINCIPAL----
while (True):
    ingreso = modulo_login.menu_login()
    if ingreso:
        menuprincipal()
    
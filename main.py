import os
import time
import Modules.Proyectos
import Modules.Registros
import Modules.Departamentos
import Modules.Empleados

def menuprincipal():
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

# ----MENU PRINCIPAL----
while (True):
    menuprincipal()
    try:
        op = int(input(" INGRESE OPCION : "))
    except ValueError:
        print("Debe ingresar un número.")
        time.sleep(1)
        os.system("cls")
        continue
    if op == 1:
        Modules.Empleados.menuempleados()
    elif op == 2:
        Modules.Proyectos.menuproyectos()
    elif op == 3:
        Modules.Registros.menuregistros()
    elif op == 4:
        Modules.Departamentos.menudepartamentos()
    elif op == 5:
        op2 = input("DESEA SALIR [SI/NO] :")
        if op2.lower() == "si":
            exit()
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

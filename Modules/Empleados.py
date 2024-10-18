import DAO.CRUDEmpleado
from DTO.Empleado import Empleado
from DTO.GestionEmpleados import GestionEmpleados
import os, time
from datetime import date

# ---- EMPLEADO ----
def menuempleados():
    while (True):
        os.system('cls')
        print("===============================")
        print("   M E N Ú  E M P L E A D O S  ")
        print("===============================")
        print("       1.- INGRESAR            ")
        print("       2.- MOSTRAR             ")
        print("       3.- MODIFICAR           ")
        print("       4.- ELIMINAR            ")
        print("       5.- VOLVER              ")
        print("===============================")

        try:
            op = int(input(" INGRESE OPCION : "))
        except ValueError:
            print("Debe ingresar un número.")
            time.sleep(1)
            os.system("cls")
            continue
        if op == 1:
            ingresardatos_empleados()
        elif op == 2:
            menumostrar_empleados()
        elif op == 3:
            modificardatos_empleados()
        elif op == 4:
            eliminardatos_empleados()
        elif op == 5:
            break
        else:
            print("Opción Fuera de Rango")
            time.sleep(2)
# Ingresar
def menumostrar_empleados():
    while True:
        os.system('cls')
        print("===============================")
        print("    M E N Ú  M O S T R A R     ")
        print("===============================")
        print("       1.- MOSTRAR TODO        ")
        print("       2.- MOSTRAR UNO         ")
        print("       3.- MOSTRAR PARCIAL     ")
        print("       4.- VOLVER              ")
        print("===============================")
        try:
            op = int(input(" INGRESE OPCION : "))
        except ValueError:
            print("Debe ingresar un número.")
            time.sleep(1)
            os.system("cls")
            continue
        if op == 1:
            os.system('cls')
            print(GestionEmpleados())
            os.system("pause")
        elif op == 2:
            print(GestionEmpleados.mostrar_uno())
            os.system("pause")
        elif op == 3:
            mostrarparcial_empleados()
        elif op == 4:
            break
        else:
            print("Opción Fuera de Rango")
            time.sleep(2)

def ingresardatos_empleados():
    os.system('cls')
    print("===============================")
    print("    INGRESAR DATOS EMPLEADO    ")
    print("===============================")
    while True:
        run = input("INGRESE RUN : ")
        if len(run) != 9 or not run.isdigit():
            print("El RUN debe ser 9 dígitos.")
            time.sleep(1)
            continue
        break

    while True:
        nombre=input("INGRESE NOMBRE : ")
        if not nombre.isalpha():
            print("Debe ingresar un nombre válido.")
            time.sleep(1)
            continue
        else:
            break

    while True:
        apellido=input("INGRESE APELLIDO : ")
        if not apellido.isalpha():
            print("Debe ingresar un apellido válido.")
            time.sleep(1)
            continue
        else:
            break

    while True:
        direccion=input("INGRESE DIRECCION : ")
        if "#" in direccion:
            break
        else:
            print('Debe ingresar la dirección con el formato "Nombre Calle, #Número"')
            time.sleep(1)
            continue

    while True:
        try:
            fono=int(input("INGRESE TELEFONO : "))
            fono_str = str(fono)
            if len(fono_str) !=11:
                print("El télefono ingresado debe tener 11 dígitos.")
                continue
            else:
                break
        except ValueError:
            print("Debe ingresar dígitos.")

    while True:
        correo=input("INGRESE CORREO : ")
        if not correo.endswith("@gmail.com"):
            print('Debe ingresar un correo válido, usando el formato "@gmail.com"')
            continue
        else:
            break

    while True:
        cargo=input("INGRESE CARGO : ")
        if not nombre.isalpha():
            print("Debe ingresar un cargo válido.")
            time.sleep(1)
            continue
        else:
            break

    while True:
        try:
            salario = int(input("INGRESE SALARIO : "))
        except ValueError:
            print("Por favor ingrese un numero")
            time.sleep(2)
            continue
        else:
            break
    print("====================================")
    print(" MUESTRA DE TODOS LOS DEPARTAMENTOS ")
    print("====================================")
    datos = DAO.CRUDDepartamento.mostrartodos()
    if len(datos) == 0:
        print("No hay departamentos en la base de datos ")
        time.sleep(1)
        print("Volviendo...")
        time.sleep(2)
        menuempleados()
    else:
        for dato in datos:
            print(
                " ID : {} - NOMBRE : {} - UBICACION: {} - GERENTE : {} ".format(dato[0], dato[1], dato[2], dato[3]))
            print("--------------------------------------------------------------------------------------------------------------------------------------------------------")
    time.sleep(2)
    while True:
        try:
            opcion = int(input("INGRESE ID DE DEPARTAMENTO : "))
            datos = DAO.CRUDDepartamento.consultaparticular(opcion)
            if datos is None:
                print(" No hay departamentos con ese id ")
                continue
            else:
                depto = datos[0]
                break
        except ValueError:
            print("Ingrese un numero.")
            time.sleep(2)
            continue

    nuevo_empleado = Empleado(run, nombre, apellido, direccion, fono, correo, cargo, salario, depto)
    GestionEmpleados.agregar_empleado(nuevo_empleado)

def mostraruno_empleados():
    while True:
        os.system('cls')
        print("===============================")
        print("  MUESTRA DE DATOS PARTICULAR  ")
        print("===============================")
        try:
            op = int(input("Ingrese valor del ID del empleado que desea Mostrar los Datos : "))
        except ValueError:
            print("Ingrese un numero.")
            time.sleep(2)
            continue
        break
    print(GestionEmpleados.mostrar_uno(op))
    input("\n\n PRESIONE ENTER PARA CONTINUAR")

def mostrarparcial_empleados():
    os.system('cls')
    print("=======================================")
    print("   MUESTRA PARCIALMENTE LOS EMPLEADOS  ")
    print("=======================================")
    datos = GestionEmpleados.mostrar_parcial()
    for dato in datos:
        print(
            " ID : {} - RUN : {} - NOMBRE : {} - APELLIDO : {} - DIRECCION : {} - FONO : {} - CORREO : {} - MONTO CREDITO : {} - DEUDA : {} - TIPO : {} ".format(dato[0], dato[1], dato[2], dato[3], dato[4], dato[5], dato[6], dato[7], dato[8], dato[9]))
    input("\n\n PRESIONE CUALQUIER TECLA PARA CONTINUAR")
# Modificar datos
def modificardatos_empleados():
    os.system('cls')
    listanuevos = []
    print("========================================")
    print("       MODULO MODIFICAR EMPLEADOS       ")
    print("========================================")
    datos = GestionEmpleados()
    if len(datos) == 0:
        print("No hay empleados en la base de datos ")
        time.sleep(2)
        return
    print(GestionEmpleados())
    mod = int(input("Ingrese valor de ID del Empleado que desea Modificar: "))
    datos = GestionEmpleados.mostrar_uno(mod)

    print("\n ID         : {}".format(datos[0]))
    listanuevos.append(datos[0])
    print("\n RUN        : {}".format(datos[1]))
    listanuevos.append(datos[1])

    opm = input("DESEA MODIFICAR EL NOMBRE : {} - [SI/NO] ".format(datos[2]))
    if opm.lower() == "si":
        while True:
            nombrenuevo=input("INGRESE NOMBRE : ")
            if not nombrenuevo.isalpha():
                print("Debe ingresar un nombre válido.")
                continue
            else:
                listanuevos.append(nombrenuevo)
                break
    else:
        listanuevos.append(datos[2])

    opm = input("DESEA MODIFICAR EL APELLIDO : {} - [SI/NO] ".format(datos[3]))
    if opm.lower() == "si":
        while True:
            apellidonuevo= input("INGRESE APELLIDO : ")
            if not apellidonuevo.isalpha():
                print("Debe ingresar un apellido válido.")
                continue
            else:
                listanuevos.append(apellidonuevo)
                break
    else:
        listanuevos.append(datos[3])

    opm = input("DESEA MODIFICAR LA DIRECCION : {} - [SI/NO] ".format(datos[4]))
    if opm.lower() == "si":
        while True: 
            direcnuevo = input("INGRESE DIRECCION : ")
            if "#" in direcnuevo:
                break
            else:
                print('Debe ingresar la dirección con el formato "Nombre Calle, #Número"')
                continue
            listanuevos.append(direcnuevo)
    else:
        listanuevos.append(datos[4])

    opm = input("DESEA MODIFICAR EL TELEFONO : {} - [SI/NO] ".format(datos[5]))
    if opm.lower() == "si":
        while True: 
            try:
                fononuevo= input("INGRESE TELEFONO : ")
            except ValueError:
                print("Debe ingresar dígitos.")
                continue
            fononuevo_str = str(fononuevo)
            if len(fononuevo_str) != 11:
                    print("El télefono ingresado debe tener 11 dígitos.")
                    continue
            else:
                listanuevos.append(fononuevo_str)
    else:
        listanuevos.append(datos[5])

    opm = input("DESEA MODIFICAR EL CORREO : {} - [SI/NO] ".format(datos[6]))
    if opm.lower() == "si":
        while True: 
            correonuevo = input("INGRESE EL CORREO : ")
            if not correonuevo.endswith("@gmail.com"):
                print('Debe ingresar un correo válido, usando el formato "@gmail.com"')
                continue
            else:
                listanuevos.append(correonuevo)
                break
    else:
        listanuevos.append(datos[6])

    opm = input("DESEA MODIFICAR LA CARGO : {} - [SI/NO] ".format(datos[7]))
    if opm.lower() == "si":
        cargonuevo=input("INGRESE CARGO : ")
        listanuevos.append(cargonuevo)
    else:
        listanuevos.append(datos[7])

    opm = input("DESEA MODIFICAR EL MONTO DE SALARIO : {} - [SI/NO] ".format(datos[8]))
    if opm.lower() == "si":
            while True: 
                salarionuevo= input("INGRESE MONTO DE SALARIO : ")
                try:
                    salarionuevo_int = int(salarionuevo)
                except ValueError:
                    print("Debe ingresar un valor válido.")
                    continue
                break        
            listanuevos.append(salarionuevo_int)
    else:
        listanuevos.append(datos[8])


    opm = input("DESEA MODIFICAR EL DEPARTAMENTO : {} - [SI/NO] ".format(datos[9]))
    if opm.lower() == "si":
        departamentonuevo=input("INGRESE DEPARTAMENTO : ")
        listanuevos.append(departamentonuevo)
    else:
        listanuevos.append(datos[9])
    DAO.CRUDEmpleado.editar(listanuevos)
# Eliminar datos
def eliminardatos_empleados():
    os.system('cls')
    print("=========================================")
    print("       MODULO ELIMINAR EMPLEADOS         ")
    print("=========================================")

    datos = GestionEmpleados()
    if len(datos) == 0:
        print("No hay Empleados en la base de datos ")
        time.sleep(2)
        os.system("pause")
        return
    else:
        print(GestionEmpleados())
        GestionEmpleados.eliminar_uno()
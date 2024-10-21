import DAO.CRUDEmpleado
from DTO.Empleado import Empleado
from DTO.GestionEmpleados import GestionEmpleados
import os, time
from datetime import date

#importacion provisional
import DAO.CRUDDepartamento

def eliminar_varios(id_depto):
        datos = [DAO.CRUDEmpleado.consulta_dpto(id_depto)]
        lista_id = []
        for dato in datos:
            lista_id.append(dato[0])
        for id in lista_id:
            DAO.CRUDEmpleado.eliminar(id)

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
            mostrartodo_empleados()
        elif op == 2:
            mostraruno_empleados()
        elif op == 3:
            mostrarparcial_empleados()
        elif op == 4:
            break
        else:
            print("Opción Fuera de Rango")
            time.sleep(2)
# Mostrar
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
    datos = GestionEmpleados()
    if len(datos) == 0:
        print("No hay departamentos en la base de datos ")
        time.sleep(1)
        print("Volviendo...")
        time.sleep(2)
        return
    else:
        for dato in datos:
            print(
                " ID : {} - NOMBRE : {} - UBICACION: {} - GERENTE : {} ".format(dato[0], dato[1], dato[2], dato[3]))
            print("--------------------------------------------------------------------------------------------------------------------------------------------------------")
    time.sleep(2)
    while True:
        try:
            opcion = int(input("INGRESE ID DE DEPARTAMENTO AL QUE DESEA VINCULAR: "))
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
    e = Empleado(run, nombre, apellido, direccion, fono, correo, cargo, salario, depto)
    GestionEmpleados.agregar_empleado(e)

def mostrartodo_empleados():
    os.system('cls')
    print(GestionEmpleados())
    # print("================================")
    # print(" MUESTRA DE TODOS LOS EMPLEADOS ")
    # print("================================")
    # datos = DAO.CRUDEmpleado.mostrartodos()
    # if len(datos) == 0:
    #     print("No hay empleados en la base de datos ")
    # else:
    #     for dato in datos:
    #         print(
    #             " ID : {} - RUN : {} - NOMBRE : {} - APELLIDO : {} - DIRECCION : {} - FONO : {} - CORREO : {} - CARGO : {} - SALARIO : {} - ID DEPARTAMENTO VINCULADO : {} ".format(dato[0], dato[1], dato[2], dato[3], dato[4], dato[5], dato[6], dato[7], dato[8], dato[9]))
    #         print("--------------------------------------------------------------------------------------------------------------------------------------------------------")
    # time.sleep(2)
    os.system("pause")

def mostraruno_empleados():
    #while True:
    os.system('cls')
    print("===============================")
    print("  MUESTRA DE DATOS PARTICULAR  ")
    print("===============================")
        # try:
        #     op = int(input("Ingrese valor del ID del empleado que desea Mostrar los Datos : "))
        # except ValueError:
        #     print("Ingrese un numero.")
        #     time.sleep(2)
        #     continue
    print(GestionEmpleados.mostrar_uno())
        #break
        
    # if datos is None:
    #     print(" No hay proyectos con ese id ")
    # else:
    #     print("\n=====================================")
    #     print("     MUESTRA DE DATOS DEL EMPLEADO     ")
    #     print("=======================================")
    #     print(" ID               : {}".format(datos[0]))
    #     print(" RUN              : {}".format(datos[1]))
    #     print(" NOMBRE           : {}".format(datos[2]))
    #     print(" APELLIDO         : {}".format(datos[3]))
    #     print(" DIRECCION        : {}".format(datos[4]))
    #     print(" FONO             : {}".format(datos[5]))
    #     print(" CORREO           : {}".format(datos[6]))
    #     print(" CARGO            : {}".format(datos[7]))
    #     print(" SALARIO          : {}".format(datos[8]))
    #     print(" ID DEPTO VINCULADO  : {}".format(datos[9]))
    #     print("=======================================")
    input("\n\n PRESIONE ENTER PARA CONTINUAR")

def mostrarparcial_empleados():
    os.system('cls')
    print("=======================================")
    print("   MUESTRA PARCIALMENTE LOS CLIENTES   ")
    print("=======================================")
    datos = GestionEmpleados.mostrar_parcial()
    for dato in datos:
        print(
            " ID : {} - RUN : {} - NOMBRE : {} - APELLIDO : {} - DIRECCION : {} - FONO : {} - CORREO : {} - MONTO CREDITO : {} - DEUDA : {} - TIPO : {} ".format(dato[0], dato[1], dato[2], dato[3], dato[4], dato[5], dato[6], dato[7], dato[8], dato[9]))
    input("\n\n PRESIONE ENTER PARA CONTINUAR")
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

    #mejorable??
    print("\n ID         : {}".format(datos[0]))
    listanuevos.append(datos[0])
    print("\n RUN        : {}".format(datos[1]))
    listanuevos.append(datos[1])

    opm = input("DESEA MODIFICAR EL NOMBRE : {} - [SI/NO] ".format(datos[2]))
    if opm.lower() == "si":
        while True:
            nombre_nuevo=input("INGRESE NOMBRE : ")
            if not nombre_nuevo.isalpha():
                print("Debe ingresar un nombre válido.")
                continue
            else:
                listanuevos.append(nombre_nuevo)
                break
    else:
        listanuevos.append(datos[2])

    opm = input("DESEA MODIFICAR EL APELLIDO : {} - [SI/NO] ".format(datos[3]))
    if opm.lower() == "si":
        while True:
            apellido_nuevo= input("INGRESE APELLIDO : ")
            if not apellido_nuevo.isalpha():
                print("Debe ingresar un apellido válido.")
                continue
            else:
                listanuevos.append(apellido_nuevo)
                break
    else:
        listanuevos.append(datos[3])

    opm = input("DESEA MODIFICAR LA DIRECCION : {} - [SI/NO] ".format(datos[4]))
    if opm.lower() == "si":
        while True: 
            direc_nuevo = input("INGRESE DIRECCION : ")
            if "#" in direc_nuevo:
                listanuevos.append(direc_nuevo)
                break
            else:
                print('Debe ingresar la dirección con el formato "Nombre Calle, #Número"')
                continue                
    else:
        listanuevos.append(datos[4])

    opm = input("DESEA MODIFICAR EL TELEFONO : {} - [SI/NO] ".format(datos[5]))
    if opm.lower() == "si":
        while True: 
            try:
                fono_nuevo= int(input("INGRESE TELEFONO : "))
            except ValueError:
                print("Debe ingresar dígitos.")
                continue
            fono_nuevo_str = str(fono_nuevo)
            if len(fono_nuevo_str) != 11:
                    print("El télefono ingresado debe tener 11 dígitos.")
                    continue
            else:
                listanuevos.append(fono_nuevo)
    else:
        listanuevos.append(datos[5])

    opm = input("DESEA MODIFICAR EL CORREO : {} - [SI/NO] ".format(datos[6]))
    if opm.lower() == "si":
        while True: 
            correo_nuevo = input("INGRESE EL CORREO : ")
            if not correo_nuevo.endswith("@gmail.com"):
                print('Debe ingresar un correo válido, usando el formato "@gmail.com"')
                continue
            else:
                listanuevos.append(correo_nuevo)
                break
    else:
        listanuevos.append(datos[6])

    opm = input("DESEA MODIFICAR EL CARGO : {} - [SI/NO] ".format(datos[7]))
    if opm.lower() == "si":
        cargo_nuevo=input("INGRESE CARGO : ")
        listanuevos.append(cargo_nuevo)
    else:
        listanuevos.append(datos[7])

    opm = input("DESEA MODIFICAR EL MONTO DE SALARIO : {} - [SI/NO] ".format(datos[8]))
    if opm.lower() == "si":
            while True: 
                salario_nuevo= input("INGRESE MONTO DE SALARIO : ")
                try:
                    salario_nuevo_int = int(salario_nuevo)
                except ValueError:
                    print("Debe ingresar un valor válido.")
                    continue
                break        
            listanuevos.append(salario_nuevo_int)
    else:
        listanuevos.append(datos[8])


    opm = input("DESEA MODIFICAR EL DEPARTAMENTO : {} - [SI/NO] ".format(datos[9]))
    if opm.lower() == "si":
        print("====================================")
        print(" MUESTRA DE TODOS LOS DEPARTAMENTOS ")
        print("====================================")
        datos = DAO.CRUDDepartamento.mostrartodos()
        if len(datos) == 0:
            print("No hay departamentos en la base de datos ")
            time.sleep(1)
            print("Volviendo...")
            time.sleep(2)
            return
        else:
            for dato in datos:
                print(
                    " ID : {} - NOMBRE : {} - UBICACION: {} - GERENTE : {} ".format(dato[0], dato[1], dato[2], dato[3]))
                print("--------------------------------------------------------------------------------------------------------------------------------------------------------")
        time.sleep(2)
        while True:
            try:
                opcion = int(input("INGRESE ID DE DEPARTAMENTO AL QUE DESEA REEMPLAZAR : "))
                datos = DAO.CRUDDepartamento.consultaparticular(opcion)
                if datos is None:
                    print(" No hay departamentos con ese id ")
                    continue
                else:
                    depto = datos[0]
                    listanuevos.append(depto)
                    break
            except ValueError:
                print("Ingrese un numero.")
                time.sleep(2)
                continue
    else:
        listanuevos.append(datos[9])

    DAO.CRUDEmpleado.editar(listanuevos)
# Eliminar datos
def eliminardatos_empleados():
    os.system('cls')
    print("=========================================")
    print("       MODULO ELIMINAR EMPLEADOS         ")
    print("=========================================")
    datos = DAO.CRUDEmpleado.mostrartodos()
    if len(datos) == 0:
        print("No hay Empleados en la base de datos ")
        time.sleep(2)
        os.system("pause")
        return
    mostrartodo_empleados()
    while True:
            try:
                elim = int(input("Ingrese valor de ID del Empleado que desea Eliminar : "))
            except ValueError:
                print("Ingrese un numero.")
                time.sleep(2)
                continue
            ct_depto_r = DAO.CRUDEmpleado.cantidad_registros(elim)
            if ct_depto_r == 0:
                break
            else:
                for dato in datos:
                    print(
                    " ID : {} - FECHA : {} - CANTIDAD DE HORAS TRABAJADAS : {} - DESCRIPCION : {} - ID EMPLEADO VINCULADO : {}".format(dato[0], dato[1], dato[2], dato[3], dato[4]))
                    print("--------------------------------------------------------------------------------------------------------------------------------------------------------")
                opm = input("SI ELIMINA ESTE EMPLEADO TAMBIEN ELIMINARA {} REGISTROS DE TIEMPO VINCULADOS A ESTE MISMO, ESTA SEGURO? : [SI/NO] ".format(ct_depto_r))
                if opm.lower() == "si":
                    time.sleep(1)
                    break
                else:
                    return
    eliminar_varios_r(elim)
    DAO.CRUDEmpleado.eliminar(elim)  
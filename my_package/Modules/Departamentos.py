import DAO.CRUDDepartamento
from DTO.Departamento import Departamento
from my_package.DTO.GestionDepartamentos import GestionDepartamentos

import time, os

# ----DEPARTAMENTOS----
def menudepartamentos():
    while True:
        os.system('cls')
        print("======================================")
        print("   M E N Ú  D E P A R T A M E N T O S ")
        print("======================================")
        print("       1.- INGRESAR                   ")
        print("       2.- MOSTRAR                    ")
        print("       3.- MODIFICAR                  ")
        print("       4.- ELIMINAR                   ")
        print("       5.- VOLVER                     ")
        print("======================================")
        try:
            op = int(input(" INGRESE OPCION : "))
        except ValueError:
            print("Debe ingresar un número.")
            time.sleep(1)
            os.system("cls")
            continue
        if op == 1:
            ingresar_departamento()
        elif op == 2:
            menumostrar_departamentos()
        elif op == 3:
            modificardatos_departamento()
        elif op == 4:
            eliminardatos_departamento()
        elif op == 5:
            break
        else:
            print("Opción Fuera de Rango")
            time.sleep(2)
# Ingresar
def ingresar_departamento():
    os.system('cls')
    print("===============================")
    print("     INGRESAR DEPARTAMENTO     ")
    print("===============================")
    nombre = input("INGRESE NOMBRE DEL DEPARTAMENTO : ")

    ubicacion = input("INGRESE UBICACION DEPARTAMENTO : ") # Podrian agregarse validaciones

    gerente=input("INGRESE NOMBRE GERENTE : ")

    depto = Departamento(nombre, ubicacion, gerente)
    GestionDepartamentos.agregar(depto)
# Mostrar
def menumostrar_departamentos():
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
            mostrartodo_departamento()
        elif op == 2:
            mostraruno_departamento()
        elif op == 3:
            print("no implementado")
        elif op == 4:
            break
        else:
            print("Opción Fuera de Rango")
            time.sleep(2)

def mostrartodo_departamento():
    os.system('cls')
    print("====================================")
    print(" MUESTRA DE TODOS LOS DEPARTAMENTOS ")
    print("====================================")
    datos = DAO.CRUDDepartamento.mostrartodos()
    if len(datos) == 0:
        print("No hay departamentos en la base de datos ")
    else:
        for dato in datos:
            print(
                " ID : {} - NOMBRE : {} - UBICACION: {} - GERENTE : {} ".format(dato[0], dato[1], dato[2], dato[3]))
            print("--------------------------------------------------------------------------------------------------------------------------------------------------------")
    time.sleep(2)
    os.system("pause")

def mostraruno_departamento():
    while True:
        os.system('cls')
        print("===============================")
        print("  MUESTRA DE DATOS PARTICULAR  ")
        print("===============================")
        # try:
        #     op = int(input("Ingrese valor del ID del departamento que desea Mostrar los Datos : "))
        # except ValueError:
        #     print("Ingrese un numero.")
        #     time.sleep(2)
        #     continue
        
        # datos = DAO.CRUDDepartamento.consultaparticular(op)

        GestionDepartamentos.mostrar_uno_test()

       
        if datos is None:
            print(" No hay departamentos con ese id ")
        else:
            print("\n=========================================")
            print("     MUESTRA DE DATOS DEL DEPARTAMENTO     ")
            print("===========================================")
            print(" ID               : {}".format(datos[0]))
            print(" NOMBRE           : {}".format(datos[1]))
            print(" UBICACION        : {}".format(datos[2]))
            print(" GERENTE          : {}".format(datos[3]))
            print("=======================================")
        input("\n\n PRESIONE ENTER PARA CONTINUAR")
        break
# Modificar datos
def modificardatos_departamento():
    os.system('cls')
    listanuevos = []
    print("===========================================")
    print("       MODULO MODIFICAR DEPARTAMENTO       ")
    print("===========================================")
    datos = DAO.CRUDDepartamento.mostrartodos()
    if len(datos) == 0:
        print("No hay departamentos en la base de datos ")
        time.sleep(2)
        return
    mostrartodo_departamento()
    mod = int(input("Ingrese valor de ID del Departamento que desea Modificar: "))
    datos = DAO.CRUDDepartamento.consultaparticular(mod)

    print("\n ID         : {}".format(datos[0]))
    listanuevos.append(datos[0])

    opm = input("DESEA MODIFICAR EL NOMBRE : {} - [SI/NO] ".format(datos[1]))
    if opm.lower() == "si":
            nombrenuevo=input("INGRESE NOMBRE : ")
            listanuevos.append(nombrenuevo)
    else:
        listanuevos.append(datos[1])

    opm = input("DESEA MODIFICAR LA UBICACION : {} - [SI/NO] ".format(datos[2]))
    if opm.lower() == "si":
            ubicacionnueva= input("INGRESE UBICACION : ")
            listanuevos.append(ubicacionnueva)
    else:
        listanuevos.append(datos[2])

    opm = input("DESEA MODIFICAR EL GERENTE : {} - [SI/NO] ".format(datos[3]))
    if opm.lower()== "si":
            gerentenuevo = input("INGRESE DIRECCION : ")
            listanuevos.append(gerentenuevo)
    else:
        listanuevos.append(datos[4])

    DAO.CRUDDepartamento.editar(listanuevos)
# Eliminar datos
def eliminardatos_departamento():
    os.system('cls')
    print("=============================================")
    print("        MODULO ELIMINAR DEPARTAMENTOS        ")
    print("=============================================")
    datos = DAO.CRUDDepartamento.mostrartodos()
    dato_em = DAO.CRUDEmpleado.mostrartodos()
    dato_pr = DAO.CRUDProyecto.mostrartodos()
    if len(datos) == 0:
        print("No hay Departamentos en la base de datos ")
        time.sleep(2)
        os.system("pause")
        return
    mostrartodo_departamento()
    while True:
            try:
                elim = int(input("Ingrese valor de ID del Departamento de tiempo que desea Eliminar : "))
            except ValueError:
                print("Ingrese un numero.")
                time.sleep(2)
                continue
            ct_depto_e = DAO.CRUDDepartamento.cantidad_empleados(elim)
            if ct_depto_e == 0:
                break
            else:
                for dato in dato_em:
                    print(
                        " ID : {} - RUN : {} - NOMBRE : {} - APELLIDO : {} - DIRECCION : {} - FONO : {} - CORREO : {} - CARGO : {} - SALARIO : {} - ID DEPARTAMENTO VINCULADO : {} ".format(dato[0], dato[1], dato[2], dato[3], dato[4], dato[5], dato[6], dato[7], dato[8], dato[9]))
                    print("--------------------------------------------------------------------------------------------------------------------------------------------------------")
                opm = input("SI ELIMINA ESTE DEPARTAMENTO TAMBIEN ELIMINARA {} EMPLEADOS VINCULADOS A ESTE MISMO, ESTA SEGURO? : [SI/NO] ".format(ct_depto_e))
                if opm.lower() == "si":
                    time.sleep(1)
                    break
                else:
                    return
    while True:
        ct_depto_p = DAO.CRUDDepartamento.cantidad_proyectos(elim)
        if ct_depto_p == 0:
            break
        else:
            for dato in dato_pr:
                print(
                    " ID : {} - NOMBRE : {} -  FECHA INICIO : {} - DESCRIPCION : {} -  ID DEPARTAMENTO VINCULADO : {}".format(dato[0], dato[1], dato[3], dato[2], dato[4]))
                print("-----------------------------------------------------------------------------------------------------------------------------------------------------------")
            opm = input("SI ELIMINA ESTE DEPARTAMENTO TAMBIEN ELIMINARA {} PROYECTOS VINCULADOS A ESTE MISMO, ESTA SEGURO? : [SI/NO] ".format(ct_depto_p))
            if opm.lower() == "si":
                eliminar_varios(elim)
                eliminar_varios_p(elim)
                time.sleep(1)
                break
            else:
                return
    DAO.CRUDDepartamento.eliminar(elim)

    os.system('cls')
    print("=============================================")
    print("        MODULO ELIMINAR DEPARTAMENTOS        ")
    print("=============================================")
    datos = DAO.CRUDDepartamento.mostrartodos()
    if len(datos) == 0:
        print("No hay Departamentos en la base de datos ")
        time.sleep(2)
        os.system("pause")
        return
    mostrartodo_departamento()
    while True:
            try:
                elim = int(input("Ingrese valor de ID del Departamento de tiempo que desea Eliminar : "))
            except ValueError:
                print("Ingrese un numero.")
                time.sleep(2)
            DAO.CRUDDepartamento.eliminar(elim)
            break
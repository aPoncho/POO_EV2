import os
import time
from datetime import date
import DAO.CRUDEmpleado
import DAO.CRUDProyecto
import DAO.CRUDDepartamento
import DAO.CRUDRegistro
from DTO.Empleado import Empleado
from DTO.Proyecto import Proyecto
from DTO.Departamento import Departamento
from DTO.Registro import Registro


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


# ----PROYECTOS----
def menuproyectos():
    while True:
        os.system('cls')
        print("===============================")
        print("   M E N Ú  P R O Y E C T O S  ")
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
            ingresar_proyecto()
        elif op == 2:
            menumostrar_proyectos()
        elif op == 3:
            modificardatos_proyectos()
        elif op == 4:
            eliminardatos_proyectos()
        elif op == 5:
            break
        else:
            print("Opción Fuera de Rango")
            time.sleep(2)
# Ingresar
def ingresar_proyecto():
    os.system('cls')
    print("===============================")
    print("       INGRESAR PROYECTO       ")
    print("===============================")
    while True:
        nombre=input("INGRESE NOMBRE PROYECTO: ")
        if not nombre.isalpha():
            print("Debe ingresar un nombre válido.")
            time.sleep(1)
            continue
        else:
            break
    
    while True:
        descripcion = input("INGRESE DESCRIPCION PROYECTO : ")
        if len(descripcion) > 500:
            print("Descripcion muy larga (Max 500 caracteres)")
            time.sleep(1)
            continue
        break
    print("--- FECHA PROYECTO ---")
    while True:
        try:
            dia=input("INGRESE DIA : ")
            dia_int = int(dia)
            if dia_int > 31 or dia == "00" or dia.isdigit() == False:
                print("Ingrese el dia en 2 digitos")
                continue
            elif len(dia) == 2:
                break
            else:
                print("Ingrese el dia en 2 digitos")
                continue
        except ValueError:
            print("Debe ingresar dígitos.")
    while True:
        try:
            mes=input("INGRESE MES : ")
            mes_int = int(mes)
            if mes_int > 12 or mes == "00" or mes.isdigit() == False:
                print("Ingrese el mes en 2 digitos")
                continue
            elif len(mes) == 2:
                break
            else:
                print("Ingrese el mes en 2 digitos")
                continue
        except ValueError:
            print("Debe ingresar dígitos.")
    while True:
        try:
            año=input("INGRESE AÑO : ")
            año_int = int(año)
            if año_int < 2023 or año == "0000" or año.isdigit() == False:
                print("Ingrese el año en 4 digitos")
                continue
            elif len(año) == 4:
                break
            else:
                print("Ingrese el año en 4 digitos")
                continue
        except ValueError:
            print("Debe ingresar dígitos.")

    fecha_inicio = date(año_int, mes_int, dia_int)

    p = Proyecto(nombre, descripcion, fecha_inicio)
    DAO.CRUDProyecto.agregar(p)
# Mostrar
def menumostrar_proyectos():
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
            mostrartodo_proyectos()
        elif op == 2:
            mostraruno_proyectos()
        elif op == 3:
            mostrarparcial_empleados()
        elif op == 4:
            break
        else:
            print("Opción Fuera de Rango")
            time.sleep(2)

def mostrartodo_proyectos():
    os.system('cls')
    print("================================")
    print(" MUESTRA DE TODOS LOS PROYECTOS ")
    print("================================")
    datos = DAO.CRUDProyecto.mostrartodos()
    if len(datos) == 0:
        print("No hay proyectos en la base de datos ")
    else:
        for dato in datos:
            print(
                " ID : {} - NOMBRE : {} -  FECHA INICIO : {} - DESCRIPCION : {}".format(dato[0], dato[1], dato[3], dato[2]))
            print("-----------------------------------------------------------------------------------------------------------------------------------------------------------")
    time.sleep(2)
    os.system("pause")
    
def mostraruno_proyectos():
    while True:
        os.system('cls')
        print("===============================")
        print("  MUESTRA DE DATOS PARTICULAR  ")
        print("===============================")
        try:
            op = int(input("Ingrese valor del ID del registro de tiempo que desea Mostrar los Datos : "))
        except ValueError:
            print("Ingrese un numero.")
            time.sleep(2)
            continue
        break
    datos = DAO.CRUDProyecto.consultaparticular(op)
    if datos is None:
        print(" No hay proyectos con ese id ")
    else:
        print("\n=====================================")
        print("     MUESTRA DE DATOS DEL PROYECTO     ")
        print("=======================================")
        print(" ID               : {}".format(datos[0]))
        print(" NOMBRE           : {}".format(datos[1]))
        print(" FECHA INICIO     : {}".format(datos[3]))
        print(" DESCRIPCION      : {}".format(datos[2]))
        print("=======================================")
    input("\n\n PRESIONE ENTER PARA CONTINUAR")
# Modificar datos
def modificardatos_proyectos():
    os.system('cls')
    listanuevos = []
    print("===========================================")
    print("        MODULO MODIFICAR PROYECTOS         ")
    print("===========================================")
    datos = DAO.CRUDProyecto.mostrartodos()
    if len(datos) == 0:
        print("No hay proyectos en la base de datos ")
        time.sleep(2)
        return
    mostrartodo_proyectos()
    mod = int(input("Ingrese valor de ID del Registro de tiempo que desea Modificar: "))
    datos = DAO.CRUDProyecto.consultaparticular(mod)

    print("\n ID         : {}".format(datos[0]))
    listanuevos.append(datos[0])

    opm = input("DESEA MODIFICAR EL NOMBRE : {} - [SI/NO] ".format(datos[1]))
    if opm.lower() == "si":
            nombrenuevo= input("INGRESE NOMBRE : ")
            listanuevos.append(nombrenuevo)
    else:
        listanuevos.append(datos[1])

    opm = input("DESEA MODIFICAR LA DESCRIPCION : {} - [SI/NO] ".format(datos[2]))
    if opm.lower()== "si":
            descnueva = input("INGRESE DIRECCION : ")
            listanuevos.append(descnueva)
    else:
        listanuevos.append(datos[2])
    
    opm = input("DESEA MODIFICAR LA FECHA : {} - [SI/NO] ".format(datos[3]))
    if opm.lower() == "si":
        while True:
            try:
                dia=input("INGRESE DIA : ")
                dia_int = int(dia)
                if dia_int > 31 or dia == "00" or dia.isdigit() == False:
                    print("Ingrese el dia en 2 digitos")
                    continue
                elif len(dia) == 2:
                    break
                else:
                    print("Ingrese el dia en 2 digitos")
                    continue
            except ValueError:
                print("Debe ingresar dígitos.")
        while True:
            try:
                mes=input("INGRESE MES : ")
                mes_int = int(mes)
                if mes_int > 12 or mes == "00" or mes.isdigit() == False:
                    print("Ingrese el mes en 2 digitos")
                    continue
                elif len(mes) == 2:
                    break
                else:
                    print("Ingrese el mes en 2 digitos")
                    continue
            except ValueError:
                print("Debe ingresar dígitos.")
        while True:
            try:
                año=input("INGRESE AÑO : ")
                año_int = int(año)
                if año_int < 2023 or año == "0000" or año.isdigit() == False:
                    print("Ingrese el año en 4 digitos")
                    continue
                elif len(año) == 4:
                    break
                else:
                    print("Ingrese el año en 4 digitos")
                    continue
            except ValueError:
                print("Debe ingresar dígitos.")
            
        fechanueva = date(año_int, mes_int, dia_int)
        listanuevos.append(fechanueva)
    else: 
        listanuevos.append(datos[3])

    DAO.CRUDProyecto.editar(listanuevos)
# Eliminar datos
def eliminardatos_proyectos():
    os.system('cls')
    print("=========================================")
    print("       MODULO ELIMINAR PROYECTOS         ")
    print("=========================================")
    datos = DAO.CRUDProyecto.mostrartodos()
    if len(datos) == 0:
        print("No hay proyectos en la base de datos ")
        time.sleep(2)
        os.system("pause")
        return
    mostrartodo_proyectos()
    while True:
            try:
                elim = int(input("Ingrese valor de ID del Proyecto que desea Eliminar : "))
            except ValueError:
                print("Ingrese un numero.")
                time.sleep(2)
            DAO.CRUDProyecto.eliminar(elim)
            break


# ----REGISTROS----
def menuregistros():
    while True:
        os.system('cls')
        print("======================================")
        print("       M E N Ú  R E G I S T R O S     ")
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
            ingresar_registros()
        elif op == 2:
            menumostrar_registros()
        elif op == 3:
            modificardatos_registros()
        elif op == 4:
            eliminardatos_registros()
        elif op == 5:
            break
        else:
            print("Opción Fuera de Rango")
            time.sleep(2)
# Ingresar
def ingresar_registros():
    os.system('cls')
    print("===============================")
    print("       INGRESAR REGISTRO       ")
    print("===============================")
    print()
    print("--- FECHA REGISTRO ---")
    while True:
        try:
            dia=input("INGRESE DIA : ")
            dia_int = int(dia)
            if dia_int > 31 or dia == "00" or dia.isdigit() == False:
                print("Ingrese el dia en 2 digitos")
                continue
            elif len(dia) == 2:
                break
            else:
                print("Ingrese el dia en 2 digitos")
                continue
        except ValueError:
            print("Debe ingresar dígitos.")
    while True:
        try:
            mes=input("INGRESE MES : ")
            mes_int = int(mes)
            if mes_int > 12 or mes == "00" or mes.isdigit() == False:
                print("Ingrese el mes en 2 digitos")
                continue
            elif len(mes) == 2:
                break
            else:
                print("Ingrese el mes en 2 digitos")
                continue
        except ValueError:
            print("Debe ingresar dígitos.")
    while True:
        try:
            año=input("INGRESE AÑO : ")
            año_int = int(año)
            if año_int < 2023 or año == "0000" or año.isdigit() == False:
                print("Ingrese el año en 4 digitos")
                continue
            elif len(año) == 4:
                break
            else:
                print("Ingrese el año en 4 digitos")
                continue
        except ValueError:
            print("Debe ingresar dígitos.")
        
    fecha = date(año_int, mes_int, dia_int)

    while True:
        try:
            horas=input("INGRESE HORAS TRABAJADAS : ")
            horas_int = int(horas)
            if horas_int > 9 or horas == "00" or horas.isdigit() == False:
                print("Numero de horas ingresados no es valido")
                continue
            elif len(horas) == 1:
                break
            else:
                print("Ingrese las horas en 1 digito")
                continue
        except ValueError:
            print("Debe ingresar dígitos.")
    while True:
        descripcion = input("INGRESE DESCRIPCION PROYECTO : ")
        if len(descripcion) > 300:
            print("Descripcion muy larga (Max 300 caracteres)")
            time.sleep(1)
            continue
        else:
            break

    r = Registro(fecha, horas_int, descripcion)
    DAO.CRUDRegistro.agregar(r)
# Mostrar
def menumostrar_registros():
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
            mostrartodo_registros()
        elif op == 2:
            mostraruno_registros()
        elif op == 3:
            mostrarparcial_empleados()
        elif op == 4:
            op2 = input("DESEA VOLVER? [SI/NO] :")
            if op2.lower() == "si":
                break
            elif op2.lower() == "no":
                print("Volviendo al menu..")
                time.sleep(1)
                os.system("cls")
                continue
            else:
                print("Opción no válida.")
                time.sleep(1)
                continue
        else:
            print("Opción Fuera de Rango")
            time.sleep(2)

def mostrartodo_registros():
    os.system('cls')
    print("================================")
    print(" MUESTRA DE TODOS LOS REGISTROS ")
    print("================================")
    datos = DAO.CRUDRegistro.mostrartodos()
    if len(datos) == 0:
        print("No hay registros de tiempo en la base de datos ")
    else:
        for dato in datos:
            print(
                " ID : {} - FECHA : {} - CANTIDAD DE HORAS TRABAJADAS : {} - DESCRIPCION : {} ".format(dato[0], dato[1], dato[2], dato[3]))
            print("--------------------------------------------------------------------------------------------------------------------------------------------------------")
    time.sleep(2)
    os.system("pause")

def mostraruno_registros():
    while True:
        os.system('cls')
        print("===============================")
        print("  MUESTRA DE DATOS PARTICULAR  ")
        print("===============================")
        try:
            op = int(input("Ingrese valor del ID del registro de tiempo que desea Mostrar los Datos : "))
        except ValueError:
            print("Ingrese un numero.")
            time.sleep(2)
            continue
        break
    datos = DAO.CRUDRegistro.consultaparticular(op)
    if datos is None:
        print(" No hay registros de tiempo con ese id ")
    else:
        print("\n===============================================")
        print("     MUESTRA DE DATOS DEL REGISTRO DE TIEMPO     ")
        print("=================================================")
        print(" ID                         : {}".format(datos[0]))
        print(" FECHA                      : {}".format(datos[1]))
        print(" CANT. DE HORAS TRABAJADAS  : {}".format(datos[2]))
        print(" DESCRIPCION                : {}".format(datos[3]))
        print("=================================================")
    input("\n\n PRESIONE ENTER PARA CONTINUAR")
# Modificar datos
def modificardatos_registros():
    os.system('cls')
    listanuevos = []
    print("===========================================")
    print("        MODULO MODIFICAR REGISTROS         ")
    print("===========================================")
    datos = DAO.CRUDRegistro.mostrartodos()
    if len(datos) == 0:
        print("No hay registros de tiempo en la base de datos ")
        time.sleep(2)
        return
    mostrartodo_registros()
    
    mod = int(input("Ingrese valor de ID del Registro de tiempo que desea Modificar: "))
    datos = DAO.CRUDRegistro.consultaparticular(mod)

    print("\n ID         : {}".format(datos[0]))
    listanuevos.append(datos[0])

    opm = input("DESEA MODIFICAR LA FECHA : {} - [SI/NO] ".format(datos[1]))
    if opm.lower() == "si":
        while True:
            try:
                dia=input("INGRESE DIA : ")
                dia_int = int(dia)
                if dia_int > 31 or dia == "00" or dia.isdigit() == False:
                    print("Ingrese el dia en 2 digitos")
                    continue
                elif len(dia) == 2:
                    break
                else:
                    print("Ingrese el dia en 2 digitos")
                    continue
            except ValueError:
                print("Debe ingresar dígitos.")
        while True:
            try:
                mes=input("INGRESE MES : ")
                mes_int = int(mes)
                if mes_int > 12 or mes == "00" or mes.isdigit() == False:
                    print("Ingrese el mes en 2 digitos")
                    continue
                elif len(mes) == 2:
                    break
                else:
                    print("Ingrese el mes en 2 digitos")
                    continue
            except ValueError:
                print("Debe ingresar dígitos.")
        while True:
            try:
                año=input("INGRESE AÑO : ")
                año_int = int(año)
                if año_int < 2023 or año == "0000" or año.isdigit() == False:
                    print("Ingrese el año en 4 digitos")
                    continue
                elif len(año) == 4:
                    break
                else:
                    print("Ingrese el año en 4 digitos")
                    continue
            except ValueError:
                print("Debe ingresar dígitos.")
            
        fechanueva = date(año_int, mes_int, dia_int)
        listanuevos.append(fechanueva)
    else: 
        listanuevos.append(datos[1])

    opm = input("DESEA MODIFICAR LA CANTIDAD DE HORAS : {} - [SI/NO] ".format(datos[2]))
    if opm.lower() == "si":
            horasnueva= int(input("INGRESE CANTIDAD DE HORAS : "))
            listanuevos.append(horasnueva)
    else:
        listanuevos.append(datos[2])

    opm = input("DESEA MODIFICAR LA DESCRIPCION : {} - [SI/NO] ".format(datos[3]))
    if opm.lower()== "si":
            descnueva = input("INGRESE DIRECCION : ")
            listanuevos.append(descnueva)
    else:
        listanuevos.append(datos[3])

    DAO.CRUDRegistro.editar(listanuevos)
# Eliminar datos
def eliminardatos_registros():
    os.system('cls')
    print("=========================================")
    print("       MODULO ELIMINAR REGISTROS         ")
    print("=========================================")
    datos = DAO.CRUDRegistro.mostrartodos()
    if len(datos) == 0:
        print("No hay Registros de tiempo en la base de datos ")
        time.sleep(2)
        os.system("pause")
        return
    mostrartodo_registros()
    while True:
            try:
                elim = int(input("Ingrese valor de ID del Registro de tiempo que desea Eliminar : "))
            except ValueError:
                print("Ingrese un numero.")
                time.sleep(2)
            DAO.CRUDRegistro.eliminar(elim)
            break


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

    d = Departamento(nombre, ubicacion, gerente)
    DAO.CRUDDepartamento.agregar(d)
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
            mostrarparcial_empleados()
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
        try:
            op = int(input("Ingrese valor del ID del departamento que desea Mostrar los Datos : "))
        except ValueError:
            print("Ingrese un numero.")
            time.sleep(2)
            continue
        break
    datos = DAO.CRUDDepartamento.consultaparticular(op)
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


# ---- EMPLEADO ----
def menuempleados():
    while (True):
        #os.system('cls')
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
    
    while True:
        depto=input("INGRESE DEPARTAMENTO : ")
        if not nombre.isalpha():
            print("Debe ingresar un departamento válido.")
            time.sleep(1)
            continue
        else:
            break

    e = Empleado(run, nombre, apellido, direccion, fono, correo, cargo, salario, depto)
    DAO.CRUDEmpleado.agregar(e)

def mostrartodo_empleados():
    os.system('cls')
    print("================================")
    print(" MUESTRA DE TODOS LOS EMPLEADOS ")
    print("================================")
    datos = DAO.CRUDEmpleado.mostrartodos()
    if len(datos) == 0:
        print("No hay empleados en la base de datos ")
    else:
        for dato in datos:
            print(
                " ID : {} - RUN : {} - NOMBRE : {} - APELLIDO : {} - DIRECCION : {} - FONO : {} - CORREO : {} - CARGO : {} - SALARIO : {} - DEPARTAMENTO : {} ".format(dato[0], dato[1], dato[2], dato[3], dato[4], dato[5], dato[6], dato[7], dato[8], dato[9]))
            print("--------------------------------------------------------------------------------------------------------------------------------------------------------")
    time.sleep(2)
    os.system("pause")

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
    datos = DAO.CRUDEmpleado.consultaparticular(op)
    if datos is None:
        print(" No hay proyectos con ese id ")
    else:
        print("\n=====================================")
        print("     MUESTRA DE DATOS DEL EMPLEADO     ")
        print("=======================================")
        print(" ID               : {}".format(datos[0]))
        print(" RUN              : {}".format(datos[1]))
        print(" NOMBRE           : {}".format(datos[2]))
        print(" APELLIDO         : {}".format(datos[3]))
        print(" DIRECCION        : {}".format(datos[4]))
        print(" FONO             : {}".format(datos[5]))
        print(" CORREO           : {}".format(datos[6]))
        print(" CARGO            : {}".format(datos[7]))
        print(" SALARIO          : {}".format(datos[8]))
        print(" DEPARTAMENTO     : {}".format(datos[9]))
        print("=======================================")
    input("\n\n PRESIONE ENTER PARA CONTINUAR")

def mostrarparcial_empleados():
    os.system('cls')
    print("=======================================")
    print("   MUESTRA PARCIALMENTE LOS CLIENTES   ")
    print("=======================================")
    cant = int(input("\nIngrese la Cantidad de Clientes a Mostrar : "))
    datos = DAO.CRUDEmpleado.consultaparcial(cant)
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
    datos = DAO.CRUDREmpleado.mostrartodos()
    if len(datos) == 0:
        print("No hay empleados en la base de datos ")
        time.sleep(2)
        return
    mostrartodo_empleados()
    mod = int(input("Ingrese valor de ID del Empleado que desea Modificar: "))
    datos = DAO.CRUDEmpleado.consultaparticular(mod)

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
            DAO.CRUDEmpleado.eliminar(elim)
            break
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
        menuempleados()
    elif op == 2:
        menuproyectos()
    elif op == 3:
        menuregistros()
    elif op == 4:
        menudepartamentos()
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

import time, os
from datetime import date
from  DTO.Registro import Registro
import DAO.CRUDRegistro

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
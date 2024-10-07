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
        #os.system('cls')
        print("===============================")
        print("   M E N Ú  P R O Y E C T O S  ")
        print("===============================")
        print("       1.- INGRESAR            ")
        print("       2.- --                  ")
        print("       3.- --                  ")
        print("       4.- --                  ")
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
            mostrar()
        elif op == 3:
            modificardatos()
        elif op == 4:
            eliminardatos()
        elif op == 5:
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
# ----REGISTROS----
def menuregistros():
    while True:
        #os.system('cls')
        print("======================================")
        print("       M E N Ú  R E G I S T R O S     ")
        print("======================================")
        print("       1.- INGRESAR                   ")
        print("       2.- --                         ")
        print("       3.- --                         ")
        print("       4.- --                         ")
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
            mostrar()
        elif op == 3:
            modificardatos()
        elif op == 4:
            eliminardatos()
        elif op == 5:
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

def ingresar_registros():
    #os.system('cls')
    print("===============================")
    print("       INGRESAR PROYECTO       ")
    print("===============================")
    print()
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
# ----DEPARTAMENTOS----
def menudepartamentos():
    while True:
        os.system('cls')
        print("======================================")
        print("   M E N Ú  D E P A R T A M E N T O S ")
        print("======================================")
        print("       1.- INGRESAR                  ")
        print("       2.- --                  ")
        print("       3.- --                  ")
        print("       4.- --              ")
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
            mostrar()
        elif op == 3:
            modificardatos()
        elif op == 4:
            eliminardatos()
        elif op == 5:
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

def ingresar_departamento():
    os.system('cls')
    print("===============================")
    print("     INGRESAR DEPARTAMENTO     ")
    print("===============================")
    nombre = input("INGRESE NOMBRE DEL DEPARTAMENTO : ")

    ubicacion = input("INGRESE UBICACION DEPARTAMENTO : ") # Podrian agregarse validaciones

    while True:
        gerente=input("INGRESE NOMBRE GERENTE : ")
        if not nombre.isalpha():
            print("Debe ingresar un nombre válido.")
            time.sleep(1)
            continue
        else:
            break

    d = Departamento(nombre, ubicacion, gerente)
    DAO.CRUDDepartamento.agregar(d)

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
            mostrar_empleados()
        elif op == 3:
            modificardatos_empleados()
        elif op == 4:
            eliminardatos_empleados()
        elif op == 5:
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

def menumostrar_empleados():
    os.system('cls')
    print("===============================")
    print("    M E N Ú  M O S T R A R     ")
    print("===============================")
    print("       1.- MOSTRAR TODO        ")
    print("       2.- MOSTRAR UNO         ")
    print("       3.- MOSTRAR PARCIAL     ")
    print("       4.- VOLVER              ")
    print("===============================")

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

def mostrar_empleados():
    while (True):
        menumostrar()
        try:
            op2 = int(input(" INGRESE OPCION : "))
        except ValueError:
            print("Debe ingresar un número.")
            time.sleep(1)
            os.system("cls")
            continue
        if op2 == 1:
            mostrartodo_empleados()
            input("\n\n PRESIONE ENTER PARA CONTINUAR")
        elif op2 == 2:
            mostraruno_empleados()
        elif op2 == 3:
            mostrarparcial_empleados()
        elif op2 == 4:
            break
        else:
            print("Opción Fuera de Rango")
            time.sleep(2)
            os.system("pause")
            os.system("cls")

def mostrartodo_empleados():
    os.system('cls')
    print("===============================")
    print(" MUESTRA DE TODOS LOS CLIENTES ")
    print("===============================")
    datos = DAO.CRUDEmpleado.mostrartodos()
    for dato in datos:
        print(
            " ID : {} - RUN : {} - NOMBRE : {} - APELLIDO : {} - DIRECCION : {} - FONO : {} - CORREO : {} - CARGO : {} - SALARIO : {} - DEPARTAMENTO : {} ".format(dato[0], dato[1], dato[2], dato[3], dato[4], dato[5], dato[6], dato[7], dato[8], dato[9]))
        print("-----------------------------------------------------------------------------------------------------------------------------------------------------------")

def mostraruno_empleados():
    os.system('cls')
    print("===============================")
    print("  MUESTRA DE DATOS PARTICULAR  ")
    print("===============================")
    op = int(input("\n Ingrese valor del ID del Cliente que desea Mostrar los Datos : "))
    datos = DAO.CRUDEmpleado.consultaparticular(op)

    print("\n=====================================")
    print("     MUESTRA DE DATOS DEL CLIENTE      ")
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

def modificardatos_empleados():
    os.system('cls')
    listanuevos = []
    print("=======================================")
    print("       MODULO MODIFICAR CLIENTES       ")
    print("=======================================")
    mostrartodo()
    mod = int(input("\n ingrese valor de ID del cliente que desea Modificar: "))
    datos = DAO.CRUDEmpleado.consultaparticular(mod)

    print("ID         : {}".format(datos[0]))
    listanuevos.append(datos[0])
    print("RUN        : {}".format(datos[1]))
    listanuevos.append(datos[1])

    opm = input("DESEA MODIFICAR EL NOMBRE : {} - [SI/NO]".format(datos[2]))
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

    opm = input("DESEA MODIFICAR LA DIRECCION : {} - [SI/NO]".format(datos[4]))
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

    opm = input("DESEA MODIFICAR EL TELEFONO : {} - [SI/NO]".format(datos[5]))
    if opm.lower() == "si":
        while True: 
            try:
                fononuevo= input("INGRESE TELEFONO : ")
            except ValueError:
                print("Debe ingresar dígitos.")
                continue
            fononuevo_str = str(fononuevo)
            if len(fononuevo_str) != 9:
                    print("El télefono ingresado debe tener 9 dígitos.")
                    continue
            else:
                listanuevos.append(fononuevo)
    else:
        listanuevos.append(datos[5])

    opm = input("DESEA MODIFICAR EL CORREO : {} - [SI/NO]".format(datos[6]))
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

    opm = input("DESEA MODIFICAR LA DEUDA : {} - [SI/NO] ".format(datos[8]))
    if opm.lower() == "si":
        while True: 
            try:
                deudanuevo=int(input("INGRESE DEUDA : "))
            except ValueError:
                print("El dato ingresado debe ser un numero entero")
                continue
            break
        listanuevos.append(deudanuevo)
    else:
        listanuevos.append(datos[8])

    opm = input("DESEA MODIFICAR EL MONTO DE CREDITO : {} - [SI/NO] ".format(datos[7]))
    if opm.lower() == "si":
            while True: 
                montonuevo= input("INGRESE MONTO DE CREDITO : ")
                try:
                    montonuevo_int = int(montonuevo)
                except ValueError:
                    print("Debe ingresar un valor válido.")
                    continue
                break        
            listanuevos.append(montonuevo)
    else:
        listanuevos.append(datos[7])

    opm = input("DESEA MODIFICAR EL TIPO : {} - [SI/NO] ".format(datos[9]))
    if opm.lower() == "si":
        datos = DAO.CRUDEmpleado.mostrartipos()
        print("=======================================")
        for dato in datos:
            print(
                " CODIGO : {} - {}.".format(dato[0], dato[1]))
        print("=======================================")
        tiponuevo = int(input("INGRESE EL TIPO : "))
        listanuevos.append(tiponuevo)
    else:
        listanuevos.append(datos[9])
    DAO.CRUDEmpleado.editar(listanuevos)

def eliminardatos_empleados():
    os.system('cls')
    print("=======================================")
    print("       MODULO ELIMINAR CLIENTE         ")
    print("=======================================")
    mostrartodo()
    elim = int(input("Ingrese valor de ID del Cliente que desea Eliminar : "))
    DAO.CRUDEmpleado.eliminar(elim)

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

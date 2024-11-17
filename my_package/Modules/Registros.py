import time, os
from datetime import date
from my_package.DTO.Registro import Registro
from my_package.DAO.CRUDRegistro import GestionRegistros
from my_package.DAO.CRUDEmpleado import GestionEmpleados
from my_package.DTO.Empleado import Empleado
#fixear para empleado
def eliminar_varios_r(id_depto):
        datos = [DAO.CRUDRegistro.consulta_dpto(id_depto)]
        lista_id = []
        for dato in datos:
            lista_id.append(dato[0])
        for id in lista_id:
            DAO.CRUDRegistro.eliminar(id)
            
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
            print("No implementado")
        elif op == 3:
            print("No implementado")
        elif op == 4:
            print("No implementado")
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
            descripcion = input("INGRESE DESCRIPCION REGISTRO : ")
            if len(descripcion) > 300:
                print("Descripcion muy larga (Max 300 caracteres)")
                time.sleep(1)
                continue
            else:
                break

        datos = GestionEmpleados.obtener_todos()
        empleados = GestionEmpleados(datos)
        print(empleados)
        if datos == None:
            print("Volviendo...")
            time.sleep(2)
            break
        else:        
            while True:
                try:
                    opcion = int(input("INGRESE ID DE EMPLEADO AL QUE DESEA VINCULAR : "))
                    datos = GestionEmpleados.obtener_uno(opcion)
                    if datos is None:
                        print(" No hay empleados con ese id ")
                        continue
                    else:
                        empleado = Empleado(datos[1],datos[2],datos[3],datos[4],datos[5],datos[6],datos[7],datos[8], datos[9], datos[0])
                        id_empleado = empleado.id
                        break
                except ValueError:
                    print("Ingrese un numero.")
                    time.sleep(2)
                    continue

            r = Registro(fecha, horas_int, descripcion, id_empleado)
            GestionRegistros.agregar(r)
            break
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
    datos = GestionRegistros.obtener_todos()
    if len(datos) == 0:
        print("No hay registros de tiempo en la base de datos ")
    else:
        for dato in datos:
            print(
                " ID : {} - FECHA : {} - CANTIDAD DE HORAS TRABAJADAS : {} - DESCRIPCION : {} - ID EMPLEADO VINCULADO : {}".format(dato[0], dato[1], dato[2], dato[3], dato[4]))
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
        print(" ID EMPLEADO VINCULADO      : {}".format(datos[4]))
        print("================================================")
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
    
    opm = input("DESEA MODIFICAR EL EMPLEADO VINCULADO : {} - [SI/NO] ".format(datos[4]))
    if opm.lower() == "si":
        print("====================================")
        print("    MUESTRA DE TODOS LOS EMPLEADOS  ")
        print("====================================")
        datos = DAO.CRUDEmpleado.mostrartodos()
        if len(datos) == 0:
            print("No hay empleados en la base de datos ")
            time.sleep(1)
            print("Volviendo...")
            time.sleep(2)
            return
        else:
            for dato in datos:
                print(
                    " ID : {} - RUN : {} - NOMBRE : {} - APELLIDO : {} - DIRECCION : {} - FONO : {} - CORREO : {} - CARGO : {} - SALARIO : {} - DEPARTAMENTO : {} ".format(dato[0], dato[1], dato[2], dato[3], dato[4], dato[5], dato[6], dato[7], dato[8], dato[9]))
                print("--------------------------------------------------------------------------------------------------------------------------------------------------------")
        time.sleep(2)
        while True:
            try:
                opcion = int(input("INGRESE ID DE EMPLEADO AL QUE DESEA REEMPLAZAR : "))
                datos = DAO.CRUDEmpleado.consultaparticular(opcion)
                if datos is None:
                    print(" No hay empleados con ese id ")
                    continue
                else:
                    id_empleado = datos[0]
                    listanuevos.append(id_empleado)
                    break
            except ValueError:
                print("Ingrese un numero.")
                time.sleep(2)
                continue
    else:
        listanuevos.append(datos[4])

    DAO.CRUDRegistro.editar(listanuevos)
# Eliminar datos
def eliminardatos_registros():
    os.system('cls')
    print("=========================================")
    print("       MODULO ELIMINAR REGISTROS         ")
    print("=========================================")
    datos = GestionRegistros.obtener_todos()
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
                continue
            DAO.CRUDRegistro.eliminar(elim)
            break

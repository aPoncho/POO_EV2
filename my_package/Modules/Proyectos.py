from my_package.DAO.CRUDProyecto import GestionProyectos
import time, os
from datetime import date
from my_package.DTO.Proyecto import Proyecto
from my_package.DAO.CRUDDepartamento import GestionDepartamentos

def eliminar_varios_p(id_depto):
        datos = [DAO.CRUDProyecto.consulta_dpto(id_depto)]
        lista_id = []
        for dato in datos:
            lista_id.append(dato[0])
        for id in lista_id:
            DAO.CRUDProyecto.eliminar(id)
            
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
        
        op = input(" INGRESE OPCION : ")
        if op == '1':
            ingresar_proyecto()
        elif op == '2':
            input("No implementado, PRESIONE CUALQUIER TECLA PARA CONTINUAR")
            #menumostrar_proyectos()
        elif op == '3':
            input("No implementado, PRESIONE CUALQUIER TECLA PARA CONTINUAR")
            #modificardatos_proyectos()
        elif op == '4':
            input("No implementado, PRESIONE CUALQUIER TECLA PARA CONTINUAR")
            #eliminardatos_proyectos()
        elif op == '5':
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
        nombre = input("INGRESE NOMBRE PROYECTO: ")
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

    print("====================================")
    print(" MUESTRA DE TODOS LOS DEPARTAMENTOS ")
    print("====================================")
    datos = GestionDepartamentos.obtener_todos()
    if len(datos) == 0:
        print("No hay departamentos en la base de datos ")
        time.sleep(1)
        print("Volviendo...")
        time.sleep(2)
        return
    else:
        departamentos = GestionDepartamentos(datos)
        print(departamentos)
        #for dato in datos:
            #print(
                #" ID : {} - NOMBRE : {} - UBICACION: {} - GERENTE : {} ".format(dato[0], dato[1], dato[2], dato[3]))
            #print("--------------------------------------------------------------------------------------------------------------------------------------------------------")
    time.sleep(0.5)
    while True:
        try:
            opcion = int(input("INGRESE ID DE DEPARTAMENTO AL QUE DESEA VINCULAR : "))
            datos = GestionDepartamentos.obtener_uno(opcion)
            if datos is None:
                print(" No hay departamentos con ese id ")
                continue
            else:
                id_departamento = datos[0]
                break
        except ValueError:
            print("Ingrese un numero.")
            time.sleep(2)
            continue
        
    p = Proyecto(nombre, descripcion, fecha_inicio, id_departamento)
    GestionProyectos.agregar(p)
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
                " ID : {} - NOMBRE : {} -  FECHA INICIO : {} - DESCRIPCION : {} -  ID DEPARTAMENTO VINCULADO : {}".format(dato[0], dato[1], dato[3], dato[2], dato[4]))
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
        print(" ID DEPTO VINCULADO  : {}".format(datos[4]))
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

    opm = input("DESEA MODIFICAR EL DEPARTAMENTO VINCULADO : {} - [SI/NO] ".format(datos[4]))
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
                    id_departamento = datos[0]
                    listanuevos.append(id_departamento)
                    break
            except ValueError:
                print("Ingrese un numero.")
                time.sleep(2)
                continue
    else: 
        listanuevos.append(datos[4])

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
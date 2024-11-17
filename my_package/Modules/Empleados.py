from my_package.DAO.CRUDEmpleado import GestionEmpleados
from my_package.DTO.Usuario import Usuario
from my_package.DTO.Empleado import Empleado
from my_package.DTO.GestionDepartamentos import GestionDepartamentos
from my_package.DAO.CRUDDepartamento import obtener_todos
from my_package.DTO.GestionRegistros import GestionRegistros
import os, time
from datetime import date

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

#Ingresar Empleado (WORKING)
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
    datos = obtener_todos()
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
            datos = GestionDepartamentos.mostrar_uno(opcion)
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
    user = Usuario(run, nombre, apellido, direccion, fono, correo, 88, 'contraseña123')
    print(e)
    print(user)
    GestionEmpleados.agregar(e)


#Menu 
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

#Mostrar (WORKING)
def mostrartodo_empleados():
    os.system('cls')
    datos = GestionEmpleados.obtener_todos()
    empleados = GestionEmpleados(datos)
    print(empleados)
    os.system("pause")

#Mostrar (WORKING)
def mostraruno_empleados():
    while True:
        os.system('cls')
        try:
            op = int(input("Ingrese valor del ID del empleado que desea Mostrar los Datos : "))
        except ValueError:
            print("Ingrese un numero.")
            time.sleep(2)
            continue
        print("===============================")
        print("  MUESTRA DE DATOS PARTICULAR  ")
        print("===============================")
        datos = GestionEmpleados.obtener_uno(op)
        if datos == None:
            print(" No hay empleados con ese id ")
            print('Volviendo al menu...')           
            break
        else:
            empleado = Empleado(datos[1],datos[2],datos[3],datos[4],datos[5],datos[6],datos[7],datos[8], datos[9], datos[0])
            print(empleado)
            break
    input("\n\n PRESIONE ENTER PARA CONTINUAR")

#Mostrar (WORKING)
def mostrarparcial_empleados():
    os.system('cls')
    print("=======================================")
    print("   MUESTRA PARCIALMENTE LOS CLIENTES   ")
    print("=======================================")
    while True:
        try:
            cantidad = int(input("\nIngrese la Cantidad de Empleados a Mostrar : "))
        except:
            print("ingrese una cantidad valida")
            continue
        if cantidad == 0:
            print("cantidad no valida, volviendo al menu...")
            input("\n\n PRESIONE ENTER PARA CONTINUAR")
            break
        else:
            datos = GestionEmpleados.consulta_parcial(cantidad)
            empleados = GestionEmpleados(datos)
            print(empleados)
            input("\n\n PRESIONE ENTER PARA CONTINUAR")
            break

# Modificar datos (WORKING, falta testeo)
def modificardatos_empleados():
    os.system('cls')
    listanuevos = []
    print("========================================")
    print("       MODULO MODIFICAR EMPLEADOS       ")
    print("========================================")
    datos = GestionEmpleados.obtener_todos()
    empleados = GestionEmpleados(datos)
    if empleados == None:
        print("No hay empleados en la base de datos ")
        time.sleep(2)
    else:
        print(empleados)
        id = int(input("Ingrese valor de ID del Empleado que desea Modificar: "))
        datos = GestionEmpleados.obtener_uno(id)
        empleado = Empleado(datos[0],datos[1],datos[2],datos[3],datos[4],datos[5],datos[6],datos[7],datos[8])
        print(empleado)

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
            datos = GestionDepartamentos()
            if datos == None:
                print("No hay departamentos en la base de datos ")
                time.sleep(1)
                print("Volviendo...")
                time.sleep(2)
                return
            else:
                print(datos)
            time.sleep(2)
            while True:
                try:
                    opcion = int(input("INGRESE ID DE DEPARTAMENTO AL QUE DESEA REEMPLAZAR : "))
                    datos = GestionDepartamentos.mostrar_uno(opcion)
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

        GestionEmpleados.editar_empleado(listanuevos)
        time.sleep(2)

#WORKING (revisar el tema de resgistros, tanto foranea en bd como uso de la clase)
def eliminardatos_empleados():
    os.system('cls')
    print("=========================================")
    print("       MODULO ELIMINAR EMPLEADOS         ")
    print("=========================================")

    while True:
        datos = GestionEmpleados.obtener_todos()
        empleados = GestionEmpleados(datos)
        print(empleados)
        if empleados == None:
            break
        try:
            elim = int(input("Ingrese valor de ID del Empleado que desea Eliminar : "))
        except ValueError:
            print("Ingrese un numero.")
            time.sleep(2)
            continue
        datos = GestionEmpleados.obtener_uno(elim)
        if datos == None:
            print(" No hay empleados con ese id ")
            print('Volviendo al menu...')           
            break
        else:
            empleado = Empleado(datos[1],datos[2],datos[3],datos[4],datos[5],datos[6],datos[7],datos[8], datos[9], datos[0])
            registros_empleado = GestionRegistros.obtener_por_empleado(elim)
            print(empleado)
            if registros_empleado == None:
                print('Este empleado no presenta registros de tiempo')
                opm = input('ESTA SEGURO QUE DESEA ELIMINAR ESTE EMPLEADO? SI/NO ')
                if opm.lower() == "si":
                    GestionEmpleados.eliminar(elim)
                    print(f'empleado ID: {empleado.id} eliminado exitosamente')
                    time.sleep(1)
                    break
                else:
                    print('Operacion cancelada, volviendo al menu... ')
                    time.sleep(1)
                    break
            else:
                for dato in registros_empleado:
                    print(
                    " ID : {} - FECHA : {} - CANTIDAD DE HORAS TRABAJADAS : {} - DESCRIPCION : {} - ID EMPLEADO VINCULADO : {}".format(dato[0], dato[1], dato[2], dato[3], dato[4]))
                    print("--------------------------------------------------------------------------------------------------------------------------------------------------------")
                opm = input("SI ELIMINA ESTE EMPLEADO TAMBIEN ELIMINARA {} REGISTROS DE TIEMPO VINCULADOS A ESTE MISMO, ESTA SEGURO? : [SI/NO] ".format(registros_empleado))
                if opm.lower() == "si":
                    GestionEmpleados.eliminar(elim)
                    print(f'empleado ID: {empleado.id} eliminado exitosamente')
                    time.sleep(1)
                    break
                else:
                    print('Operacion cancelada, volviendo al menu... ')
                    time.sleep(1)
                    break
            
#FALTA TESTEARLO
def eliminar_varios(id_depto):
    while True:
        datos = GestionEmpleados.consulta_dpto(id_depto)
        lista_empleados = []
        if datos == None:
            print("No hay empleados vinculados a este departamento...")
            time.sleep(1)
            break
        else:
            print(f"ID Departamento: {id_depto}")
            for dato in datos:
                empleado = Empleado(dato[1],dato[2],dato[3],dato[4],dato[5],dato[6],dato[7],dato[8], dato[9], dato[0])
                lista_empleados.append(empleado)
            opcion = input(f'¿Desea eliminar {len(lista_empleados)} empleados?')

            if opcion.lower() == 'si':
                for empleado in lista_empleados:
                    GestionEmpleados.eliminar(empleado.id)
            else:
                print('Operacion cancelada, volviendo al menu...')
                time.sleep(2)
        
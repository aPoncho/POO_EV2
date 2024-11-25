import os
import requests
import mysql.connector



def obtener_datos_desde_api():
    url = "https://raw.githubusercontent.com/aPoncho/POO_EV2/refs/heads/master/datos.json"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print("Error al hacer la solicitud:", e)
        return None
    
def ingresar_jason(data):
    print("Datos de json")
    data = data
    print(data)

    conn = mysql.connector.connect(
        host = 'localhost',
        user = 'userempresa',
        password = 'V3ntana.13',
        db = 'empresa'
    )

    cursor= conn.cursor()
    for item in data: 
        try:
            cursor.execute('''
                INSERT INTO empleados (RUT_e, Nombre_e, Apellido_e, Direccion_e, Fono_e, Correo_e, Cargo_e, Salario_e, Departamento_e)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            ''', (item['run'], item['nombre'], item['apellido'], item['direccion'], item['fono'], item['correo'], item['cargo'], item['salario'], item['depto']))
        except mysql.connector.Error as err:
            print(f"Error al insertar los datos: {err}")

    conn.commit()
    input("\n\n Datos Json traspasados con éxito...")
    conn.close()
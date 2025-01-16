## Crear tabla 'personas' en la base de datos 'oltp'

import psycopg2
from psycopg2 import sql

def connect_and_create_table():
    # Datos de conexión
    host = "192.168.141.128"  
    dbname = "oltp"  
    user = "juan"  
    password = "juan"  

    try:
        # Conexión a la base de datos
        connection = psycopg2.connect(
            host=host,
            dbname=dbname,
            user=user,
            password=password
        )
        cursor = connection.cursor()

        # Comando SQL para crear la tabla
        create_table_query = sql.SQL(
            """
            CREATE TABLE IF NOT EXISTS personas (
                person_id SERIAL PRIMARY KEY,
                per_acv VARCHAR(255),
                per_cli VARCHAR(255),
                per_fecha_de_nacimiento DATE,
                per_apellido VARCHAR(255),
                per_nombre VARCHAR(255),
                per_email VARCHAR(255),
                per_nacionalidad VARCHAR(255),
                per_alta_fecha DATE,
                per_baja_fecha DATE
            );
            """
        )

        # Ejecutar el comando para crear la tabla
        cursor.execute(create_table_query)
        connection.commit()
        print("Tabla 'personas' creada exitosamente.")

    except psycopg2.Error as e:
        print(f"Error al conectar o crear la tabla: {e}")

    finally:
        # Cerrar la conexión
        if cursor:
            cursor.close()
        if connection:
            connection.close()
            print("Conexión cerrada.")

if __name__ == "__main__":
    connect_and_create_table()

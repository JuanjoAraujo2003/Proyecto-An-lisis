## Crear tabla 'sor_personas' en la base de datos 'sor'

import psycopg2
from psycopg2 import sql

def create_sor_personas_table():
    # Datos de conexión
    host = "192.168.141.128"
    dbname = "sor"
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

        # Crear tabla sor_personas
        create_table_query = sql.SQL(
            """
            CREATE TABLE IF NOT EXISTS sor_personas (
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
        cursor.execute(create_table_query)
        connection.commit()
        print("Tabla 'sor_personas' creada exitosamente.")

    except psycopg2.Error as e:
        print(f"Error al crear la tabla 'sor_personas': {e}")

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

if __name__ == "__main__":
    create_sor_personas_table()

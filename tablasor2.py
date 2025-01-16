## Crear tabla 'sor_cuentas' en la base de datos 'sor'

import psycopg2
from psycopg2 import sql

def create_sor_cuentas_table():
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

        # Crear tabla sor_cuentas
        create_table_query = sql.SQL(
            """
            CREATE TABLE IF NOT EXISTS sor_cuentas (
                cta_id SERIAL PRIMARY KEY,
                cta_persona INT REFERENCES sor_personas(person_id),
                cta_pro_producto VARCHAR(255),
                cta_num VARCHAR(255),
                cta_monto_origen FLOAT,
                cta_deuda_vence FLOAT,
                cta_tco VARCHAR(150)
            );
            """
        )
        cursor.execute(create_table_query)
        connection.commit()
        print("Tabla 'sor_cuentas' creada exitosamente.")

    except psycopg2.Error as e:
        print(f"Error al crear la tabla 'sor_cuentas': {e}")

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

if __name__ == "__main__":
    create_sor_cuentas_table()

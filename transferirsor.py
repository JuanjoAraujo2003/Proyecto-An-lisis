##Tranferir los datos de la tabla 'stg_personas' de la base de datos 'staging' a la tabla 'sor_personas' de la base de datos 'sor'

import psycopg2

def transfer_personas_to_sor():
    # Datos de conexión
    staging_conn_params = {
        "host": "192.168.141.128",
        "dbname": "staging",
        "user": "juan",
        "password": "juan"
    }
    sor_conn_params = {
        "host": "192.168.141.128",
        "dbname": "sor",
        "user": "juan",
        "password": "juan"
    }

    try:
        # Conexión a Staging y SOR
        staging_conn = psycopg2.connect(**staging_conn_params)
        sor_conn = psycopg2.connect(**sor_conn_params)

        staging_cursor = staging_conn.cursor()
        sor_cursor = sor_conn.cursor()

        # Leer datos desde Staging
        staging_cursor.execute("SELECT * FROM stg_personas;")
        rows = staging_cursor.fetchall()

        # Insertar datos en SOR
        insert_query = """
            INSERT INTO sor_personas (
                person_id, per_acv, per_cli, per_fecha_de_nacimiento, 
                per_apellido, per_nombre, per_email, per_nacionalidad, 
                per_alta_fecha, per_baja_fecha
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        """
        for row in rows:
            sor_cursor.execute(insert_query, row)

        sor_conn.commit()
        print("Datos transferidos de 'stg_personas' a 'sor_personas' exitosamente.")

    except psycopg2.Error as e:
        print(f"Error al transferir datos: {e}")

    finally:
        # Cerrar conexiones
        if staging_cursor:
            staging_cursor.close()
        if staging_conn:
            staging_conn.close()
        if sor_cursor:
            sor_cursor.close()
        if sor_conn:
            sor_conn.close()

if __name__ == "__main__":
    transfer_personas_to_sor()

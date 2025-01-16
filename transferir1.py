##Tranferir los datos de la tabla 'personas' de la base de datos 'oltp' a la tabla 'stg_personas' de la base de datos 'staging'

import psycopg2

def transfer_personas_to_staging():
    # Conexión a las bases de datos
    oltp_conn_params = {
        "host": "192.168.141.128",
        "dbname": "oltp",
        "user": "juan",
        "password": "juan"
    }
    staging_conn_params = {
        "host": "192.168.141.128",
        "dbname": "staging",
        "user": "juan",
        "password": "juan"
    }

    try:
        # Conexiones
        oltp_conn = psycopg2.connect(**oltp_conn_params)
        staging_conn = psycopg2.connect(**staging_conn_params)

        oltp_cursor = oltp_conn.cursor()
        staging_cursor = staging_conn.cursor()

        # Consulta para obtener los datos de OLTP
        oltp_cursor.execute("SELECT * FROM personas;")
        personas_data = oltp_cursor.fetchall()

        # Insertar datos en Staging
        for row in personas_data:
            staging_cursor.execute("""
                INSERT INTO stg_personas (
                    person_id, per_acv, per_cli, per_fecha_de_nacimiento,
                    per_apellido, per_nombre, per_email, per_nacionalidad,
                    per_alta_fecha, per_baja_fecha
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
            """, row)

        staging_conn.commit()
        print("Datos transferidos de 'personas' a 'stg_personas' exitosamente.")

    except psycopg2.Error as e:
        print(f"Error durante la transferencia de 'personas': {e}")

    finally:
        # Cerrar conexiones
        if oltp_cursor:
            oltp_cursor.close()
        if staging_cursor:
            staging_cursor.close()
        if oltp_conn:
            oltp_conn.close()
        if staging_conn:
            staging_conn.close()

if __name__ == "__main__":
    transfer_personas_to_staging()

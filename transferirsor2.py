##Tranferir los datos de la tabla 'stg_cuentas' de la base de datos 'staging' a la tabla 'sor_cuentas' de la base de datos 'sor' 

import psycopg2

def transfer_cuentas_to_sor():
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
        staging_cursor.execute("SELECT * FROM stg_cuentas;")
        rows = staging_cursor.fetchall()

        # Insertar datos en SOR
        insert_query = """
            INSERT INTO sor_cuentas (
                cta_id, cta_persona, cta_pro_producto, cta_num, 
                cta_monto_origen, cta_deuda_vence, cta_tco
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s);
        """
        for row in rows:
            sor_cursor.execute(insert_query, row)

        sor_conn.commit()
        print("Datos transferidos de 'stg_cuentas' a 'sor_cuentas' exitosamente.")

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
    transfer_cuentas_to_sor()

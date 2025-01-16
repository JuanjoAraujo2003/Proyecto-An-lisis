##Tranferir los datos de la tabla 'cuentas' de la base de datos 'oltp' a la tabla 'stg_cuentas' de la base de datos 'staging'

import psycopg2

def transfer_cuentas_to_staging():
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
        oltp_conn = psycopg2.connect(**oltp_conn_params)
        staging_conn = psycopg2.connect(**staging_conn_params)

        oltp_cursor = oltp_conn.cursor()
        staging_cursor = staging_conn.cursor()

        oltp_cursor.execute("SELECT * FROM cuentas;")
        cuentas_data = oltp_cursor.fetchall()

        for row in cuentas_data:
            staging_cursor.execute("""
                INSERT INTO stg_cuentas (
                    cta_id, cta_persona, cta_pro_producto, cta_num,
                    cta_monto_origen, cta_deuda_vence, cta_tco
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s);
            """, row)

        staging_conn.commit()
        print("Datos transferidos de 'cuentas' a 'stg_cuentas' exitosamente.")

    except psycopg2.Error as e:
        print(f"Error durante la transferencia de 'cuentas': {e}")

    finally:
        if oltp_cursor:
            oltp_cursor.close()
        if staging_cursor:
            staging_cursor.close()
        if oltp_conn:
            oltp_conn.close()
        if staging_conn:
            staging_conn.close()

if __name__ == "__main__":
    transfer_cuentas_to_staging()

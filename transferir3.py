##Tranferir los datos de la tabla 'pagos' de la base de datos 'oltp' a la tabla 'stg_pagos' de la base de datos 'staging'

import psycopg2

def transfer_pagos_to_staging():
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

        oltp_cursor.execute("SELECT * FROM pagos;")
        pagos_data = oltp_cursor.fetchall()

        for row in pagos_data:
            staging_cursor.execute("""
                INSERT INTO stg_pagos (
                    id_pago, id_cuenta, fecha_pago,
                    monto_pagado, estado_pago
                )
                VALUES (%s, %s, %s, %s, %s);
            """, row)

        staging_conn.commit()
        print("Datos transferidos de 'pagos' a 'stg_pagos' exitosamente.")

    except psycopg2.Error as e:
        print(f"Error durante la transferencia de 'pagos': {e}")

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
    transfer_pagos_to_staging()

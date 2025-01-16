## Limpieza de datos en la tabla 'stg_pagos' de la base de datos 'staging'

import psycopg2

def clean_pagos():
    host = "192.168.141.128"
    dbname = "staging"
    user = "juan"
    password = "juan"

    try:
        connection = psycopg2.connect(host=host, dbname=dbname, user=user, password=password)
        cursor = connection.cursor()

        # Eliminar pagos con cuentas no válidas
        cursor.execute("""
            DELETE FROM stg_pagos
            WHERE id_cuenta NOT IN (
                SELECT cta_id FROM stg_cuentas
            );
        """)

        # Corregir montos negativos
        cursor.execute("""
            UPDATE stg_pagos
            SET monto_pagado = 0.0
            WHERE monto_pagado < 0;
        """)

        # Estandarizar estados de pago
        cursor.execute("""
            UPDATE stg_pagos
            SET estado_pago = CASE
                WHEN estado_pago NOT IN ('Pagado', 'Pendiente', 'Atrasado') THEN 'Desconocido'
                ELSE estado_pago
            END;
        """)

        connection.commit()
        print("Limpieza y normalización de 'stg_pagos' completada.")

    except psycopg2.Error as e:
        print(f"Error durante la limpieza de 'stg_pagos': {e}")

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

if __name__ == "__main__":
    clean_pagos()

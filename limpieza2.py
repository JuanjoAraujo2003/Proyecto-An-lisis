## Limpieza de datos en la tabla 'stg_cuentas' de la base de datos 'staging'

import psycopg2

def clean_cuentas():
    host = "192.168.141.128"
    dbname = "staging"
    user = "juan"
    password = "juan"

    try:
        connection = psycopg2.connect(host=host, dbname=dbname, user=user, password=password)
        cursor = connection.cursor()

        # Eliminar cuentas con personas no válidas
        cursor.execute("""
            DELETE FROM stg_cuentas
            WHERE cta_persona NOT IN (
                SELECT person_id FROM stg_personas
            );
        """)

        # Completar valores nulos en montos
        cursor.execute("""
            UPDATE stg_cuentas
            SET cta_deuda_vence = 0.0
            WHERE cta_deuda_vence IS NULL;
        """)

        # Estandarizar tipos de contrato
        cursor.execute("""
            UPDATE stg_cuentas
            SET cta_tco = CASE
                WHEN cta_tco IS NULL THEN 'Contrato Desconocido'
                WHEN cta_tco NOT IN ('Contrato Anual', 'Contrato Mensual') THEN 'Contrato Otros'
                ELSE cta_tco
            END;
        """)

        connection.commit()
        print("Limpieza y normalización de 'stg_cuentas' completada.")

    except psycopg2.Error as e:
        print(f"Error durante la limpieza de 'stg_cuentas': {e}")

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

if __name__ == "__main__":
    clean_cuentas()

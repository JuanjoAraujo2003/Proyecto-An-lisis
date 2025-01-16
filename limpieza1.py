##Limpieza de datos en la tabla 'stg_personas' de la base de datos 'staging'

import psycopg2

def clean_personas():
    host = "192.168.141.128"
    dbname = "staging"
    user = "juan"
    password = "juan"

    try:
        connection = psycopg2.connect(host=host, dbname=dbname, user=user, password=password)
        cursor = connection.cursor()

        # Eliminar duplicados por correo electrónico
        cursor.execute("""
            DELETE FROM stg_personas
            WHERE person_id NOT IN (
                SELECT MIN(person_id)
                FROM stg_personas
                GROUP BY per_email
            );
        """)

        # Completar valores nulos
        cursor.execute("""
            UPDATE stg_personas
            SET per_nacionalidad = 'Desconocida'
            WHERE per_nacionalidad IS NULL;
        """)

        # Validar integridad de fechas
        cursor.execute("""
            DELETE FROM stg_personas
            WHERE per_baja_fecha < per_alta_fecha;
        """)

        connection.commit()
        print("Limpieza y normalización de 'stg_personas' completada.")

    except psycopg2.Error as e:
        print(f"Error durante la limpieza de 'stg_personas': {e}")

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

if __name__ == "__main__":
    clean_personas()

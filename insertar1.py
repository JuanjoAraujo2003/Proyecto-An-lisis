##Insertar datos a la tabla 'personas' de la base de datos 'oltp' con datos falsos

import psycopg2
from faker import Faker

def insert_fake_data():
    # Datos de conexión
    host = "192.168.141.128"  
    dbname = "oltp"  
    user = "juan"  
    password = "juan"  
    fake = Faker()
    connection = None
    cursor = None

    try:
        # Conexión a la base de datos
        connection = psycopg2.connect(
            host=host,
            dbname=dbname,
            user=user,
            password=password
        )
        cursor = connection.cursor()

        # Insertar 35 datos falsos en la tabla 'personas'
        for _ in range(35):
            cursor.execute(
                """
                INSERT INTO personas (
                    per_acv, per_cli, per_fecha_de_nacimiento, per_apellido, per_nombre,
                    per_email, per_nacionalidad, per_alta_fecha, per_baja_fecha
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                """,
                (
                    fake.word(),
                    fake.word(),
                    fake.date_of_birth(minimum_age=18, maximum_age=90),
                    fake.last_name(),
                    fake.first_name(),
                    fake.email(),
                    fake.country(),
                    fake.date_this_decade(before_today=True, after_today=False),
                    fake.date_this_decade(before_today=False, after_today=True)
                )
            )

        # Confirmar los cambios
        connection.commit()
        print("35 datos falsos insertados en la tabla 'personas'.")

    except psycopg2.Error as e:
        print(f"Error al insertar datos falsos: {e}")

    finally:
        # Cerrar la conexión
        if cursor:
            cursor.close()
        if connection:
            connection.close()
            print("Conexión cerrada.")

if __name__ == "__main__":
    insert_fake_data()

##Insertar datos a la tabla 'cuentas' de la base de datos 'oltp' con datos falsos

import psycopg2
from faker import Faker
import random

def insert_fake_data_cuentas():
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

        # Obtener IDs de personas para referencias
        cursor.execute("SELECT person_id FROM personas;")
        person_ids = [row[0] for row in cursor.fetchall()]

        if not person_ids:
            print("No hay registros en la tabla 'personas'.")
            return

        # Tipos de contrato predefinidos
        tipos_contrato = ["Contrato de cesión por deuda", "Contrato por prenda"]

        # Insertar 35 datos falsos en la tabla 'cuentas'
        for _ in range(35):
            monto_origen = round(random.uniform(500, 10000), 2)  # Deuda inicial entre 500 y 10,000
            deuda_vence = round(random.uniform(0, monto_origen), 2)  # Deuda actual <= monto_origen
            tipo_contrato = random.choice(tipos_contrato)  # Tipo de contrato aleatorio

            cursor.execute(
                """
                INSERT INTO cuentas (
                    cta_persona, cta_pro_producto, cta_num, cta_monto_origen,
                    cta_deuda_vence, cta_tco
                ) VALUES (%s, %s, %s, %s, %s, %s)
                """,
                (
                    random.choice(person_ids),
                    fake.word(),
                    fake.uuid4(),
                    monto_origen,
                    deuda_vence,
                    tipo_contrato
                )
            )

        # Confirmar los cambios
        connection.commit()
        print("35 datos falsos insertados en la tabla 'cuentas'.")

    except psycopg2.Error as e:
        print(f"Error al insertar datos falsos en cuentas: {e}")

    finally:
        # Cerrar la conexión
        if cursor is not None:
            cursor.close()
        if connection is not None:
            connection.close()
            print("Conexión cerrada.")

if __name__ == "__main__":
    insert_fake_data_cuentas()

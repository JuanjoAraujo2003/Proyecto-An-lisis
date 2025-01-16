##Insertar datos a la tabla 'pagos' de la base de datos 'oltp' con datos falsos

import psycopg2
from faker import Faker
import random

def insert_fake_data_pagos():
    
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

        # Obtener IDs de cuentas para referencias
        cursor.execute("SELECT cta_id FROM cuentas;")
        cuenta_ids = [row[0] for row in cursor.fetchall()]

        if not cuenta_ids:
            print("No hay registros en la tabla 'cuentas'.")
            return

        # Estados de pago predefinidos
        estados_pago = ["Completado", "Pendiente", "Fallido"]

        # Insertar 35 datos falsos en la tabla 'pagos'
        for _ in range(35):
            cursor.execute(
                """
                INSERT INTO pagos (
                    id_cuenta, fecha_pago, monto_pagado, estado_pago
                ) VALUES (%s, %s, %s, %s)
                """,
                (
                    random.choice(cuenta_ids),
                    fake.date_this_year(before_today=True, after_today=False),
                    round(random.uniform(50, 5000), 2),  # Monto pagado entre 50 y 5000
                    random.choice(estados_pago)  # Estado de pago aleatorio
                )
            )

        # Confirmar los cambios
        connection.commit()
        print("35 datos falsos insertados en la tabla 'pagos'.")

    except psycopg2.Error as e:
        print(f"Error al insertar datos falsos en pagos: {e}")

    finally:
        # Cerrar la conexión
        if cursor is not None:
            cursor.close()
        if connection is not None:
            connection.close()
            print("Conexión cerrada.")

if __name__ == "__main__":
    insert_fake_data_pagos()

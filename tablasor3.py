## Crear tabla 'sor_pagos' en la base de datos 'sor'


import psycopg2
from psycopg2 import sql

def create_sor_pagos_table():
    # Datos de conexión
    host = "192.168.141.128"
    dbname = "sor"
    user = "juan"
    password = "juan"

    try:
        # Conexión a la base de datos
        connection = psycopg2.connect(
            host=host,
            dbname=dbname,
            user=user,
            password=password
        )
        cursor = connection.cursor()

        # Crear tabla sor_pagos
        create_table_query = sql.SQL(
            """
            CREATE TABLE IF NOT EXISTS sor_pagos (
                id_pago SERIAL PRIMARY KEY,
                id_cuenta INT NOT NULL,
                fecha_pago DATE NOT NULL,
                monto_pagado DECIMAL(10, 2) NOT NULL,
                estado_pago VARCHAR(50) NOT NULL,
                FOREIGN KEY (id_cuenta) REFERENCES sor_cuentas(cta_id) ON DELETE CASCADE
            );
            """
        )
        cursor.execute(create_table_query)
        connection.commit()
        print("Tabla 'sor_pagos' creada exitosamente.")

    except psycopg2.Error as e:
        print(f"Error al crear la tabla 'sor_pagos': {e}")

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

if __name__ == "__main__":
    create_sor_pagos_table()

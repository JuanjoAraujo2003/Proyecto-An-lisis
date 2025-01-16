## Crear tabla 'stg_pagos' en la base de datos 'staging'


import psycopg2
from psycopg2 import sql

def connect_and_create_table():
    # Datos de conexión
    host = "192.168.141.128"  
    dbname = "staging"     
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

        # Comando SQL para crear la tabla
        create_table_query = sql.SQL(
            """
            CREATE TABLE IF NOT EXISTS stg_pagos (
                id_pago SERIAL PRIMARY KEY,
                id_cuenta INT NOT NULL,
                fecha_pago DATE NOT NULL,
                monto_pagado DECIMAL(10, 2) NOT NULL,
                estado_pago VARCHAR(50) NOT NULL,
                FOREIGN KEY (id_cuenta) REFERENCES stg_cuentas(cta_id) ON DELETE CASCADE
            );
            """
        )

        # Ejecutar el comando para crear la tabla
        cursor.execute(create_table_query)
        connection.commit()
        print("Tabla 'stg_pagos' creada exitosamente.")

    except psycopg2.Error as e:
        print(f"Error al conectar o crear la tabla: {e}")

    finally:
        # Cerrar la conexión
        if cursor:
            cursor.close()
        if connection:
            connection.close()
            print("Conexión cerrada.")

if __name__ == "__main__":
    connect_and_create_table()

## Crear tabla 'pagos' en la base de datos 'oltp'

import psycopg2

def create_table_pagos():
    # Datos de conexión
    host = "192.168.141.128"  
    dbname = "oltp"  
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

        # Crear la tabla 'pagos'
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS pagos (
                id_pago SERIAL PRIMARY KEY,
                id_cuenta INT NOT NULL,
                fecha_pago DATE NOT NULL,
                monto_pagado DECIMAL(10, 2) NOT NULL,
                estado_pago VARCHAR(50) NOT NULL,
                FOREIGN KEY (id_cuenta) REFERENCES cuentas(cta_id) ON DELETE CASCADE
            );
            """
        )

        # Confirmar los cambios
        connection.commit()
        print("Tabla 'pagos' creada exitosamente.")

    except psycopg2.Error as e:
        print(f"Error al crear la tabla 'pagos': {e}")

    finally:
        # Cerrar la conexión
        if cursor is not None:
            cursor.close()
        if connection is not None:
            connection.close()
            print("Conexión cerrada.")

if __name__ == "__main__":
    create_table_pagos()

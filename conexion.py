from sqlalchemy import create_engine, text

def connect_to_postgres():
    try:
        
        username = "juan"
        password = "juan"
        host = "192.168.141.128"
        port = "5432"
        database = "sor"

        # Crear la URL de conexión con codificación
        db_url = f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}"

        # Crear el motor de conexión
        engine = create_engine(db_url, connect_args={"client_encoding": "utf8"})

        # Probar la conexión
        with engine.connect() as connection:
            result = connection.execute(text("SELECT version();"))
            for row in result:
                print(f"Versión de PostgreSQL: {row[0]}")

    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")

if __name__ == "__main__":
    connect_to_postgres()

# Proyecto de Analisis de datos
# Integrantes: Juan Araujo, Didier Guerrero, Anthony Rodriguez.

Este archivo contiene los pasos, comandos y scripts utilizados para gestionar las bases de datos **OLTP**, **Staging** y **SOR** en PostgreSQL dentro del entorno de Kali Linux.

---

## Requisitos Previos

1. **Kali Linux** instalado y actualizado.
2. PostgreSQL configurado y en ejecución.
3. Python 3.x instalado junto con las librerías necesarias (`psycopg2`, `faker`).
4. Archivos de scripts listos para ejecutar.

---

## 1. Conexión a PostgreSQL

### Iniciar PostgreSQL:
```bash
sudo service postgresql start
```

### Habilitar PostgreSQL:
```bash
sudo systemctl enable postgresql
```

### Crear un Usuario para la base de datos:
```bash
create user ... with password `...`
```

### Crear base de datos 
```bash
CREATE DATABASE oltp;
CREATE DATABASE staging;
CREATE DATABASE sor;
```

### Verificar el estatus del servicio
```bash
sudo service postgresql status
```

### Conexion al servicio de postgres
```bash
sudo -u postgres psql
```

### Conectarse a una base de datos
```bash
\connect 'base de datos'
```

### Estructuras de Tablas
```bash
CREATE TABLE personas (
    person_id SERIAL PRIMARY KEY,
    per_acv VARCHAR(255),
    per_cli VARCHAR(255),
    per_fecha_de_nacimiento DATE,
    per_apellido VARCHAR(255),
    per_nombre VARCHAR(255),
    per_email VARCHAR(255),
    per_nacionalidad VARCHAR(255),
    per_alta_fecha DATE,
    per_baja_fecha DATE
);

CREATE TABLE cuentas (
    cta_id SERIAL PRIMARY KEY,
    cta_persona INT REFERENCES personas(person_id),
    cta_pro_producto VARCHAR(255),
    cta_num VARCHAR(255),
    cta_monto_origen FLOAT,
    cta_deuda_vence FLOAT,
    cta_tco VARCHAR(150)
);

CREATE TABLE pagos (
    id_pago SERIAL PRIMARY KEY,
    id_cuenta INT NOT NULL REFERENCES cuentas(cta_id) ON DELETE CASCADE,
    fecha_pago DATE NOT NULL,
    monto_pagado DECIMAL(10, 2) NOT NULL,
    estado_pago VARCHAR(50) NOT NULL
);
```

### Exportar datos a csv
```bash
psql -d sor -c "\COPY sor_personas TO '/ruta/personas.csv' CSV HEADER;"
psql -d sor -c "\COPY sor_cuentas TO '/ruta/cuentas.csv' CSV HEADER;"
psql -d sor -c "\COPY sor_pagos TO '/ruta/pagos.csv' CSV HEADER;"

```




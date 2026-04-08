import psycopg2
from psycopg2 import sql
import os
from dotenv import load_dotenv

load_dotenv()


def obtener_conexion():
    db_host = os.getenv('DB_HOST')
    db_name = os.getenv('DB_NAME')
    db_user = os.getenv('DB_USER')

    if not all([db_host, db_name, db_user]):
        print("Error: Faltan variables de configuración en el archivo .env")
        return None

    try:
        conexion = psycopg2.connect(
            host=db_host,
            port=os.getenv('DB_PORT', '5432'),
            database=db_name,
            user=db_user,
            password=os.getenv('DB_PASSWORD')
        )
        return conexion
    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None


def crear_base_de_datos():
    conn = None
    try:
        conn = psycopg2.connect(
            host=os.getenv('DB_HOST'),
            port=os.getenv('DB_PORT', '5432'),
            dbname="postgres",
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
        )
        conn.autocommit = True
        with conn.cursor() as cursor:
            cursor.execute(
                "select 1 from pg_database where datname=%s;", (os.getenv(
                    'DB_NAME'),)
            )
            existe = cursor.fetchone()
            if not existe:
                db_name = os.getenv('DB_NAME')
                cursor.execute(sql.SQL("CREATE DATABASE {}").format(
                    sql.Identifier(db_name)))
                print(
                    f"Base de datos '{os.getenv('DB_NAME')}' creada exitosamente.")
            else:
                print(f"La base de datos '{os.getenv('DB_NAME')}' ya existe.")
    finally:
        if conn:
            conn.close()


def init_db():
    crear_base_de_datos()
    conn = obtener_conexion()
    if conn is None:
        print("No se pudo establecer la conexión para inicializar la base de datos.")
        return
    try:
        with conn:
            with conn.cursor() as cursor:
                cursor.execute("""
                CREATE TABLE IF NOT EXISTS categorias (
                    id SERIAL PRIMARY KEY,
                    nombre VARCHAR(100) NOT NULL unique,
                    descripcion TEXT
                );
                
                CREATE TABLE IF NOT EXISTS productos (
                    id SERIAL PRIMARY KEY,
                    nombre VARCHAR(100) NOT NULL,
                    precio DECIMAL(10, 2) NOT NULL,
                    stock INT NOT NULL DEFAULT 0 CHECK (stock >= 0),
                    categoria_id INTEGER REFERENCES categorias(id) ON DELETE SET NULL
                );
                
                CREATE TABLE IF NOT EXISTS clientes (
                    id SERIAL PRIMARY KEY,
                    nombre VARCHAR(100) NOT NULL,
                    email VARCHAR(100) NOT NULL UNIQUE,
                    telefono VARCHAR(20)
                );
                
                
                CREATE TABLE IF NOT EXISTS ventas (
                    id         SERIAL PRIMARY KEY,
                    cliente_id INTEGER NOT NULL REFERENCES clientes(id) ON DELETE CASCADE,
                    total      NUMERIC(10,2) NOT NULL DEFAULT 0,
                    fecha     DATE NOT NULL DEFAULT CURRENT_DATE
                );

                CREATE TABLE IF NOT EXISTS detalle_ventas (
                    id          SERIAL PRIMARY KEY,
                    id_venta    INTEGER NOT NULL REFERENCES ventas(id) ON DELETE CASCADE,
                    id_producto INTEGER NOT NULL REFERENCES productos(id),
                    cantidad    INTEGER NOT NULL CHECK (cantidad > 0),
                    precio_unit NUMERIC(10,2) NOT NULL
                );
            """)
            print("Tablas verificadas/creadas correctamente.")
    except Exception as e:
        print(f"Error al crear las tablas: {e}")
    finally:
        conn.close()

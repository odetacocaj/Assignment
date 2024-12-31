import psycopg2
from psycopg2 import sql
from dotenv import load_dotenv
import os
from urllib.parse import urlparse

def get_db_connection():
    load_dotenv()

    db_url = os.getenv("DATABASE_URL")

    if db_url:
        parsed_url = urlparse(db_url)

        db_name = parsed_url.path[1:]  
        db_user = parsed_url.username
        db_password = parsed_url.password
        db_host = parsed_url.hostname
        db_port = parsed_url.port

        conn_str = f"dbname={db_name} user={db_user} password={db_password} host={db_host} port={db_port}"

    else:
        db_name = os.getenv("DB_NAME")
        db_user = os.getenv("DB_USER")
        db_password = os.getenv("DB_PASSWORD")
        db_host = os.getenv("DB_HOST", "localhost")
        db_port = os.getenv("DB_PORT", "5432")

        conn_str = f"dbname=postgres user={db_user} password={db_password} host={db_host} port={db_port}"

  
    conn = psycopg2.connect(conn_str)
    conn.autocommit = True
    cur = conn.cursor()

 
    cur.execute(sql.SQL("SELECT 1 FROM pg_catalog.pg_database WHERE datname = %s"), [db_name])
    if not cur.fetchone():
        print(f"Database {db_name} does not exist. Creating it now...")
        cur.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(db_name)))

    conn.close()

    
    conn = psycopg2.connect(dbname=db_name, user=db_user, password=db_password, host=db_host, port=db_port)
    return conn

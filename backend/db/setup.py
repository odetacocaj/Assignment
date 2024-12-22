import psycopg2
from psycopg2 import sql
from dotenv import load_dotenv
import os

def create_tables():
    load_dotenv()

    db_name = os.getenv("DB_NAME")
    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")

    conn = psycopg2.connect(dbname="postgres", user=db_user, password=db_password)
    conn.autocommit = True
    cur = conn.cursor()


    cur.execute(sql.SQL("SELECT 1 FROM pg_catalog.pg_database WHERE datname = %s"), [db_name])
    if not cur.fetchone():
        cur.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(db_name)))

    cur.close()
    conn.close()


    conn = psycopg2.connect(dbname=db_name, user=db_user, password=db_password)
    cur = conn.cursor()


    cur.execute("""
    CREATE TABLE IF NOT EXISTS characters (
        id SERIAL PRIMARY KEY,
        name TEXT,
        actor TEXT,
        image_url TEXT,
        search_vector tsvector  -- Added search_vector column for full-text search
    );
    """)


    cur.execute("""
    CREATE INDEX IF NOT EXISTS search_idx ON characters USING GIN (search_vector);
    """)

    conn.commit()
    cur.close()
    conn.close()

if __name__ == "__main__":
    create_tables()

import psycopg2
from psycopg2 import sql
from dotenv import load_dotenv
import os

def create_tables():
    load_dotenv()  

   
    db_url = os.getenv("DATABASE_URL")

    if db_url:
        
        conn_str = db_url
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
        cur.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(db_name)))

   
    conn.close() 
    conn = psycopg2.connect(dbname=db_name, user=db_user, password=db_password, host=db_host, port=db_port)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS characters (
        id SERIAL PRIMARY KEY,
        name TEXT NOT NULL,
        actor TEXT NOT NULL,
        image_url TEXT,
        description TEXT,  -- Nullable field for description
        category TEXT NOT NULL,  -- For distinguishing between 'norsemen', 'vikings', etc.
        search_vector tsvector,
        CONSTRAINT unique_name_actor_category UNIQUE (name, actor, category)  -- Unique constraint
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

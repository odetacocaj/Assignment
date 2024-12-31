from psycopg2 import sql
from .db_connection import get_db_connection  

def create_tables():
    conn = get_db_connection()  
    conn.autocommit = True
    cur = conn.cursor()

    db_name = conn.get_dsn_parameters()['dbname']  
    cur.execute(sql.SQL("SELECT 1 FROM pg_catalog.pg_database WHERE datname = %s"), [db_name])
    if not cur.fetchone():
        cur.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(db_name)))

    conn.close()

   
    conn = get_db_connection()  
    cur = conn.cursor()

   
    cur.execute("""
    CREATE TABLE IF NOT EXISTS characters (
        id SERIAL PRIMARY KEY,
        name TEXT NOT NULL,
        actor TEXT NOT NULL,
        image_url TEXT,
        description TEXT,  
        category TEXT NOT NULL,  
        search_vector tsvector,
        CONSTRAINT unique_name_actor_category UNIQUE (name, actor, category)  
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

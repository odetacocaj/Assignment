import psycopg2
from dotenv import load_dotenv
import os

def create_tables():
    load_dotenv() 

    db_name = os.getenv("DB_NAME")
    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")

    conn = psycopg2.connect(dbname=db_name, user=db_user, password=db_password)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS characters (
        id SERIAL PRIMARY KEY,
        name TEXT,
        actor TEXT,
        image_url TEXT,
        
    );
    """)


    conn.commit()
    cur.close()
    conn.close()

if __name__ == "__main__":
    create_tables()

import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def get_db():
   
    db_url = os.getenv("DATABASE_URL")

    if db_url:
       
        conn = psycopg2.connect(db_url)
    else:
       
        db_name = os.getenv("DB_NAME")
        db_user = os.getenv("DB_USER")
        db_password = os.getenv("DB_PASSWORD")
        db_host = os.getenv("DB_HOST", "localhost")  
        db_port = os.getenv("DB_PORT", "5432")  

    
        conn = psycopg2.connect(dbname=db_name, user=db_user, password=db_password, host=db_host, port=db_port)

    conn.autocommit = True
    return conn

def get_all_characters(category=None):
    conn = get_db()
    cursor = conn.cursor()

   
    if category:
        cursor.execute("SELECT id, name, actor, image_url, description FROM characters WHERE category = %s;", (category,))
    else:
        cursor.execute("SELECT id, name, actor, image_url FROM characters;")
    
    characters = cursor.fetchall()
    cursor.close()
    conn.close()

    return [{"id": c[0], "name": c[1], "actor": c[2], "image_url": c[3]} for c in characters]


def search_characters(query, category=None):
    conn = get_db()
    cursor = conn.cursor()
    partial_query = f"%{query}%"
    
    if category:
        cursor.execute("""
            SELECT id, name, actor, image_url, description
            FROM characters
            WHERE (name ILIKE %s OR actor ILIKE %s OR description ILIKE %s)
            AND category = %s
        """, (partial_query, partial_query, partial_query, category))
    else:
        cursor.execute("""
            SELECT id, name, actor, image_url, description
            FROM characters
            WHERE (name ILIKE %s OR actor ILIKE %s OR description ILIKE %s)
        """, (partial_query, partial_query, partial_query))
    
    characters = cursor.fetchall()
    cursor.close()
    conn.close()

    return [{"id": c[0], "name": c[1], "actor": c[2], "image_url": c[3]} for c in characters]


def get_character_by_id(character_id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, actor, image_url, description FROM characters WHERE id = %s", (character_id,))
    character = cursor.fetchone()  
    cursor.close()
    conn.close()

    if character:
        return {"id": character[0], "name": character[1], "actor": character[2], "image_url": character[3], "description" : character[4]}
    else:
        return None  

if __name__ == "__main__":

    print(get_all_characters())
    print(search_characters('rag'))  
    print(get_character_by_id(19))  

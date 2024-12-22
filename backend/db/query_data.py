import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def get_db():
    db_name = os.getenv("DB_NAME")
    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")
    
    conn = psycopg2.connect(dbname=db_name, user=db_user, password=db_password)
    conn.autocommit = True
    return conn

def get_all_characters():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, actor, image_url FROM characters;")
    characters = cursor.fetchall()
    cursor.close()
    conn.close()

    return [{"id": c[0], "name": c[1], "actor": c[2], "image_url": c[3]} for c in characters]



def search_characters(query):
    conn = get_db()
    cursor = conn.cursor()

   
    cursor.execute("""
        SELECT id, name, actor, image_url
        FROM characters
        WHERE search_vector @@ plainto_tsquery('english', %s)
    """, (query,))  

    characters = cursor.fetchall()
    cursor.close()
    conn.close()

    return [{"id": c[0], "name": c[1], "actor": c[2], "image_url": c[3]} for c in characters]

   

def get_character_by_id(character_id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, actor, image_url FROM characters WHERE id = %s", (character_id,))
    character = cursor.fetchone()  
    cursor.close()
    conn.close()

    if character:
        return {"id": character[0], "name": character[1], "actor": character[2], "image_url": character[3]}
    else:
        return None  

if __name__ == "__main__":

    print(get_all_characters())
    print(search_characters('rag'))  
    print(get_character_by_id(19))  

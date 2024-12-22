import psycopg2
from dotenv import load_dotenv
import os


def insert_characters(characters):
    load_dotenv()
    db_name = os.getenv("DB_NAME")
    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")
    
    try:
        conn = psycopg2.connect(dbname=db_name, user=db_user, password=db_password)
        cur = conn.cursor()
        
        for character in characters:
           
            # print(f"Inserting: {character['name']}, {character['actor']}, {character['image_url']}")
            
          
            cur.execute("""
                INSERT INTO characters (name, actor, image_url, search_vector)
                VALUES (%s, %s, %s, to_tsvector('english', %s || ' ' || %s))
            """, (character['name'], character['actor'], character['image_url'], character['name'], character['actor']))
            
            conn.commit()
        
        print("All characters inserted successfully!")
    except Exception as e:
        print(f"Error inserting characters: {e}")
    finally:
        cur.close()
        conn.close()

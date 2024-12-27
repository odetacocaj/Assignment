import psycopg2
from dotenv import load_dotenv
import os

def validate_and_prepare_character(character, category):

    name = character.get('name', 'N/A').strip() or 'N/A'
    actor = character.get('actor', 'N/A').strip() or 'N/A'
    image_url = character.get('image_url', 'N/A').strip() or 'N/A'
    description = character.get('description', 'N/A').strip() or 'N/A'


    if not image_url.startswith(('http://', 'https://')):
        image_url = 'https://www.pngitem.com/pimgs/m/579-5798505_user-placeholder-svg-hd-png-download.png'

    return {
        "name": name,
        "actor": actor,
        "image_url": image_url,
        "description": description,
        "category": category
    }

def insert_characters_and_norsemen(vikings, norsemen):
    load_dotenv()

   
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

    try:
        cur = conn.cursor()

        
        for character in vikings:
            prepared_character = validate_and_prepare_character(character, 'vikings')
            cur.execute("""
                INSERT INTO characters (name, actor, image_url, description, category, search_vector)
                VALUES (%s, %s, %s, %s, %s, to_tsvector('english', %s || ' ' || %s))
                ON CONFLICT (name, actor, category) DO UPDATE
                SET actor = EXCLUDED.actor,
                    image_url = EXCLUDED.image_url,
                    description = EXCLUDED.description,
                    search_vector = EXCLUDED.search_vector
            """, (
                prepared_character['name'], 
                prepared_character['actor'], 
                prepared_character['image_url'], 
                prepared_character['description'],  
                prepared_character['category'],  
                prepared_character['name'], 
                prepared_character['actor']
            ))
        
     
        for character in norsemen:
            prepared_character = validate_and_prepare_character(character, 'norsemen')
            cur.execute("""
                INSERT INTO characters (name, actor, image_url, description, category, search_vector)
                VALUES (%s, %s, %s, %s, %s, to_tsvector('english', %s || ' ' || %s))
                ON CONFLICT (name, actor, category) DO UPDATE
                SET image_url = EXCLUDED.image_url,
                    description = EXCLUDED.description,
                    search_vector = EXCLUDED.search_vector
            """, (
                prepared_character['name'], 
                prepared_character['actor'], 
                prepared_character['image_url'], 
                prepared_character['description'],  
                prepared_character['category'],  
                prepared_character['name'], 
                prepared_character['actor']
            ))

        conn.commit()
        print("All characters and norsemen inserted successfully!")

    except Exception as e:
        print(f"Error inserting characters: {e}")
    
    finally:
        cur.close()
        conn.close()

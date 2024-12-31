from .db_connection import get_db_connection  


def get_all_characters(category=None):
    conn = get_db_connection()
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
    conn = get_db_connection()
    cursor = conn.cursor()
    
    if category:
        cursor.execute("""
            SELECT id, name, actor, image_url, description
            FROM characters
            WHERE search_vector @@ plainto_tsquery(%s)
            AND category = %s
        """, (query, category))
    else:
        cursor.execute("""
            SELECT id, name, actor, image_url, description
            FROM characters
            WHERE search_vector @@ plainto_tsquery(%s)
        """, (query,))
    
    characters = cursor.fetchall()
    cursor.close()
    conn.close()

    return [{"id": c[0], "name": c[1], "actor": c[2], "image_url": c[3]} for c in characters]

def get_character_by_id(character_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, actor, image_url, description FROM characters WHERE id = %s", (character_id,))
    character = cursor.fetchone()
    cursor.close()
    conn.close()

    if character:
        return {"id": character[0], "name": character[1], "actor": character[2], "image_url": character[3], "description" : character[4]}
    else:
        return None

def edit_character(character_id, name=None, actor=None, image_url=None, description=None, category=None):
    """
    Edit an existing character's details in the database.
    """
    conn = get_db_connection()
    cursor = conn.cursor()

    fields = []
    values = []

    if name:
        fields.append("name = %s")
        values.append(name)
    if actor:
        fields.append("actor = %s")
        values.append(actor)
    if image_url:
        fields.append("image_url = %s")
        values.append(image_url)
    if description:
        fields.append("description = %s")
        values.append(description)
    if category:
        fields.append("category = %s")
        values.append(category)
    
    if fields:
        values.append(character_id)
        query = f"UPDATE characters SET {', '.join(fields)} WHERE id = %s;"
        cursor.execute(query, values)
        conn.commit()
    
    cursor.close()
    conn.close()

    return {"message": "Character updated successfully"}


if __name__ == "__main__":
    print(get_all_characters())
    print(search_characters('rag'))
    print(get_character_by_id(19))

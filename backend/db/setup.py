import psycopg2
from psycopg2 import sql
from dotenv import load_dotenv
import os
from urllib.parse import urlparse

def create_tables():
    load_dotenv()

    db_url = os.getenv("DATABASE_URL")

    if db_url:
        # Parse the DATABASE_URL
        parsed_url = urlparse(db_url)

        # Extract db_name, user, password, host, and port from the connection string
        db_name = parsed_url.path[1:]  # Remove leading '/' from the path
        db_user = parsed_url.username
        db_password = parsed_url.password
        db_host = parsed_url.hostname
        db_port = parsed_url.port

        # Construct the connection string
        conn_str = f"dbname={db_name} user={db_user} password={db_password} host={db_host} port={db_port}"

    else:
        # Fallback to individual environment variables
        db_name = os.getenv("DB_NAME")
        db_user = os.getenv("DB_USER")
        db_password = os.getenv("DB_PASSWORD")
        db_host = os.getenv("DB_HOST", "localhost")
        db_port = os.getenv("DB_PORT", "5432")

        # Construct the connection string for local development
        conn_str = f"dbname=postgres user={db_user} password={db_password} host={db_host} port={db_port}"

    # Connect to the database
    conn = psycopg2.connect(conn_str)
    conn.autocommit = True
    cur = conn.cursor()

    # Check if the database exists, create it if it doesn't
    cur.execute(sql.SQL("SELECT 1 FROM pg_catalog.pg_database WHERE datname = %s"), [db_name])
    if not cur.fetchone():
        cur.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(db_name)))

    # Close the initial connection
    conn.close()

    # Connect to the newly created or existing database
    conn = psycopg2.connect(dbname=db_name, user=db_user, password=db_password, host=db_host, port=db_port)
    cur = conn.cursor()

    # Create the characters table if it doesn't exist
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

    # Create the index on the search_vector column
    cur.execute("""
    CREATE INDEX IF NOT EXISTS search_idx ON characters USING GIN (search_vector);
    """)

    # Commit the changes and close the connection
    conn.commit()
    cur.close()
    conn.close()

if __name__ == "__main__":
    create_tables()

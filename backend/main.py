from flask import Flask
from scraper.vikings_scraper import scrape_vikings_characters
from db.insert_data import insert_characters
from db.setup import create_tables
from routes import main  


app = Flask(__name__)


app.register_blueprint(main)

def setup_database():
    
    try:
        print("Setting up database...")
        create_tables()  

      
        print("Scraping Vikings characters...")
        vikings_characters = scrape_vikings_characters()

    
        print("Inserting Vikings characters into the database...")
        insert_characters(vikings_characters)

        print("Data scraping and insertion complete!")
    except Exception as e:
        print(f"Error setting up database: {e}")

if __name__ == "__main__":
    # Uncomment the line below to scrape and insert data each time the app starts
    # setup_database()

   
    app.run(debug=True)  

from flask import Flask
from scraper.vikings_scraper import scrape_vikings_characters
from scraper.norsemen_scraper import scrape_norsemen_characters  
from db.insert_data import insert_characters_and_norsemen  
from db.setup import create_tables
from routes import main  
import schedule
import threading
import time

app = Flask(__name__)
app.register_blueprint(main)

def setup_database():
    try:
        print("Setting up database...")
        create_tables()  
        
        print("Scraping Vikings characters...")
        vikings_characters = scrape_vikings_characters()

        print("Scraping Norsemen characters...")
        norsemen_characters = scrape_norsemen_characters()  
        
        print("Inserting Vikings and Norsemen characters into the database...")
        insert_characters_and_norsemen(vikings_characters, norsemen_characters)  
        
        print("Data scraping and insertion complete!")
        
    except Exception as e:
        print(f"Error setting up database: {e}")

def scheduled_scraping():
    try:
        vikings_characters = scrape_vikings_characters()
        norsemen_characters = scrape_norsemen_characters()
        insert_characters_and_norsemen(vikings_characters, norsemen_characters)
        print("Scheduled scraping completed successfully.")
    except Exception as e:
        print(f"Error during scheduled scraping: {e}")

def start_scheduler():
    schedule.every(24).hours.do(scheduled_scraping)

    def run_schedule():
        while True:
            schedule.run_pending()
            time.sleep(1)  
    
    threading.Thread(target=run_schedule, daemon=True).start()

if __name__ == "__main__":
    # Uncomment the following line if you want to scrape and insert data on app startup
    #setup_database()
    
    start_scheduler()

    app.run(debug=True)

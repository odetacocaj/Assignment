import requests
from bs4 import BeautifulSoup

def scrape_vikings_characters():
    url = "https://www.history.com/shows/vikings/cast"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    characters = []
    
    character_divs = soup.find_all('div', class_='details') 

    for character_div in character_divs:
        name = character_div.find('strong').text.strip() if character_div.find('strong') else 'N/A'
        actor = character_div.find('small').text.strip().replace('Played by ', '') if character_div.find('small') else 'N/A'
        img_container = character_div.find_previous('div', class_='img-container')
        image_url = img_container.find('img')['src'] if img_container and img_container.find('img') else None

        characters.append({
            'name': name,
            'actor': actor,
            'image_url': image_url
        })
    
    return characters



if __name__ == "__main__":
    characters = scrape_vikings_characters()
    # for character in characters:
    #     print(character)

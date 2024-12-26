import requests
from bs4 import BeautifulSoup

def scrape_norsemen_characters():
    url = "https://m.imdb.com/title/tt5905354/"
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/114.0.0.0 Safari/537.36"
        )
    }
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"Failed to fetch the page. Status code: {response.status_code}")
        return []

    soup = BeautifulSoup(response.content, 'html.parser')
    cast_items = soup.find_all("div", {"data-testid": "title-cast-item"})

    characters = []

    for item in cast_items:
        actor_name = item.find("a", {"data-testid": "title-cast-item__actor"})
        actor_name = actor_name.text.strip() if actor_name else "N/A"

        character_name = item.find("a", {"data-testid": "cast-item-characters-link"})
        character_name = character_name.text.strip() if character_name else "N/A"

        episode_details = item.find("button", {"data-testid": "title-cast-item__eps-toggle__large"})
        episode_details = episode_details.text.strip() if episode_details else "N/A"

        image_tag = item.find("img", class_="ipc-image")
        if image_tag:
            srcset = image_tag.get("srcset", "")
            image_url = srcset.split(",")[0] if srcset else ""
        else:
            image_url = ""  

        characters.append({
            "actor": actor_name,
            "name": character_name,
            "description": episode_details,
            "image_url": image_url,
        })

    return characters

if __name__ == "__main__":
    characters = scrape_norsemen_characters()
    # for character in characters:
    #     print(character)

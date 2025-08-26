import random 
import json

def main_film():
    with open('film.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    random_film = random.choice(data["Films"])


main_film()

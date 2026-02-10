import random
import json


def get_random_film():
    # Gibt einen zufälligen Film aus film.json zurück.
    with open('film.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    return random.choice(data["titles"])

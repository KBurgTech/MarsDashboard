import random

import requests

ANIMALS = [
    "Dog",
    "Cat",
    "Penguin",
    "Lama",
    "Bird"
]

ACCESS_KEY = "HtU5b2UKmalDrAg7iKTFwtrK9iBmKDa5PXEwDQSbFyk"
SECRET_KEY = "wyQU4_P51r7lF9sS_ywvU5OTu7mbzuF-YqcoE1fad08"


def get_animal_picture_link(animal):
    response = requests.get(
        f"https://api.unsplash.com/search/photos?page=1&query={animal}&client_id={ACCESS_KEY}&per_page=10")
    images = response.json()['results']
    return images[random.randint(0, 9)]['urls']['full']  # Lets get a radom picture every time

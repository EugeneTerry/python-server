

ANIMALS = [
    {
        "id": 1,
        "name": "Snickers",
        "breed": "Mutt",
        "locationId": 1,
        "customerId": 4
    },
    {
        "id": 2,
        "name": "Gypsy",
        "breed": "Poodle",
        "locationId": 1,
        "customerId": 2
    },
    {
        "id": 3,
        "name": "Blue",
        "breed": "Lab",
        "locationId": 2,
        "customerId": 1
    },
    {
      "id": 4,
      "name": "Butch Mane IIII",
      "breed": "Great Dane",
      "locationId": 1,
      "customerId": 4
    },
    {
      "id": 6,
      "name": "Markey Mark III",
      "breed": "Pug",
      "locationId": 1,
      "customerId": 3
    },
    {
      "name": "Michael Day",
      "breed": "Lab",
      "locationId": 3,
      "customerId": 2,
      "id": 5
    }
]


def get_all_animals():
    return ANIMALS

# Function with a single parameter
def get_single_animal(id): # Variable to hold the found animal, if it exists
    requested_animal = None
    for animal in ANIMALS:
        if animal["id"] == id: # Dictionaries in Python use [] notation to find a key, not dot notation
            requested_animal = animal

    return requested_animal



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

def create_animal(animal):
    # Get the id value of the last animal in the list
    max_id = ANIMALS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the animal dictionary
    animal["id"] = new_id

    # Add the animal dictionary to the list
    ANIMALS.append(animal)

    # Return the dictionary with `id` property added
    return animal

def delete_animal(id):
    # Initial -1 value for animal index, in case one isn't found
    animal_index = -1

    # Iterate the ANIMALS list, but use enumerate() so that you
    # can access the index value of each item
    for index, animal in enumerate(ANIMALS):
        if animal["id"] == id:
            # Found the animal. Store the current index.
            animal_index = index

    # If the animal was found, use pop(int) to remove it from list
    if animal_index >= 0:
        ANIMALS.pop(animal_index)


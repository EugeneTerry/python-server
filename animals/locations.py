LOCATIONS = [
  {
    "id": 1,
    "name": "Nashville North",
    "address": "8422 Johnson Pike"
  },
  {
    "id": 2,
    "name": "Nashville South",
    "address": "209 Emory Drive"
  },
  {
    "name": "Nashville West",
    "address": "2323 Brooks Way",
    "id": 3
  },
  {
    "name": "Nashville East",
    "address": "7889 RearWheel Drive",
    "id": 4
  }
]

def get_all_locations():
    return LOCATIONS

def get_single_location(id): # Variable to hold the found animal, if it exists
    requested_location = None
    for location in LOCATIONS:
        if location["id"] == id: # Dictionaries in Python use [] notation to find a key, not dot notation
            requested_location = location

    return requested_location
    
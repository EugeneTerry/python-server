EMPLOYEES = [
  {
    "id": 1,
    "name": "Ronold McDonald",
    "locationId": 1
  },
  {
    "id": 2,
    "name": "Emma Beaton",
    "locationId": 1
  },
  {
    "id": 3,
    "name": "Conell Sanders",
    "locationId": 2
  },
  {
    "id": 4,
    "name": "Wendy Frost",
    "locationId": 2
  },
  {
    "name": "Terry, Eugene",
    "locationId": 2,
    "id": 5
  },
  {
    "name": "Faith Star",
    "locationId": 1,
    "id": 6
  },
  {
    "name": "John",
    "locationId": 3,
    "id": 7
  },
  {
    "name": "Diego",
    "locationId": 3,
    "id": 8
  }
]

def get_all_employees():
    return EMPLOYEES

def get_single_employee(id):
  requested_employee = None
  for employee in EMPLOYEES:
    if employee["id"] == id:
      requested_employee = employee

  return requested_employee
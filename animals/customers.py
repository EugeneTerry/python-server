CUSTOMERS = [
  {
    "id": 1,
    "name": "Hannah Hall",
    "address": "7002 Chestnut Ct",
    "email": "HannahHall@xmail.com"
  },
  {
    "id": 2,
    "name": "Taylor Slow",
    "address": "77A Almond Cv",
    "email": "TaylorSlow@kmail.com"
  },
  {
    "id": 3,
    "name": "Bruno Pluto",
    "address": "4 Cashew Dr",
    "email": "BPluto@mars.com"
  },
  {
    "id": 4,
    "name": "Tom Jump",
    "address": "2322 Walnut St",
    "email": "JumpJump@me.net"
  }
]

def get_all_customers():
    return CUSTOMERS


def get_single_customer(id):
  requested_customer = None
  for customer in CUSTOMERS:
    if customer["id"] == id:
      requested_customer = customer

  return requested_customer

def create_customer(customer):
  max_id = CUSTOMERS[-1]["id"]
  new_id = max_id + 1
  customer["id"] = new_id
  CUSTOMERS.append(customer)
  return customer

def delete_customer(id):
    customer_index = -1
    for index, customer in enumerate(CUSTOMERS):
      if customer["id"] == id:
        customer_index = index
    if customer_index >= 0:
      CUSTOMERS.pop(customer_index)

def update_customer(id, new_customer):
  for index, customer in enumerate(CUSTOMERS):
    if customer["id"] == id:
      CUSTOMERS[index] = new_customer
      break
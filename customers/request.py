import sqlite3
import json

from models import CUSTOMER

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

# OLD GET ALL METHOD
# def get_all_customers():
#     return CUSTOMERS

def get_all_customers():
  with sqlite3.connect("./kennel.db") as conn:
    conn.row_factory = sqlite3.Row
    db_cursor = conn.cursor()
    
    db_cursor.execute(""" 
    SELECT
      a.id,
      a.name,
      a.address,
      a.email,
      a.password
    FROM customer a
      """)

    customers = []

    dataset = db_cursor.fetchall()

    for row in dataset:
      customer = CUSTOMER(row['id'], row['name'], row['address'],
                          row['email'], row['password'])
      customers.append(customer.__dict__)
  
  return json.dumps(customers)    


# OLD GET SINGLE METHOD
# def get_single_customer(id):
#   requested_customer = None
#   for customer in CUSTOMERS:
#     if customer["id"] == id:
#       requested_customer = customer

#   return requested_customer

def get_single_customer(id):
  with sqlite3.connect("./kennel.db") as conn:
    conn.row_factory = sqlite3.Row
    db_cursor = conn.cursor()

    db_cursor.execute("""
    SELECT
      a.id,
      a.name,
      a.address,
      a.email,
      a.password
    FROM customer a
    WHERE a.id = ?
    """, ( id, ))

    data = db_cursor.fetchall()

    customer = CUSTOMER(data['id'], data['name'], data['address'],
                        data['email'], data['password'])
    
    return json.dumps(customer.__dict__)

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
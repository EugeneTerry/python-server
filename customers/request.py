import sqlite3
import json
from urllib.parse import unquote_plus

from models import CUSTOMER

CUSTOMERS = [
 
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
      c.id,
      c.name,
      c.address,
      c.email,
      c.password
    FROM customer c
    WHERE c.id = ?
    """, ( id, ))

    data = db_cursor.fetchone()

    customer = CUSTOMER(data['id'], data['name'], data['address'],
                        data['email'], data['password'])
    
    return json.dumps(customer.__dict__)

def get_customers_by_email(email):

    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        select
            c.id,
            c.name,
            c.address,
            c.email,
            c.password
        from Customer c
        WHERE c.email = ?
        """, ( email, ))

        customers = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            customer = CUSTOMER(row['id'], row['name'], row['address'], row['email'] , row['password'])
            customers.append(customer.__dict__)

    return json.dumps(customers)


def get_customers_by_name(name):

    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        response = []
        value = unquote_plus(name)
        # Write the SQL query to get the information you want
        db_cursor.execute("""
        select
            c.id,
            c.name,
            c.address,
            c.email,
            c.password
        from Customer c
        WHERE c.name = ?;
        """, ( value, ))

        customers = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            response.append(CUSTOMER(*row).__dict__)


    return response

def create_customer(customer):
  max_id = CUSTOMERS[-1]["id"]
  new_id = max_id + 1
  customer["id"] = new_id
  CUSTOMERS.append(customer)
  return customer

def delete_customer(id):
    with sqlite3.connect("./kennel.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM customer
        WHERE id = ?
        """, (id, ))

# def delete_customer(id):
#     customer_index = -1
#     for index, customer in enumerate(CUSTOMERS):
#       if customer["id"] == id:
#         customer_index = index
#     if customer_index >= 0:
#       CUSTOMERS.pop(customer_index)

#OLD UPDATE METHOD
# def update_customer(id, new_customer):
#   for index, customer in enumerate(CUSTOMERS):
#     if customer["id"] == id:
#       CUSTOMERS[index] = new_customer
#       break

# NEW UPDATE METHOD
def update_customer(id, new_customer):
  with sqlite3.connect("./kennel.db") as conn:
    db_cursor = conn.cursor()
    
    db_cursor.execute("""
    UPDATE customer
      SET
        name = ?,
        address = ?,
        email = ?,
        password = ?
    WHERE id = ?
    """, (new_customer['name'], new_customer['address'],
          new_customer['email'], new_customer['password'], id,))
    
    rows_affected = db_cursor.rowcount
  
  if rows_affected == 0:
    return False
  else:
    return True
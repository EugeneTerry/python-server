import random
QUOTES = [
  'Im your father',
  'forget about it',
  'you had me at hello'

]

def get_all_quotes():
    return QUOTES

def get_random_quotes():
    return random.choice(QUOTES)
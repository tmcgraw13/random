import random
from database_connection import save_random_integer as save

def random_int_generator():
    num = random.randint(0, 100)
    save(num) #saves to the database
    return num
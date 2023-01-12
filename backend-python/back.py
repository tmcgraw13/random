import random
from database.db_save import save_random_integer as rand_save

def random_int_generator():
    num = random.randint(0, 100)
    rand_save(num) #saves to the database
    return num
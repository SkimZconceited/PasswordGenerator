import random
import string

def get_random_pass(length):
    letters = string.ascii_letters
    result_str = '' .join(random.choice(letters) for i in range(length)
    
    print(result_str)

get_random_pass(8)
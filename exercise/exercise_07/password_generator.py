import string
import random

def generate_password(number):
    return "".join(random.choice(string.ascii_lowercase) for _ in range(number))

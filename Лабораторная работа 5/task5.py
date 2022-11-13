import string
from random import sample

def get_random_password() -> str:
    alphabet = string.ascii_uppercase + string.ascii_lowercase + string.digits
    n = 8
    return ''.join(sample(alphabet,n))

print(get_random_password())

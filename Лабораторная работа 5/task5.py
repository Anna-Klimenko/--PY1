import string
from random import sample

def get_random_password(n=8) -> str:
    alphabet = string.ascii_uppercase + string.ascii_lowercase + string.digits
    return ''.join(sample(alphabet,n))

print(get_random_password())

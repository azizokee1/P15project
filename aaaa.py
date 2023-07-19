import random
from uuid import uuid4

def genarte_code():
    code=random.randint(1000,9999)
    return str(code)
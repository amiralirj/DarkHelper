import random, string
def Get_hash():
    x = ''.join(random.choices(string.ascii_letters + string.digits, k=26))
    return x
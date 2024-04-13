import random as rn
import string

def random_password():
    '''returns random 8 symbol long password as str'''
    lista = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(rn.choice(lista) for _ in range(8))
    return password

print(f"your randomly generated password is {random_password()}")
import re
import math

key_space = 'abcdefghijklmnopqrstuvwxyz'

def factorial(x):
    product = 1
    for i in range(1,x+1):
        product = product * i
    return product

def convert_to_lower(text):
    return text.lower()

def get_text_index(text):
    list_index = [key_space.index(i) for i in convert_to_lower(text) if i in key_space]
    return list_index

def encryption_sequence(text):
    list_sequence = [(math.pow(2, 2*i)*factorial(2*i+2))/(factorial(2*i)) for i in range(len(get_text_index(text)))]
    return list_sequence

def add_prime(text):
    return [i + 2019 for i in encryption_sequence(text)]

def solve_congruence(text):
    nested_list_rem = []
    i = 0
    while i < len(add_prime(text)):
        rem = [x for x in range(26) if (add_prime(text)[i]*x)%26 == get_text_index(text)[i]]
        nested_list_rem.append(rem)
        i += 1
    return nested_list_rem
    # list_rem = []
    # for i in nested_list_rem:
    #     list_rem.append(i[0])
    # return list_rem

def convert_to_text(text):
    return [key_space[i] for i in solve_congruence(text)]

def add_space(text):
    pattern = re.finditer(r'\s', text)
    spaceList = [ x.start() for x in pattern]
    list_encoded = list(convert_to_text(text))
    for i in spaceList:
        list_encoded.insert(i, ' ')
    return ''.join(list_encoded)

text = 'dahni lgzyhii and mawwacqw'
print(solve_congruence(text))
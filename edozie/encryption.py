import re
import math

key_space = 'abcdefghijklmnopqrstuvwxyz'

def factorial(x):
    product =1
    for i in range(1,x+1):
        product= product * i
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

def multiply_terms(text):
    list_multiply = [get_text_index(text)[i] * add_prime(text)[i] for i in range(len(get_text_index(text)))]
    return list_multiply

def mod26(text):
    list_terms = [i%26 for i in multiply_terms(text)]
    return list_terms

def convert_to_text(text):
    return [key_space[int(i)] for i in mod26(text)]

def add_space(text):
    pattern = re.finditer(r'\s', text)
    spaceList = [ x.start() for x in pattern]
    listEncoded = list(convert_to_text(text))
    for i in spaceList:
        listEncoded.insert(i, ' ')
    return ''.join(listEncoded)

text = 'hello bitches and bastards'

print(add_space(text))
print(add_prime(text))
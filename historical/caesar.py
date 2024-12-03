import re

def caesar_encrypt(plaintext, key):
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    pattern = re.finditer(r'\s', plaintext)
    space_list = [x.start() for x in pattern]
    plaintext = plaintext.lower()
    plaintext_index = [alphabets.find(i) for i in plaintext if i in alphabets]
    add_key = [(i + key)%len(alphabets) for i in plaintext_index]
    list_ciphertext = [alphabets[i] for i in add_key]
    for i in space_list:
        list_ciphertext.insert(i, ' ')
    ciphertext = ''.join(list_ciphertext)
    return ciphertext


def caesar_decrypt(ciphertext, key):
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    pattern = re.finditer(r'\s', ciphertext)
    space_list = [x.start() for x in pattern]
    ciphertext_index = [alphabets.find(i) for i in ciphertext if i in alphabets]
    subtract_key = [(i - key + len(alphabets))%len(alphabets) for i in ciphertext_index]
    decrypted_list = [alphabets[i] for i in subtract_key]
    for i in space_list:
        decrypted_list.insert(i, ' ')
    plaintext = ''.join(decrypted_list)
    return plaintext 


def caesar_brute_force(ciphertext):
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    for key in range(len(alphabets)):
        print(caesar_decrypt(ciphertext, key))
        print()

    


#Encryption
def caesar_ascii_encrypt(plaintext, key):
    plaintext_index = [ord(i) for i in plaintext]
    add_key = [(i + key)%128 for i in plaintext_index]
    cipher_list = [chr(i) for i in add_key]
    ciphertext = ''.join(cipher_list)
    return ciphertext

#Decryption
def caesar_ascii_decrypt(ciphertext, key):
    cipher_index = [ord(i) for i in ciphertext]
    subtract_key = [(i-key)%128 for i in cipher_index]
    plain_list = [chr(i) for i in subtract_key]
    plaintext = ''.join(plain_list)
    return plaintext 
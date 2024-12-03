import re
import string

def simple_sub_encrypt(plaintext):
    alphabets = string.ascii_lowercase
    key_list = ['d', 'm', 'h', 'w', 'z', 'r', 'p', 'x', 's', 'i', 'v', 'q', 'k', 'a', 'e', 'o',
    'n', 'j', 'l', 't', 'c', 'y', 'g', 'u', 'b', 'f']
    key = ''.join(key_list)
    plaintext = plaintext.lower()
    pattern = re.finditer(r'\s', plaintext)
    space_list = [x.start() for x in pattern]
    cipher_index = [alphabets.find(i) for i in plaintext if i in alphabets]
    cipher = [key[i] for i in cipher_index]
    for x in space_list:
        cipher.insert(x, ' ')
    ciphertext = ''.join(cipher)
    return ciphertext
print("Encrypted text is:", simple_sub_encrypt('abc def ghi'))

def simple_subs_decrypt(ciphertext):
    alphabets = string.ascii_lowercase
    key_list = ['d', 'm', 'h', 'w', 'z', 'r', 'p', 'x', 's', 'i', 'v', 'q', 'k', 'a', 'e', 'o',
    'n', 'j', 'l', 't', 'c', 'y', 'g', 'u', 'b', 'f']
    key = ''.join(key_list)
    ciphertext = ciphertext.lower()
    pattern = re.finditer(r'\s', ciphertext)
    space_list = [x.start() for x in pattern]
    plain_index = [key.find(i) for i in ciphertext if i in alphabets]
    plain = [alphabets[i] for i in plain_index]
    for x in space_list:
        plain.insert(x, ' ')
    plaintext = ''.join(plain)
    return plaintext

print('Decrypted text is:', simple_subs_decrypt('dmh wzr pxs'))
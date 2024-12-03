import re

def vigenere_encrypt(plaintext, key):
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    pattern = re.finditer(r'\s', plaintext)
    space_list = [s.start() for s in pattern]
    plaintext = plaintext.replace(' ', '')
    comb_key = key * int(len(plaintext)//len(key)) + key[:len(plaintext)%len(key)]
    list_plaintext_index = [alphabets.find(i) for i in plaintext]
    list_comb_key_index = [alphabets.find(j) for j in comb_key]
    add_lists = [(list_plaintext_index[i] + list_comb_key_index[i])%len(alphabets) for i in range(len(list_comb_key_index))]
    letter_list = [alphabets[i] for i in add_lists]
    for i in space_list:
        letter_list.insert(i, ' ')
    cipher_text = ''.join(letter_list)
    return cipher_text

def vigenere_decrypt(ciphertext, key):
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    pattern = re.finditer(r'\s', ciphertext)
    space_list = [s.start() for s in pattern]
    ciphertext = ciphertext.replace(' ', '')
    comb_key = key * int(len(ciphertext)//len(key)) + key[:len(ciphertext)%len(key)]
    list_ciphertext_index = [alphabets.find(i) for i in ciphertext]
    list_comb_key_index = [alphabets.find(i) for i in comb_key]
    subtract_lists = [(list_ciphertext_index[i] - list_comb_key_index[i]+26)%26 for i in range(len(list_comb_key_index))]
    letter_lists = [alphabets[i] for i in subtract_lists]
    for i in space_list:
        letter_lists.insert(i, ' ')
    plaintext = ''.join(letter_lists)
    return plaintext

def vigenere_bruteforce(ciphertext):
    key_list = ['compute', 'suspect', 'matress', 'follows', 'attacks', 'bottles', 'damages', 'finding']
    for key in key_list:
        print(vigenere_decrypt(ciphertext, key))
        print()


plain = "Obi is a boy"
key = "worgs"

print(vigenere_encrypt(plain, key))
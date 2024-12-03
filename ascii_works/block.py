'''
The chr() function takes a base ten integer and returns its corresponding ascii string

The ord() function is the reverse of the chr() function. 

The ord function takes an ascii string and returns its base ten ascii equivalent
'''
from key import key
from shuffled_key import shuffled_key

def create_blocks(plaintext, bit_size):
    list_plaintext_demo = [bin(ord(x)).replace('b', '') for x in plaintext]
    list_plaintext_ascii = [(bit_size-len(i))*'0'+i for i in list_plaintext_demo]
    joint_plaintext = ''.join(list_plaintext_ascii)
    block_list = []
    for i in range(0, len(joint_plaintext), bit_size):
        block_list.append([joint_plaintext[i+j]for j in range(bit_size)])
    blocks = [''.join(x) for x in block_list]
    return blocks
    

def binary_blocks_encryption(plaintext, bit_size, key=key, shuffled_key=shuffled_key):
    #key = ['00', '01', '10', '11']
    #shuffled_key = ['01', '10', '11', '00']
    cipher_list = []
    for i in create_blocks(plaintext, bit_size):
        key_i_index = key.index(i)
        cipher_list.append(shuffled_key[key_i_index])
    return ''.join(cipher_list)


def block_decryption(ciphertext, bit_size, key=key, shuffled_key=shuffled_key):
    cipher_block = []
    for i in range(0, len(ciphertext), bit_size):
        cipher_block.append(ciphertext[i:i+bit_size])
    plain_list = []
    for i in cipher_block:
        shuffled_key_i_index = shuffled_key.index(i)
        plain_list.append(key[shuffled_key_i_index])
    # plaintext_block_list = [plain_list[i:i+2] for i in range(0, len(plain_list), 2)]
    # plaintext_list = [''.join(i) for i in plaintext_block_list]
    base_ten_list = [int(i, 2) for i in plain_list]
    plaintext = ''
    for i in base_ten_list:
        plaintext += chr(i)
    return plaintext


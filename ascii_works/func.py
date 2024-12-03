import random
from block import create_blocks, binary_blocks_encryption, block_decryption


def generate_key(bit_size):
    all_nums = [bin(i).replace('b', '') for i in range(2**bit_size)]
    key = []
    for i in all_nums:
        if len(i) > bit_size:
            i = list(i)
            i.pop(0)
            key.append(''.join(i))
        elif len(i) < bit_size:
            i = (bit_size-len(i))*'0' + i
            key.append(i)
        else:
            key.append(i)
    return key

bit = 2

with open('key.py', 'w') as key_file:
    key_file.write(f'key_{bit}_bit = {generate_key(bit)}')
 
shuffled_key = generate_key(bit)
random.shuffle(shuffled_key)

with open('shuffled_key.py', 'w') as key_file:
    key_file.write(f'shuffled_key = {shuffled_key}')
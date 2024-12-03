import random

global shuffled_key
shuffled_key = ['01110101', '11100001', '01110010', '11101001', '10011011', '11011011',
 '00101001', '10010000', '00100001','00000011', '11100101', '00111010', '00110101','11001001', 
 '10111100', '01000100', '01110100', '10000111', '10001011', '00111011','00110010', '01100100', 
 '00001001', '00100110', '11111101', '10001101', '01010101', '10110100','01010010', '01010000', '01110001', 
 '10010111', '00110001', '11011010', '00101011', '11010110', '11001000', '10100111', '00010001', '01000000',
 '01100000','00001110', '11101111', '00000000', '11101101','11110011', '10001111', '11000111','11000100', '11110100', 
 '10010110', '10111010','11111111', '11001011', '01101110', '01111000', '01110011', '11010011', '00001101', '11000001',
 '01000110', '11101000', '11010101', '01001001', '10011001', '01000001', '11001101', '11000110', '00100100', '10011110', 
 '00000110', '00010010', '00100010', '01100011', '11001010', '00100101', '01011111', '11101011', '11101100', '11110110',
 '00110000', '00101000', '11000000', '00111000', '11011101', '11010000', '01000011', '10101111', '00101010', '01000010', 
 '00111001', '11110111', '00000100', '11011000', '00001000', '10000101', '10100000', '11111100', '10101101', '11000101',
 '01001111', '01101101', '00011111', '01100101', '10101001', '00000001', '11101010', '11110001', '01110000', '01100111', 
 '01110111', '00011000', '10001000', '00100111', '00011100', '10011010', '10001100', '10001001', '11111001', '10010001',
 '11000010', '00000111', '00001010', '00101100', '01000101', '01111010', '11010001', '01001100', '10111011', '00011011', 
 '10111111', '01110110', '10100010', '01011001', '10101010', '00110111', '11100000', '01010100', '01111001', '11010111',
 '01101000', '11011111', '10100001', '10101100', '01101010', '11001111', '10010011', '11000011', '10110010', '01111101', 
 '00001111', '11111110', '10110111', '11101110', '01011000', '11011100', '10000110', '11111011', '01010011', '00010111',
 '00011110', '01001010', '00010100', '10010101', '10100100', '11110000', '01111100', '10010010', '00001100', '01100010', 
 '11001110', '01000111', '01101100', '01100110', '00010000', '11111000', '10101011', '10110000', '11100011', '10101110',
 '10110001', '11001100', '00110100', '01010111', '01111110', '11100010', '01100001', '00111101', '10111110', '11100111', 
 '00000010', '00110110', '10101000', '10000010', '00011001', '11111010', '00011010', '01111011', '10100101', '11011110',
 '10111000', '11110010', '01111111', '01011010', '00100000', '00011101', '10011111', '10110110', '01011101', '00001011', 
 '01001000', '00010101', '01011100', '00010011', '00101101', '01011110', '10011000', '10100011', '01101001', '11100100',
 '00111110', '01001101', '01010001', '10001110', '01001011', '10000011', '10111001', '10000001', '00100011', '10000000', 
 '00101110', '10110011', '11100110', '00101111', '10001010', '10111101', '01010110', '10010100', '00000101', '11011001',
 '11110101', '10000100', '10011101', '01001110', '00010110', '01011011', '10011100', '00111111', '01101011', '01101111', 
 '00111100', '10110101', '11010010', '00110011', '11010100', '10100110']


def generate_binary_bits(bit_size):
    nums = [i for i in range(2**bit_size)]
    binary_nums = [bin(i).replace('b', '') for i in nums]
    binary_nums_new = []
    for i in binary_nums:
        if len(i) < bit_size:
            i = (bit_size-len(i))*'0' + i
        elif len(i) > bit_size:
            i = i[1:]
        binary_nums_new.append(i)
    return binary_nums_new

global key
key = generate_binary_bits(bit_size=8)

def encrypt_keys(item, bit_size):
    count = 0
    item_list = []
    while count <= len(item) - 1:
        item_list.append(item[count:count+bit_size])
        count += bit_size
    encoded_list = []
    for i in item_list:
        if i in shuffled_key:
            i_index = key.index(i)
            encoded_list.append(shuffled_key[i_index])
    return ''.join(encoded_list)

def decrypt_keys(item, bit_size):
    count = 0
    item_list = []
    while count <= len(item) - 1:
        item_list.append(item[count:count+bit_size])
        count += bit_size
    decoded_list = []
    for i in item_list:
        if i in key:
            i_index = shuffled_key.index(i)
            decoded_list.append(key[i_index])
    return ''.join(decoded_list)

def XoR(x, y):
    list_xor = [(int(x[i]) + int(y[i]))%2 for i in range(len(x))]
    str_list_xor = [str(i) for i in list_xor]
    return ''.join(str_list_xor)

def step_one(ciphertext, bit_size):
    '''
    In this step, we divide the ciphertext into two equal parts.
    We call the first part L1 and the second part R1
    '''
    L1 = ciphertext[:int(len(ciphertext)/2)]
    R1 = ciphertext[int(len(ciphertext)/2):]
    return [L1, R1]

def step_two(ciphertext, bit_size):
    '''
    In this step, we put R0=L1, then we wncode R0 to get E.
    The encryption function is the `reverse_string` function we defined above
    '''
    R0 = step_one(ciphertext, bit_size)[0]
    E = encrypt_keys(R0, bit_size)
    return [R0, E]

def step_three(ciphertext, bit_size):
    '''
    In this step, we perform L0=R1 XoR E using the `XoR` function defined above.
    Once we obtain L0 and R0, we join them
    '''
    R0 = step_one(ciphertext, bit_size)[0]
    E = encrypt_keys(R0, bit_size)
    L1 = step_one(ciphertext, bit_size)[0]
    R1 = step_one(ciphertext, bit_size)[1]
    L0 = XoR(R1, E)
    return [L0, R0]

def step_four(ciphertext, bit_size):
    '''
    In this step, we join L0 and R0 obtained in step three
    '''
    return ''.join(step_three(ciphertext, bit_size))

def binary_to_plaintext(ciphertext, bit_size):
    '''
    This is the part where we convert the binary numbers to plaintext letters.
    This is the final part of te decryption process
    '''
    count = 0
    plaintext_list = []
    while count <= len(ciphertext) -1:
        plaintext_list.append(step_four(ciphertext, bit_size)[count:bit_size+count])
        count += bit_size
    plaintext_base10 = [int(i, 2) for i in plaintext_list]
    plaintext = [chr(i) for i in plaintext_base10]
    return ''.join(plaintext)
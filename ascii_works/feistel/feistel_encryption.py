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

def XoR(x, y):
    list_xor = [(int(x[i]) + int(y[i]))%2 for i in range(len(x))]
    str_list_xor = [str(i) for i in list_xor]
    return ''.join(str_list_xor)   


def plaintext_to_binary(plaintext, bit_size):
    '''
    The `plaintext_to_binary` function converts the plaintext
    from the original text to its binary equivalent
    '''
    plaintext_decimal = [ord(i) for i in plaintext]
    plaintext_binary = [bin(int(x)).replace('b', '')  for x in plaintext_decimal]
    plaintext_binary_8bit = []
    for i in plaintext_binary:
        if len(i) < bit_size:
            i = (bit_size-len(i))*'0' + i
        plaintext_binary_8bit.append(i)
    joint_binary_plaintext = ''.join(plaintext_binary_8bit)
    return joint_binary_plaintext

def step_one(plaintext, bit_size):
    '''
    This is the first step of the feistel encryption.
    In this step, we divide the binary equivalent of the plaintext into two parts.
    We call the first part L0 and other part R0
    '''
    L0 = plaintext_to_binary(plaintext, bit_size)[0:int(len(plaintext_to_binary(plaintext, bit_size))/2)]
    R0 = plaintext_to_binary(plaintext, bit_size)[int(len(plaintext_to_binary(plaintext, bit_size))/2):]
    return [L0, R0]


def step_two(plaintext, bit_size):
    '''
    R0 is encoded and stored in a variable `E`. For the encoding,
    we simply reverse R0 using the `reverse_string` function
    '''
    R0 = step_one(plaintext, bit_size)[1]
    E = encrypt_keys(R0, 8)
    return [R0, E]

def step_three(plaintext, bit_size):
    '''
    What we do in step three is to form the L1 and R1.
    L1 = R0 and R1 = L0 XOR E
    We use the XoR function we defined above for this
    '''
    L1 = step_two(plaintext, bit_size)[0]
    L0 = step_one(plaintext, bit_size)[0]
    E = step_two(plaintext, bit_size)[1]
    R1 = ''.join(XoR(L0, E))
    return [L1, R1]

def step_four(plaintext, bit_size):
    '''
    In this final step, we join L1 and R1 using string concatenation
    '''
    return ''.join(step_three(plaintext, bit_size))

plaintext = '''All things bright and beautiful. All creatures great and small. All things wise and wonderful. The Lord God made them all.'''
print(step_four(plaintext, 8))
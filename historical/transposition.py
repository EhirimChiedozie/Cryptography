
def transposition_encrypt(plaintext, key):
    plaintext = plaintext + (key-len(plaintext)%key) * ' '
    plaintext = plaintext.replace(' ', '-')
    nested_list_plaintext = []
     
    for i in range(0,int(len(plaintext)-key+1), key):
        list_items = list(plaintext[i:i+key])
        nested_list_plaintext.append(list_items)

    count = 0
    encrypt_list = []
    while count < key:
        joint_items = []
        for item in nested_list_plaintext:
            joint_items.append(item[count])
        encrypt_list.append(joint_items)
        count += 1


    join_lists = [''.join(item) for item in encrypt_list]
    ciphertext = ''.join(join_lists)
    return ciphertext


def transposition_decrypt(ciphertext, key):
    used_key = int(len(ciphertext)/key)
    nested_list_ciphertext = []
    for i in range(0, len(ciphertext), used_key):
        list_items = list(ciphertext[i:i+used_key])
        nested_list_ciphertext.append(list_items)

    count = 0
    decrypt_list = []
    while count < used_key:
        joint_items = []
        for i in nested_list_ciphertext:
            joint_items.append(i[count])
        decrypt_list.append(joint_items)
        count += 1
    join_lists = [''.join(item) for item in decrypt_list]
    plaintext = ''.join(join_lists)
    return plaintext

def bruteforce_transposition(message):
    for key in range(1,len(message)):
        try:
            print(transposition_decrypt(message, key), key)
        except Exception:
            pass

ciphertext = '''tbsvzhr-eyeojr--wu-dqnmtou-phgifeescod--kx-l--eoa-'''
print (bruteforce_transposition(ciphertext))

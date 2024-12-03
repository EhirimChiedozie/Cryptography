binary_message = [
    '01000010', '01101001', '01101110', '01100001', '01101110', '01100011', '01100101','00100000','01101100',
    '01101111', '01110110', '01100101', '01110011', '00100000', '01111001', '01101111', '01110101'
]
base_ten = [int(i, 2) for i in binary_message]
message_list = [chr(j) for j in base_ten]
message = ''.join(message_list)
print(message) 
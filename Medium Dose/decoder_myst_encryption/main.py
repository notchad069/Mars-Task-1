msg = input("Enter the encrypted message real quick : ")
msgg = msg.upper()
msg_letters = list(msgg)
dec_letters = []
j = 1
for i in range(len(msg_letters)):
    dec_letters.append(chr(ord(msg_letters[i])-j))
    j = j+1
dec_msg = "".join(dec_letters)
print("The decrypted msg is:" , dec_msg)

def decryption():
    code = input("enter the msg : ")
    dist = int(input("enter distance value : "))
    plainText = ""

    for ch in code:
        cipherV = ord(ch) - dist
        if(cipherV < ord('a')):
            cipherV = ord('z') - ord('a') - ord(ch) - dist - 1
        plainText += chr(cipherV)
    print(plainText)


def decrypt(text, s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) - s - 65) % 26 + 65)
        else:
            result += chr((ord(char) - s - 97) % 26 + 97)
    return result
    

decryption()
encrypted_text = "LIPPS"
s = 4
print(decrypt(encrypted_text, s))  # 'HELLO'


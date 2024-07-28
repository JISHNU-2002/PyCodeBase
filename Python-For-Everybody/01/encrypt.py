def encryption():
    plainText = input("enter the msg : ")
    dist = int(input("enter distance value : "))
    code = ""

    for ch in plainText:
        cipherV = ord(ch) + dist
        if(cipherV > ord('z')):
            cipherV = ord('a') - ord('z') - ord(ch) + dist + 1
        code += chr(cipherV)
    print(code)


def encrypt(text, s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) + s - 65) % 26 + 65)
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
    return result


encryption()
text = "HELLO"
s = 4
print(encrypt(text, s))  # 'LIPPS'


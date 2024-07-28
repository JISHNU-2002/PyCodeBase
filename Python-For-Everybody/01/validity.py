"""Write a Python program to check the validity of a password given by the
user.
The Password should satisfy the following criteria:
1. Contains at least one letter between a and z
2. Contains at least one number between 0 and 9
3. Contains at least one letter between A and Z
4. Contains at least one special character from $, #, @
5. Minimum length of password: 6"""
password = input("Enter the Password :")
l = n = L = sp = 0

for ch in password:
    if (len(password) >= 6):
        if (ch.islower()):
            l += 1
        elif (ch.isupper()):
            L += 1
        elif (ch.isdigit()):
            n += 1
        elif (ch == '$' or ch == '#' or ch == '@'):
            sp += 1
if (l >= 1 and L >= 1 and n >= 1 and sp >= 1):
    print("Valid Password")
else:
    print("Not Valid")

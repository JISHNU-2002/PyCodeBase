str1 = str(input('Enter a string = '))
n = len(str1)

for i in range(len(str1)-1,-1,-1):
    print(str1[i],end = "")
print()
n = int(input('Enter no of rows = '))

#right number pyramid
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end = " ")
    print()
print('\n')

#invert number pyramid
for i in range(n+1,1,-1):
    for j in range(1,i):
        print(j,end = " ")
    print()
print('\n')

#right alphabet pyramid
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(64+j),end = " ")
    print()
print('\n')

#invert alphabet pyramid
for i in range(n+1,1,-1):
    for j in range(1,i):
        print(chr(64+j),end = " ")
    print()
print('\n')



#left number pyramid
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end = " ")
    for k in range(1,i+1):
        print(k,end = " ")
    print()
print('\n')

#invert number pyramid
for i in range(n+1,1):
    for j in range(n-i+1,i):
        print(" ",end = " ")
    for k in range(n-i+1,i,-1):
        print(k,end = " ")
    print()
print('\n')

#left alphabet pyramid
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end = " ")
    for k in range(1,i+1):
        print(chr(64+k),end = " ")
    print()
print('\n')
#invert alphabet pyramid



#number pyramid
for i in range(1,n+1):
    for j in range(1, n-i+1):
        print(" ",end = " ")
    for k in range(1,i+1):
        print(k,end = " ")
    for m in range(i-1,0,-1):
        print(m,end = " ")
    print()
print("\n")

#invert number pyramid

#alphabet pyramid

#invert alphabet pyramid


#multiplication table of n
for i in range(1,11):
    print('{} * {} = {}'.format(i,n,n*i))
print('\n')



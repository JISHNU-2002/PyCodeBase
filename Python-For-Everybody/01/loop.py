for ascii in range(128):
    print(ascii,chr(ascii),end = "\n")
print(list(range(5)))

for count in range(5):
    print(count)

for count in range(100,110):
    print(count)

#(start,stop,step)
for count in range(1000,1010,2):
    print(count)

x = int(input('Enter num1 = '))
y = int(input('Enter num2 = '))
product = 1
for i in range(y):
    product = product*x
    print(product,end = "\n")
print('product = ',product)

#factorial of a number
num = int(input('Enter a number to find factorial of = '))
fact = 1
for i in range(num):
    fact = fact*(i+1)
print('factorial of {} using for loop = {}'.format(num,fact))

fact = 1
n = num
while(n!=0):
    fact = fact*n
    n-=1
print('factorial of %d using while loop = %d'%(num,fact))

#string
string = 'python'
for ch in string:
    print(ch,ord(ch))



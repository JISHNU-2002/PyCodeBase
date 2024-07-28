sum = 0
count = 0
while True:
    number = input("Enter a number or press Enter to quit: ")
    if number == "":
        break
    sum += float(number)
    count += 1
print("The sum is", sum)
if count > 0:
    print("The average is", sum / count)
print()

s = 0
count = 0
while True:
    n = input('Enter a number = ')
    if(n == ""):
        break
    s += int(n)
    count +=1

print('Sum = ',s)
if(count>0):    
    print('Average = ',s/count)

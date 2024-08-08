n = int(input('Enter no of terms = '))
n1 = 1
n2 = 1
print(n1,n2,sep = "->",end = "->")
while(n-2 != 0 ):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    n-=1
    print(n3,end = "->")



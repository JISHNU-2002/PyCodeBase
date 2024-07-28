def pascaltriangle(n):
    for i in range(0,n+1):
        for j in range(1, n-i):
            print(" ",end = "")
        for k in range(0,i+1):
            print(int(ncr(i,k)),end= "")
    print()
pascaltriangle(10)

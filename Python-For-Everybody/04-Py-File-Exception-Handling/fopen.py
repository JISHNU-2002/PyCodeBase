with open('file.txt','r') as fptr:
    #fp = fptr.read()
    #fp = fptr.readlines()
    fp = fptr.readlines(16)
    print(fp)
list = ['whatsapp','facebook']
with open('file2.txt','w') as fs:
    fp = fs.write('this is line1\n')
    print(fp)
    for i in list:
        fp = fs.write(i+"\n")
        print(fp)

with open('file.txt','r') as fo:
    with open('file3.txt','w') as fs:
        for line in fo:
            fs.write(line)
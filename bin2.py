

def bin2(n):
    r=n
    b=''
    # b=str(r)
    while r!=0:
        q=r%2
        b=str(q)+b
        r=r//2

    return b
for i in range(0,10):
    print(i,"=",bin2(i))


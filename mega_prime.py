def pn(n):
    c=0
    for i in range (1,n+1):
        if n%i==0:
            c=c+1
    if c==2:
        return True
    return False
n=int(input ())
v=[]
if pn(n):
    c=str(n)
    d=len(c)
    for i in c:
        if pn(int(i)):
            v.append(i)
            m=len(v)
    if d==m:
        print('Mega Prime')
    else:
        print('Not Mega Prime')
else:
    print('Not Mega Prime')
n=int(input())
s=0
while n>0:
    r=n%10
    s=s+r**2
    n=n//10
    if n==0 and s>9:
        n=s
        s=0
if s==1 or s==3:
    print('True')
else:
    print('False')

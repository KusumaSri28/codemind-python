m,n=map(int,input().split())
while 1:
    if m==0 or n==0:
        break
    if m>n:
        m%=n
    else:
        n%=m
if n==0:
    print(m)
else:
    print(n)
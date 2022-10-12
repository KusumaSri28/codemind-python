m,n=map(int,input().split())
for i in range(1,m+1):
    if m==0 or n==0:
        break
    elif m>n:
        m%=n
    else:
        n%=m
if m==0:
    print(n)
else:
    print(m)
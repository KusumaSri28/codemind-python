n=int(input ())
m=abs(n)
r=0
while m>0:
    s=m%10
    r=r*10+s
    m=m//10
if n<0:
    print(-r)
else:
    print(r)
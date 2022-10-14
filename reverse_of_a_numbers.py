n=int(input ())
r=0
while n>0:
    s=n%10
    r=r*10+s
    n=n//10
print (r)

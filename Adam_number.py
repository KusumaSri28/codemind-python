n=int(input ())
o=n*n
s=0
p=0
while n>0:
    r=n%10
    s=s*10+r
    n=n//10
m=s*s
while m>0:
    q=m%10
    p=p*10+q
    m=m//10
if p==o:
    print("True")
else:
    print ("False")
    
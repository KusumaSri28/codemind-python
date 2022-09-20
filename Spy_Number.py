n=int(input ())
s=0
p=1
while n>0:
    j=n%10
    s+=j
    p=p*j
    n=n//10
if s==p:
    print("Spy Number")
else:
    print("Not Spy Number")
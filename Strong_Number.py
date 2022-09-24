import math
n=int(input ())
p=n
r=0
while n>0:
    s=n%10
    n=n//10
    m=math.factorial(s)
    r+=m
if r==p:
    print("The number",p,"is a strong number")
else:
    print("The number",p,"is not a strong number")
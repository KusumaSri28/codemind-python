import math
n,m,p=map(int, input ().split ())
b=math.pow(n,m)
print(format (b%p,".0f"))
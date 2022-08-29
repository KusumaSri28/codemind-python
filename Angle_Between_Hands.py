h,n=map(int, input ().split(":"))
c=abs(30*(h%12)-5.5*n)
print(min(c,360-c))

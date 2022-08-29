h,m=map (int, input ().split(":"))
a=abs(30*(h%12)-5.5*m)
print(min(a,360-a))
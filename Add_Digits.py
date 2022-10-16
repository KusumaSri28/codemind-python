def add(a):
    s=0
    while a>0:
        r=a%10
        s=s+r
        a=a//10
    return s
a=int(input())
while a>9:
    a=add(a)
print(a)
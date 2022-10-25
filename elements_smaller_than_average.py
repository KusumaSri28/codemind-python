n=int(input())
ar=list(map(int,input().split()))
p=0
c=0
for i in range(n):
    p+=ar[i]
o=p//n
for i in range(n):
    if ar[i]<=o:
        c+=1
print(c)
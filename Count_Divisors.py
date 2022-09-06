m,n,p=map(int, input ().split())
s=0
for i in range (m,n+1):
    if i%p==0:
        s+=1
print (s)
    
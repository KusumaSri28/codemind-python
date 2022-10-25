n=int(input ())
m=list(map(int, input ().split()))
p=0
h=0
for i in range (n):
    p+=m[i]
o=p//n
for i in range (n):
    if o>=m[i]:
        h+=1
print(h)
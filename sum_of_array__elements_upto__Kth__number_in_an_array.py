n=int(input ())
m=list(map(int, input ().split()))
p=int(input ())
h=0
for i in range (p):
    h+=m[i]
print(h)
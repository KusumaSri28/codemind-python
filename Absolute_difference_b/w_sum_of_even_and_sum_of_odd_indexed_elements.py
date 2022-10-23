n=int(input ())
m=list(map(int, input ().split()))
p=0
o=0
for i in range (n):
    if i%2==0:
        p+=m[i]
    else:
        o+=m[i]
print(abs(p-o))
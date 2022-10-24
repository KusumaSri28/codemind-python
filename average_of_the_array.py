n=int(input ())
m=list(map(int, input ().split()))
h=0
for i in range (n):
    h+=m[i]
print(format( (h/n),".2f"))
n=int(input ())
m=list(map(int, input ().split()))
p=0
for i in range (n):
    p+=m[i]
o=p//n
if o in m:
    print("True")
else:
    print ("False")
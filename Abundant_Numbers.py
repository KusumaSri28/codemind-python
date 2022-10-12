n=int(input())
r=0
for i in range(1,n):
    if n%i==0:
        r+=i
if r>n:
    print('True')
else:
    print('False')
    
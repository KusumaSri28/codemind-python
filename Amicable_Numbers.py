n=int(input())
m=int(input())
p=0
o=0
for i in range(1,n):
    if n%i==0:
        p+=i
for i in range(1,m):
    if m%i==0:
        o+=i
if p==m and n==o:
    print('Amicable')
else:
    print('Not Amicable')
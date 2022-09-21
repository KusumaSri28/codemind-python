n=int(input())
s=0
m=n*n
while m>0:
    r=m%10
    s+=r
    m=m//10
if n==s:
    print('Neon Number')
else:
    print('Not Neon Number')
    
n=int(input())
o=0
m=n*n
while m>0:
    p=m%10
    o+=p
    m=m//10
if o==n:
     print('Neon Number')
else:
     print('Not Neon Number')
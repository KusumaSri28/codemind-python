n,m=map(int,input().split())
for i in range(1,n+1):
    a=m*i
    if a%n==0:
       print(a)
       break
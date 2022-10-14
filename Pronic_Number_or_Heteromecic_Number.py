n=int(input())
p=0
for i in range(1,n):
    if i*(i+1)==n:
        p+=1
        break
if p==1:
    print('YES')
else:
    print('NO')
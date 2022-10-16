n=int(input())
m=int(input())
for i in range(n,m+1):
    if i>1:
        for num in range(2,i):
            if i%num==0:
                break
        else:
                print(i)
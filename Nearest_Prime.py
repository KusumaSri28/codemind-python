m=int(input())
for _ in range(m):
    n=int(input())
    np=n
    while True:
        fc=0
        for i in range(1,np+1):
            if np%i==0:
                fc+=1
        if fc==2:
            break
        np-=1
    cp=n
    while True:
        fc=0
        for i in range(1,cp+1):
            if cp%i==0:
                fc+=1
        if fc==2:
            break
        cp+=1
    x=cp-n
    y=n-np
    if x>y:
        print(np)
    elif x<y:
        print(cp)
    elif x==y:
        print(min(np,cp))
    


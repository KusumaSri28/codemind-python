m,n,p=map(int,input().split())
if m>50 and n>60 and p>100:
    print(10)
elif m>50 and n>60 and p<100:
    print(9)
elif m<50 and n>60 and p>100:
    print(8)
elif m>50 and p>100 and n<60:
    print(7)
elif m>50 and p<100 and n<60:
    print(6)
elif m<50 and p>100 and n<60:
    print(6)
elif m<50 and p<100 and n>60:
    print(6)
else:
    print(5)
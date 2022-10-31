n=input()
p=0
for i in str(n):
    p=n.count(i)
    if p>1:
       print('Not Unique Number')
       break
else:
    print('Unique Number')
    
    
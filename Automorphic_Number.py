n=int(input())
m=pow(n,2)
mod=pow(10,len(str(n)))
if m%mod==n:
    print('Automorphic Number')
else:
    print('Not an Automorphic Number')
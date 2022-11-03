n=int(input())
k=list(str(n))
for i in range(len(k)):
    if k[i]=='6':
        k[i]='9'
        break
    else:
        continue
a="".join(k)
print(int(a))
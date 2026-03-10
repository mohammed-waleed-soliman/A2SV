n, k = map(int,input().split())
a = list(map(int,input().split()))
i = 0
j = 0
s = 0
res = 0
while j<n:
    s+=a[j]
    while s>k:
        s-=a[i]
        i+=1
    res = max(res,j-i+1)
    j+=1
print(res)

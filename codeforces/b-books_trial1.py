n, t = map(int,input().split())
a = list(map(int,input().split()))
i = 0
sum = 0
res = 0
for j in range(n):
    sum+=a[j]
    if sum<=t:
        res = max(res,j-i+1)
    else:
        while i<j:
            if sum<=t:
                break
            sum-=a[i]
            i+=1
print(res)

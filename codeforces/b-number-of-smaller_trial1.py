n, m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
j = 0
a.append(b[m-1]+1)
res = []
for i in range(m):
    while b[i]>a[j]:
        j+=1
    res.append(j)
print(*res)

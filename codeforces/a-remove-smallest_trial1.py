t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    cond = True
    for i in range(n-1):
        if(a[i+1]-a[i]>1):
            cond = False
    if cond:
        print("YES")
    else:
        print("NO")
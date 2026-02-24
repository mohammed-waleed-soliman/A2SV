n = int(input().strip())
a = list(map(int, input().rstrip().split()))

for i in range(1,n):
    ind = i-1
    temp = a[i]
    cond = False
    while ind>=0 and a[ind]>temp:
        a[ind+1] = a[ind]
        print(*a)
        ind -=1
        cond = True
    if cond:
        a[ind+1] = temp
        print(*a)
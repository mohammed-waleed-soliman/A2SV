n = int(input())
a = list(map(int,input().split()))
res = [0]*100
for i in a:
    res[i]+=1
print(*res)
n = int(input())
a = list(map(int,input().split()))
x = False
y = False
for i in a:
    if i%2:
        x=True
    else:
        y=True
if x and y:
    a.sort()
    print(*a)
else:
    print(*a)
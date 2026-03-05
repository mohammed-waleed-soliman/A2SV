n, k = map(int,input().split())
a = list(map(int,input().split()))
a.sort()
freq = dict()
for i in a:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
count=0
x = 1
for key in freq:
    if(count>=k):
        break
    count += freq[key]
    x = key
if k==0 and a[0]==1:
    print(-1)
elif count==k:
    print(x)
else:
    print(-1)
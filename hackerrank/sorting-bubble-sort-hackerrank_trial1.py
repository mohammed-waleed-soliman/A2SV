size = int(input())
a = list(map(int,input().split()))
count = 0
for i in range(len(a)):
    for j in range(len(a)-1-i):
        if(a[j]>a[j+1]):
            count+=1
            temp = a[j]
            a[j]=a[j+1]
            a[j+1]=temp
print(f"Array is sorted in {count} swaps.")
print(f"First Element: {a[0]}")
print(f"Last Element: {a[len(a)-1]}")
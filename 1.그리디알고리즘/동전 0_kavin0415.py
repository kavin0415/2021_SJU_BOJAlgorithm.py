n,k=map(int,input().split())
a=list(range(n))
count=0
for i in range(n):
    a[i]=int(input())
for i in range(n):
    while a[n-i-1]<=k:
        tem=int(k/a[n-i-1])
        k=k%a[n-i-1]
        count+=tem
print(count)

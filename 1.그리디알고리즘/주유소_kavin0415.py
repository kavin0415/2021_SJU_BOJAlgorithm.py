N=int(input())
road=list(map(int,input().split()))
cost=list(map(int,input().split()))
money=0
i=0
jump=0
lowcost=cost[0]
for i in range(0,N-1,1):
    if lowcost<cost[i]:
        money+=lowcost*road[i]
    else:
        money+=cost[i]*road[i]
        lowcost=cost[i]
print(money)
        

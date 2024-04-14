from collections import defaultdict
n=int(input())
l=list(map(int, input().split()))
d=defaultdict(int)
ans=0
for i in l:
    ans+=d[-i]
    d[i]+=1
print(ans)
T=int(input())
l1 = list(map(int,input().strip().split()))
l=-1
u=-1
cnt=1
for i in range(len(l1)):
    if l1[i]%2==0:
        l=i
        break
if l!=-1:
    for i in range(l,len(l1)):
        if l1[i]>T:
            u=i-1
            break
    if u==-1:
        u=len(l1)-1
    if u==l:
        print(1)
    else:
        for i in range(l,u):
            if l1[i]%2!=l1[i+1]%2:
                cnt=cnt+1
        print(cnt)
else:
    print(0)
            

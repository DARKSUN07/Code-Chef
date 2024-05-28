N,H,x=map(int,input().split())
T=list(map(int, input().strip().split()))
Ti=max(T)
if Ti+x<H:
    print("NO")
elif Ti+x>=H:
    print("YES")

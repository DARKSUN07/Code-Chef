T=int(input())
for i in range(T):
    N,M,X=map(int,input().split())
    if M==X:
        print("0")
    else:
        ans=int((N*X)/(X+1))
        print(ans)

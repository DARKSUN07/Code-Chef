n=int(input())
def cal(A,K):
    store=0
    count=0
    for j in A:
        if j>=K:
            store=store+(j-K)
        elif j<K and j+store>=K:
            store=(j+store)-K
        elif j<K and j+store<K:
            print("NO",count+1)
            return None
        count=count+1
    return True

for i in range(n):
    N,K=map(int,input().split())
    A=list(map(int,input().strip().split()))
    if cal(A,K):
        print("YES")

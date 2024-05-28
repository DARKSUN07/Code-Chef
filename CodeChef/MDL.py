T=int(input())
for i in range(T):
    N=int(input())
    A=list(map(int,input().split()))
    if A.index(max(A))>A.index(min(A)):
        print(min(A),max(A))
    else:
        print(max(A),min(A))

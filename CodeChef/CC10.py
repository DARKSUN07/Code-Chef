N,Q=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
for i in range(Q):
    L,R=map(int,input().split())
    num=L-1
    strength=0
    for j in range(R-L+1):
        pro=A[num]*B[num]
        strength=strength+pro
        num=num+1
    print(strength)

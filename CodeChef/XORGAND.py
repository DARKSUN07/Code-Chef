for i in range(int(input())):
    N=int(input())
    A=list(map(int,input().split()))
    for j in range(int(input())):
        L,R,X=map(int,input().split())
        l=A[L-1:R+1]
        cnt=0
        for k in l:
            if k & X==0:
                cnt+=1
        print(cnt)

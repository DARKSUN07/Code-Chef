T=int(input())
for i in range(T):
    N,X=map(int,input().split())
    H=list(map(int,input().split()))
    l1=[]
    count=0
    leng=len(H)
    maxi=max(H)
    if leng>=maxi:
        print(maxi)
    else:
        for i in range(leng):
            l1.append(H[i])
        for j in range(leng):
            while l1[j]>0:
                l1[j]=l1[j]-X
                count+=1
        if leng<maxi and count<maxi:
            print(count)
        else:
            print(maxi)

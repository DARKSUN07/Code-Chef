for i in range(int(input())):
    N=int(input())
    H=list(map(int,input().split()))
    H.sort()
    count=0
    maxi=0
    if N==1:
        print(H[0])
    else:
        for j in range(len(H)-1,1,-1):
            if H[j]==H[j-1]:
                count+=1
            elif maxi<H[j]+1:
                maxi=H[j]+count
                count=0
        print(maxi)

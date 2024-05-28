for T in range(int(input())):
    l=list(map(int,input().split()))
    cnt=0
    for i in range(len(l)-1,0,-1):
        for j in range(i):
            if l[j]>l[j+1]:
                temp=l[j]
                l[j]=l[j+1]
                l[j+1]=temp
                cnt+=1
    print(cnt)

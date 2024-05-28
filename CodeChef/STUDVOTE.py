for T in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int,input().split()))
    l1=[]
    for i in range (len(a)):
        A=a
        if len(A)==0:
            break
        if a[i]==i+1:
            ele=a[i]
            x=[k for j,k in enumerate(A) if k!=ele]
    for i in range (1,len(a)+1):
        l1.append(a.count(i))
    cnt=0
    for i in l1:
        if i>=k:
            cnt+=1
    continue
    print(cnt)

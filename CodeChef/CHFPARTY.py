for T in range(int(input())):
    n= int(input())
    l1 = list(map(int,input().split()))
    l1.sort()
    if(l1[0]==0):
        s = 1
        for i in range(1,n):
            if(l1[i]<=s):
                s = s + 1
            else:
                break
        print(s)
    else:
        print(0)

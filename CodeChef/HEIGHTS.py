import math
for T in range(int(input())):
    N=int(input())
    if N==0 or N==1:
        print("0")
    else:
        l=list(map(int,input().split()))
        l.sort()
        cnt=0
        i=0
        while i<N:  
            if i+1==N:
                if i>0 and l[i-1]!=l[i]:
                    cnt+=1
                    break
                else:
                    break
            elif l[i]!=l[i+1]:
                if i>0 and l[i-1]==l[i]:
                    cnt-=1
                cnt+=1
                i+=1
            else:
                i+=1
        print(math.ceil(cnt/2))
        

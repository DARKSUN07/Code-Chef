T=int(input())

def check(S):
    leng=len(S)
    if leng>50:
        S=S[:51]
    for j in range(leng):
        if S[j]=="1":
            break
        elif j==leng-1:
            return False
    for k in range(j,leng):
        if S[k]=="0":
            break
        elif k==leng-1:
            return True
    if k==leng:
        return True
    else:
        for l in range(k,leng):
            if S[l]=="1":
                return False
            elif l==leng-1:
                return True

if T>10:
    T=10
for i in range(T):
    S=input()
    if check(S):
        print("YES")
    else:
        print("NO")
            

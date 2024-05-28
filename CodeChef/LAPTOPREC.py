def mode(ls): 
    counts = {}
    for item in ls:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    return [key for key in counts.keys() if counts[key] == max(counts.values())]

T=int(input())
for i in range(T):
    N=int(input())
    A=list(map(int,input().split()))
    l=mode(A)
    if len(l)==1:
        print(l[0])
    else:
        print("CONFUSED")

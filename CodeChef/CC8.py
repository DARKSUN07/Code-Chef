n=int(input())
for i in range(n):
    X,Y,Z=map(int,input().split())
    if X+Y<=Z:
        print("2")
    elif X+Y>Z:
        if X<=Z:
            print("1")
        else:
            print("0")

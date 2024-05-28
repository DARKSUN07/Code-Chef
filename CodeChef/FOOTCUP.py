for i in range(int(input())):
    X,Y=map(int,input().split())
    if X==Y and X==0:
        print("NO")
    elif X==Y:
        print("YES")
    else:
        print("NO")

for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    if a.count(0)>a.count(1):
        print("0")
    else:
        print("1")

T=int(input())
for i in range(T):
    X,Y,Z=map(int,input().split())
    num=(Z-Y)//X
    print(num)

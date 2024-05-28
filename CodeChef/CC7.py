n=int(input())
for i in range(n):
    X,Y=map(int,input().split())
    if X*100<Y*10:
        print("Disposable")
    elif X*100>=Y*10:
        print("Cloth")

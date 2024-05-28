n=int(input())

for i in range (n):
    x,y,z=map(int,input().split())
    if x+y==z:
        print("EQUAL")
    elif x+y<z:
        print("PLANEBUS")
    elif x+y>z:
        print("TRAIN")

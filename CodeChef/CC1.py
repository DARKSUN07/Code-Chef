num=int(input())

def compare(x,y):
    if x>y:
        print("A")
    else:
        print("B")

for i in range (num):
    num1,num2=map(int,input().split())
    compare(num1,num2)
    

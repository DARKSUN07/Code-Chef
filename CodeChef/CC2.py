n=int(input())

def coins(x):
    if x%5!=0:
        print("-1")
    elif x%10==0:
        print(int(x/10))
    elif x%10==5:
        money=0
        money=money+x//10+1
        print(money)

for i in range (n):
    money=int(input())
    coins(money)
    

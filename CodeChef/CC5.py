T=int(input())

for i in range(T):
    N,A,B=map(int,input().split())
    print(2*(180+N)-(A+B))

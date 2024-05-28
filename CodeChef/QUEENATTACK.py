for i in range(int(input())):
    N,X,Y=map(int,input().split())
    mini=min(X,Y)
    maxi=max(X,Y)
    if N==1:
        print("0")
    elif N==2:
        print("3")
    else:
        if N%2==1:
            if mini<=(N+1)/2 and maxi<=(N+1)/2:
                print(int(((N-1)*3)+((mini-1)*2)))
            elif mini<=(N+1)/2 and maxi>=(N+1)/2:
                if ((N+1)/2)-mini>=maxi-((N+1)/2):
                    print(int(((N-1)*3)+((mini-1)*2)))
                elif ((N+1)/2)-mini<maxi-((N+1)/2):
                    print(int(((N-1)*3)+((N-maxi)*2)))    
            elif mini>=(N+1)/2 and maxi>=(N+1)/2:
                print(int(((N-1)*3)+((N-maxi)*2)))

        else:
            if mini<(N+1)/2 and maxi<(N+1)/2:
                print(int(((N-1)*3)+((mini-1)*2)))
            elif mini<(N+1)/2 and maxi>(N+1)/2:
                if ((N+1)/2)-mini>=maxi-((N+1)/2):
                    print(int(((N-1)*3)+((mini-1)*2)))
                elif ((N+1)/2)-mini<maxi-((N+1)/2):
                    print(int(((N-1)*3)+((N-maxi)*2)))    
            elif mini>(N+1)/2 and maxi>(N+1)/2:
                print(int(((N-1)*3)+((N-maxi)*2)))

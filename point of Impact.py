# cook your dish here
def pointofImpact():
    try:
        T=int(input())
        while(T):
            n,k,x,y=map(int,input().split())
            if(x==y):
                print(n,n)
            else:
                Q=[]
                if(x<y):
                    Q=[[x+n-y,n],[n,x+n-y],[y-x,0],[0,y-x]]
                else:
                    Q=[[n,y+n-x],[y+n-x,n],[0,x-y],[x-y,0]]
                A=Q[(k-1)%4]
                print(A[0],A[1])
        T-=1
    except:
        pass
pointofImpact()
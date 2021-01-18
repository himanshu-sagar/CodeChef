# cook your dish here
def FairElections():
    try:
        T=int(input())
        while(T):
            n,m=map(int,input().split())
            a=list(map(int,input().split()))
            b=list(map(int,input().split()))
            a.sort()
            b.sort()
            ta=sum(a)
            tb=sum(b)
            if ta>tb:
                print(0)
                continue
            j=0
            ct=m-1
            for i in range(0,n):
                ta=ta-a[i]
                tb=tb-b[ct]
                ta=ta+b[ct]
                tb=tb+a[i]
                j+=1
                ct-=1
                if ta>tb or ct<0:
                    break
            if ta>tb:
                print(j)
            else:
                print(-1)
                
            T-=1
    except:
        pass
FairElections()

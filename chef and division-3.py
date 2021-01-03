# cook your dish here
def division3():
    try:
        T=int(input())
        while(T):
            n,k,d=map(int,input().split())
            A=list(map(int,input().split()))
            totalproblems=sum(A)
            res=totalproblems//k
            if totalproblems<k:
                print(0)
            
            elif res<=d and totalproblems>=k:
                print(res)
            else:
                print(d)
            
            T-=1
    except:
        pass
division3()

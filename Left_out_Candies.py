q=int(input())
while(q):
    q-=1
    n,t=map(int,input().split())
    while(t):
        t-=1
        if(n%2==0):
            n=n-(n//2)
        else:
            n=n-((n+1)//2)
        n=n-(n//4)
    print(n)

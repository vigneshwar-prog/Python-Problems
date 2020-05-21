n=int(input())
m1=[list(map(int,input().split())) for i in range(n)]
m2=[list(map(int,input().split())) for i in range(n)]
r=n
c=n
k=0
l=0
while(k<r and l<c):
   
    for i in range(l,c):
        print(m1[k][i],end=" ")
   
    for i in range(l,c):
        print(m2[k][i],end=" ")
   
    k+=1
   
    for i in range(k,r):
        print(m1[i][c-1],end=" ")
   
    for i in range(k,r):
        print(m2[i][c-1],end=" ")
    c-=1
   
    if k<r:
        for i in range(c-1,l-1,-1):
            print(m1[r-1][i],end=" ")
       
        for i in range(c-1,l-1,-1):
            print(m2[r-1][i],end=" ")
        r-=1
       
    if l<c:
        for i in range(r-1,k-1,-1):
            print(m1[i][l],end=" ")
       
        for i in range(r-1,k-1,-1):
            print(m2[i][l],end=" ")
        l+=1

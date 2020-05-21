t=int(input())
ans=[]
while(t):
    n=int(input())
    lst=list(map(int,input().split()))
    c=n
    count=1
    first=lst[0]
    for i in range(1,n):
        if(first==lst[i]):
            count+=1
        else:
            while(count):
                count-=1
                c+=count
            count=1
            first=lst[i]
    t-=1
    ans.append(c)
for i in ans:
    print(i)

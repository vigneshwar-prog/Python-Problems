b,v,c = list(map(int,input().split()))
x,y = list(map(int,input().split()))
flag=0
if x > y:
    flag=1
    x,y = y,x
    v,c = c,v
s=0
v_count,c_count=0,0
while b > 1 and (v > 0 or c > 0):
    if c > 0:
        s+=y
        c -= 1
        v_count+=1
    else:
        s+=x
        v -= 1
        c_count+=1
    b-=2
if(flag==0):
    print(c_count)
    print(v_count)
else:
    print(v_count)
    print(c_count)
print(s)

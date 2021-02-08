a=[1,2,3,4,7,4]
for i in range(1,len(a)):
    p=a[i]
    s=i-1
    while p>=\
            0 and a[p]>s:
        a[s+1]=a[s]
        p-=1
    a[p]=s
print(a)
def insert_sort(a):
    for i in range(1,len(a)):
        m=a[i]
        d=i-1
        while d>=0 and a[d]>m:
            a[d+1]=a[d]
            d-=1
        a[d+1]=m

a=[8,34,56,9,2,67,1,5,35,34,23,22,45,70,12,8]
print(a)
insert_sort(a)
print(a)
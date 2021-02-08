def sel_sort(a):
    for i in range(len(a)-1):
        m=i
        n=i+1
        while n<len(a):
            if a[m]>a[n]:
                m=n
            n+=1
        a[i],a[m]=a[m],a[i]



a=[8,34,56,9,2,67,1,5,35,34,23,22,45,70,12,8]
print(a)
sel_sort(a)
print(a)
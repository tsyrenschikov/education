from random import randint
def sel_sort(array):
    for i in range(len(a)-1):
        m=i
        j=i+1
        while j<len(a):
            if a[j]<a[m]:
                m=j
            j+=1
        a[i],a[m]=a[m],a[i]


a = []
for i in range(randint(3,10)):
    a.append(randint(1, 99))

print(a)
sel_sort(a)
print(a)
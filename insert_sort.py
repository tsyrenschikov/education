from random import randint
def InsertSort(a):
    for index in range(1,len(a)):
        p= a[index]
        sort = index - 1
        while (sort>= 0) and (a[sort] > p):
            a[sort+1] = a[sort]
            sort = sort - 1
        a[sort+1] = p

a=[]
for i in range(randint(2,20)):
    a.append(randint(1,99))
print(' Произвольные числа = ',a)
InsertSort(a)
print('Сортированные числа = ',a)
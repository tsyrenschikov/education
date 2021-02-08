from random import randint
n_list=[]
n1_list=[]
n2_list=[]
for i in range(randint(10,20)):
    n_list.append(randint(1,99))
    n1_list.append(randint(1, 99))
    n2_list.append(randint(1, 99))
print(n_list)
n3_list=list(filter(lambda x:x%2==0, map(int,n_list)))
print(n3_list)

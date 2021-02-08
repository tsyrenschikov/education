from random import randint
n_list=[]
n1_list=[]
for i in range(randint(10,20)):
    n_list.append(randint(1,99))
    n1_list.append(2)
print(n_list)
print(n1_list)
n_list=list(filter(lambda x:x%2==0,n_list))
n_list=list(map(pow,n_list,n1_list))
print(n_list)

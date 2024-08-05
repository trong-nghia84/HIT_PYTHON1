my_list=input()
my_list=my_list.split()
for i in range(len(my_list)):
    my_list[i]=int(my_list[i])
my_tuple=tuple(my_list)
count=0
for i in my_tuple:
    if i==i+1:
        count+=1
    if count%5==0:
        print(i)




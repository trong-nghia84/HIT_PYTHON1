n=int(input("n="))
fib_list=[0,1]
for i in range(2,n) :
    next_fib=fib_list[i-1]+fib_list[i-2]
    fib_list.append(next_fib)
print(fib_list)


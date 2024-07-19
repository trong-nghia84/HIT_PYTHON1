n=int(input("n="))
for i in range(1,n+1) :
    t=i
    s=0
    while t>0 :
        k= t%10
        s+=k**3
        t//=10
    if s==i :
        print(i);


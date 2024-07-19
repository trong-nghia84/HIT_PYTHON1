#Phan a:
n=int(input("n="))
s1=0
if n<0:
    print("S(n)=",s1)
else :
    for i in range(1,2*n+2) :
        s1+=(-1)**(i+1)*i
    print("S(n)=",s1)
#Phan b:
s2=0
if n<=0 :
    print("S(n)=", s2)
else :
    for i in range(1,n+1) :
        s2+=1/i
    print("S(n)=",s2)
#Phan c:
a=float(input("a="))
b=float(input("b="))
c=float(input("c="))
if a==0 :
    print("khong phai phuong trinh bac 2")
else :
    delta=b*b-4*a*c
    if delta<0 :
        print("Phuong trinh vo nghiem")
    elif delta==0 :
        print("phuong trinh co nghiem kep",-b/(2*a))
    else :
        print("phuong trinh co 2 nghiem")
        print("x1=",(-b+delta**0.5)/(2*a))
        print("x2=",(-b-delta**0.5)/(2*a))
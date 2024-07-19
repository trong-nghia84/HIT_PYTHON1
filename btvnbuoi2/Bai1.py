#Phan a:
a=int(input("nhap mot so nguyen: "))
tong_chu_so=0
while a>0:
    chu_so_cuoi =a%10
    tong_chu_so+=chu_so_cuoi
    a//=10
print("tong cac chu so cua so nguyen la:",tong_chu_so)

#Phan b:
n=int(input("n= "))
tong_cac_uoc=0
for i in range(1,n):
    if n %  i ==0:
        tong_cac_uoc+=i
print("tong cac uoc cua n la:",tong_cac_uoc)

#phan c:
b1= int(input("so_nguyen_1:"))
b2= int(input("so_nguyen_2:"))
b3= int(input("so_nguyen_3:"))
if b1+b2>b3 and b2+b3>b1 and b3+b1>b2 :
    print("la tam giac")
    if b1==b2 or b2==b3 or b3==b1 :
        if b1==b2 and b2==b3 and b3==b1 :
            print("la tam giac deu")
        else :
            print("la tam giac can")
    elif b1*b1+b2*b2==b3*b3 or b2*b2+b3*b3==b1*b1 or b3*b3+b1*b1==b2*b2 :
        print("la tam giac vuong")
    elif b1*b1+b2*b2>b3*b3 or b2*b2+b3*b3>b1*b1 or b3*b3+b1*b1>b2*b2 :
        print("la tam giac nhon")
    else :
        print("la tam giac tu")
else :
    print("khong la tam giac")
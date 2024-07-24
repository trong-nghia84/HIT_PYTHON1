my_list = list()
n=int(input("n="))
#cau 1:
for i in range(n):
    phan_tu=int(input(f"nhập phan tu thu {i+1}: "))
    my_list.append(phan_tu)
print(my_list)
x=int(input("nhap so can tim kiem: "))
count=0
for phan_tu in my_list:
    if phan_tu == x:
        count+=1
print(f"so lan suat hien cua {x} la:",count)

#cau 2:
my_list[2:7]= [8, 5, 4, 0, 1, 3]
print("list sau khi thay doi:",my_list)

#cau 4:
MAX=my_list[0]
MIN=my_list[0]
for phan_tu in my_list:
    if phan_tu > MAX:
        MAX=phan_tu
    if phan_tu < MIN:
        MIN=phan_tu
print("MAX=",MAX)
print("MIN=",MIN)

#cau 5:
y=int(input("y="))
my_list.insert(0,y)
print("list sau khi chen y:",my_list)

#cau 6:
tang_dan = True
giam_dan = True
for i in range(n+1):
    if my_list[i] < my_list[i+1]:
        giam_dan = False
    elif my_list[i] > my_list[i+1]:
        tang_dan = False
if tang_dan:
    print("TANG")
elif giam_dan:
    print("GIAM")
else:
    print("NO")

#cau 7:
new_list=list()
phan_tu_moi=0
for i in range(n+2):
    phan_tu_moi+=int(my_list[i])
    new_list.append(phan_tu_moi)
print("new_list:",new_list)

#cau 8:
my_list2=[94, 39, 49, 6, -55, -37, 1, -23, -31, 1000]
my_list2.sort()
print("sap tang dan cua gia tri",my_list2)
for i in range(n+1):
    my_list2[i]=abs(my_list2[i])
my_list2.sort()
print("sap mang tang dan theo gia tri tuyet doi:",my_list2)
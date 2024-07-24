n=int(input("n="))
x=str(input("chuoi :"))
x=x.strip()
danh_sach=x.split()
danh_sach_so= list(map(int, danh_sach))
count1=0
print(x)
so_thay_thich=[]
for so in danh_sach_so:
    if so%2==1:
        so_thay_thich.append(so)
        count1+=1
print("so luong so thay ba thich:",count1)
so_thay_thich.sort()
print("sap xep cac so thay thich:",so_thay_thich)

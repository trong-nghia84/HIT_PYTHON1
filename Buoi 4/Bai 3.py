x=str(input("n va m lan luot bang:"))
x=x.split()
n=int(x[0])
m=int(x[1])

mang=str(input("mang:"))
mang=tuple(mang.split())

tap_a=str(input("A:"))
tap_b=str(input("B:"))
tap_a=tuple(tap_a.split())
tap_b=tuple(tap_b.split())
print(tap_a)
print(tap_b)
happy_point=0
for i in range(n):
    for j in range(m):
        if tap_a[j] == mang[i]:
            happy_point+=1
        if tap_b[j] == mang[i]:
            happy_point-=1
print("diem hanh phuc :",happy_point)


a=str(input("xau:"))
a=a.split()
b=tuple(a)

print("mang a:",a)
print("tuple b:",b)
count=0
for i in b:
    if i.isdigit():
        count+=1
print("so phan tu co dang so:",count)

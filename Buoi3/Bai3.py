s1=input("chuoi s1:")
s2=input("chuoi s2:")
print("chuoi s1:",s1)
print("chuoi s2:",s2)

#cau 1:
print("chuoi s1 sau khi dao nguoc:",s1[::-1])

#cau 2:
a=int(input("a="))
b=int(input("b="))
if 1 <=a < b <= len(s2):
    chuoi_con = s2[a:b+1]
    chuoi_con_dao_nguoc = chuoi_con[::-1]
    s2n=s2[:a] + chuoi_con_dao_nguoc + s2[b+1:]
print("chuoi s2 sau khi dao nguoc:",s2n)

#cau 3:
s3=''
for i in range(0,len(s1),2):
    s3+=s1[i]
print("chuoi s3",s3)

#cau 4:
s4=''
if len(s1) >= len(s2):
    n=len(s1)
else:
    n=len(s2)
for i in range(n):
    s4+=s1[i]+s2[i]
print("chuoi s4:",s4)

#cau 5:
chuoi1_moi = s2[0] + s1[1:]
chuoi2_moi = s1[0] + s2[1:]
print(f"{chuoi1_moi} va {chuoi2_moi}")
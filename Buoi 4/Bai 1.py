# t=()
# t2=("hello",1,2,["some text",1,2])
# print(f"t={t}\t({type(t)})")
# print(f"t2={t2}\t({type(t2)})")

# t3="hello",1,2,["some text",1,2]
# t=t2
# print("t[2]=",t[2])
# print("t[3][2]=",t[3][2])
# t2=list(t2)
# print(t2)
# t2[0]="hi"
# t2=tuple(t2)
# print(t2)

# s={1,2,1,2,3,5,4}
# print(type(s))
# print(s)
# s.add([10])
# print(s)
# s.update([10,20])
# print(s)

# a={"blue","red","green"}
# b={"yellow","red","orange"}
# print(a&b)
# print(a|b)

# string="hoc lap trinh python with HIT"
# #cach 1:
# result=[]
# for char in string:
#     if char == " ":
#         continue
#     result.append(char)
# print("tuple1=",tuple(result))
#
# #cach 2:
# # result2=[]
# # for index in range(len(string)):
# #     if string[index] == " ":
# #         continue
# #     result2.append(string[index])
# # print("tuple2=",tuple(result2))
# #
# # #cach 3:
# # result3=[char for char in string if char !=" "]
# # print("tuple3=",tuple(result3))
# #
# string=tuple(string)
# print("count=",string.count('o'))
#
# count=0
# occurences_char_0=[count+1 for char in result3 if char == "o"]
# print("0 occurences=", len(occurences_char_0))

# max1=0
# max2=0
# my_list=[2,4,5,6,5,7,4]
# # for ptu in my_list:
# #     if ptu > max1 :
# #         max1=ptu
# # print(max1)
# # max2=0
# # for i in my_list:
# #     if i<max1 & i>max2:
# #         max2=i
# # print(max2)
#
# #in ra ptu lon thu 2 trong list
# my_list= set(my_list)
# l = list(my_list)
# print(l[-2])

tuple_xau=('6','5','7')
new_list =[int(x) for x in tuple_xau]
new_tuple=tuple(new_list)
print("tuple cu:",tuple_xau)
print("tuple moi:",new_tuple)
tong=sum(new_tuple)
count=len(new_tuple)
trung_binh_cong=tong/count
print("trung binh cong= ",trung_binh_cong)
#Phan a:
a=int(input("a="))
count=0
while a:
  count += a & 1
  a>>=1
print(count)

#Phan b:
x= "awesome"
print(f"Python is {x}") #kieu f-string (chuoi dinh dang)
print("Python is",x) #co ban
print("Python is {}".format(x)) #Phuong thuc format()


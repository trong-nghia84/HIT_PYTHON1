n=int(input("n="))
x=str(input("tap:"))
x=x.split()
for i in range(n):
    x[i]=int(x[i])
s=set(x)
print(s)
t=int(input())
a=0
sn= set()
for i in s:
    if a<t:
        a+=i
        sn.add(i)
print(sn)
def  sum(n):
    t=0
    while n>0:
        t+=n%10
        n//=10
    return t

def count_total(n):
    count=0
    while n>9:
        n=sum(n)
        count+=1
    return n,count
n=int(input("n="))
print(count_total(n))
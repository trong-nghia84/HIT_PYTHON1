n = int(input("Nhập số hàng N: "))
for i in range(1,n+1):
    for j in range(1,n+1):
        a[i][j]=0
for i in range(1,n+1):
    a[i][1]=1
for i in range(1,n+1):
    a[i][i]=1
for i in range(3,n+1):
    for j in range(2,n):
        a[i][j]=a[i-1][j-1]+a[i-1][j]
for i in range(1,n+1):
    for j in range(1,i):
        print(a[i][j],"")
    print(end="\n")
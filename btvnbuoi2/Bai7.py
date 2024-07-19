
n = int(input("Nhập số nguyên dương N: "))
for i in range(1,n + 1):
    tong_uoc_i=0
    for j in range(1,i):
        if i % j == 0:
            tong_uoc_i+=j
    if tong_uoc_i >i :
        tong_uoc_2=0
        for j in range(1,tong_uoc_i):
            if tong_uoc_i % j==0:
                tong_uoc_2+=j;
        if tong_uoc_2==i:
            print(i,tong_uoc_i,"la cap so Amicable")

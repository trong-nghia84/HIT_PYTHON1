n=int(input("n="))

for i in range(1,n+1):
    tong_cac_uoc=0
    for j in range(1,i):

        if i%j==0 :
            tong_cac_uoc+=j
    if tong_cac_uoc==i:
        print(i)


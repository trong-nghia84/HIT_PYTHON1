def matrix(ma_tran,n,m):
    so_hang = n
    so_cot = m
    ma_tran_chuyen_vi = [[0 for a in range(so_hang)] for b in range(so_cot)]

    for i in range(so_hang):
        for j in range(so_cot):
            ma_tran_chuyen_vi[j][i] = ma_tran[i][j]
    return ma_tran_chuyen_vi

n=int(input("n="))
m=int(input("m="))
ma_tran = []
for i in range(n):
    row = list(map(int, input().split()))
    ma_tran.append(row)
print("Ma trận chuyển vị:")
for row in matrix(ma_tran,n,m):
  print(row)
chuoi=input("chuoi:")
dem={}
for ki_tu in chuoi:
    if ki_tu in dem:
        dem[ki_tu]+=1
    else:
        dem[ki_tu]=1
print(dem)


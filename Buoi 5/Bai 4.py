def xuat (CONFIG):
    for key, value in CONFIG.items():
        print(key, value)
CONFIG={
    'n':'1500',
    'm':'2',
    'CLUSTERS':'3',
    'ITER':'10000',
    'METHOD':'FCM',
    'MEASURE':'EUCLIDEAN',
    'YEARS':'51'
}
xuat(CONFIG)
CONFIG['MEASURE']='MANHATAN'
xuat(CONFIG)
print("CONFIG:",CONFIG['METHOD'])
CONFIG['LOSS FUNCTION']='NORM_2'
xuat(CONFIG)
CONFIG.pop('YEARS')
xuat(CONFIG)
S=input('xau:')

if S in CONFIG.values():
    print('xau S trung voi gia tri cua thong so trong CONFIG')
else:
    print('sau S ko trung')
my_set=set()
my_list=list()
for i in CONFIG.values():
    my_set.add(i)
    my_list.append(i)
print(my_set)
print(my_list)

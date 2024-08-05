import pprint
my_dict= {
    "name":"john",
    "age": 30,
    "city":"new york",
    "score":{
        "math":80,
        "english": 90
    },

}
print(my_dict['name'])
pprint.pprint(my_dict)
for i in my_dict:
    print(i,my_dict[i])
for key,value in my_dict.items():
    print(key, value)
for i,key in enumerate(my_dict):
    print(i,key,my_dict[key])
for key in my_dict.values():
    print(key)
for i,(key,value) in enumerate(my_dict.items()):
    print(i,key,value)
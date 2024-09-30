# Dictionary is  a collection of key and values , it s mutable, it is a unordred ,it is a index based
# it contain a dupllicate values, inside Dictionary we can write list also
data = {
    1 :5,
    "name":"reetu"
}
print(data)
print(data.get(1)) # 5
print(data.keys()) # dict_keys([1, 'name'])
data.update({"name":"abi"})
print(data)  # {1: 5, 'name': 'abi'}

keys=['names','age']
values=['Reetu',25]
data=dict(zip(keys,values))
print(data) # {'names': 'Reetu', 'age': 25}
print(data['name'])
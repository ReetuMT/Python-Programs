# set is a collection of non-repeatative elements, it will not allow  duplicate values, set is not a index based
# in this we cant be change the values,
# set should be created using {} curly braces

b=set()
print(b)
b.add(3)
b.add(4)
b.add(2)
print(b) # {2, 3, 4}
b.add((1,6,3))
print(b) # {2, 3, 4, (1, 6, 3)}
# b.add([7,3])  not allowed
print(len(b)) # 4
b.pop()
print(b)


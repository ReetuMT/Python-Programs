#  List are container to store a set of values of any data type

num=[12,45,7,6]
print(num)
print(num[0])
print(num[1:3])
  # index out of range

# --------------------------
names=["reetu","abi","renu"]
print(names)
get=[names,num]
print(get)

# List methods
# 1.  Append function will add the values at the end of the list
names.append("malatesh")  
print(names)
# Output -['reetu', 'abi', 'renu', 'malatesh']

# 2. Insert function will add the values at the given index 
names.insert(2,"reshu")
print(names)  
# Output : ['reetu', 'abi', 'reshu', 'renu', 'malatesh']

#3. Remove function will remove the given value
names.remove("abi")
print(names)
# Output : ['reetu', 'reshu', 'renu', 'malatesh']

# Pop function will delete last value and it will delete the value index based also
names.pop()
print(names) # ['reetu', 'reshu', 'renu']
names.pop(2)
print(names)  #['reetu', 'reshu']


# extend method wiil add the multiple values at a time
names.extend([23,45,"reet"])
print(names) # ['reetu', 'reshu', 23, 45, 'reet']


nums=[345,43,56,3,6,123]
nums.sort()
print(nums)  # [3, 6, 43, 56, 123, 345]
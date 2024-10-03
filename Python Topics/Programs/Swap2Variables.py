a=4
b=3
temp=a
a=b
b=temp
print(f"a is = {a}  b value is = {b}")

# ------------------Or --------------------------
a=4
b=3
a=a+b
b=a-b
a=a-b
print("------------")
print(f"a is = {a}  b value is = {b}")

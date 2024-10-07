  # Global variable
name="Reetu"
id=101
def person_data():
    age = 25  # Local variable
    print(f"My name is :  = {name}")  # Accessing global variable
    print(f"id is :  = {id}")
    print(f"Age : = {age}")  # Accessing local variable

person_data()

print(f"Global name prints the :  = {name}")  # Accessing global variable


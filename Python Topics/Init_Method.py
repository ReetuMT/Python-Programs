class Person:
    def __init__(self, name, age):  
        self.name = name  
        self.age = age  

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Creating an object of the Person class
person = Person("Reetu", 23)
person1=Person("Renu",37)
person.display()  
person1.display()


# 
class Employee:
    pass

emp = Employee() 
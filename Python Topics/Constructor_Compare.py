class Employee:
    def __init__(self, name, age, salary):
        self.name = name  
        self.age = age     
        self.salary = salary 

    def get_data(self):
        print(f"Employee Name: {self.name}")
        print(f"Employee Age: {self.age}")
        print(f"Employee Salary: {self.salary}")
    
    def update_salary(self, new_salary):
        self.salary = new_salary  
        print(f"Updated Salary for {self.name}: {self.salary}")
    
    def age_compare(self, other_emp):
        if self.age > other_emp.age:
            print(f"{self.name} is older than {other_emp.name}.")
        elif self.age < other_emp.age:
            print(f"{self.name} is younger than {other_emp.name}.")
        else:
            print(f"{self.name} and {other_emp.name} are of the same age.")

emp1 = Employee("Abi", 28, 50000)
emp2 = Employee("Malatesh", 30, 55000)
emp1.get_data()
emp1.update_salary(70000)
print("--------------------------------")
emp2.get_data()
print("-----------------------------------")
emp1.age_compare(emp2)

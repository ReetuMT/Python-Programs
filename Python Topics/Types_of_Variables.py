class Car:

    wheel=4 # Class variable
    def __init__(self, name, color):
        self.name = name  # Instance variable
        self.color = color 
    def data(self):
        print(f"Car name is = {self.name}")
        print(f"Car color is = {self.color}")
        print(f"Number of wheels are = {self.wheel}")

        
Car.wheel=6  # Class variable
car1 = Car("kia", "Red")
car2 = Car("Honda", "Blue")
car1.data()


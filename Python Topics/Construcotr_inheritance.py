# Parent class (Super class)
class Vehicle:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
    
    def show_info(self):
        print(f"Vehicle Name: {self.name}")
        print(f"Speed: {self.speed} km/h")

# Child class 
class Car(Vehicle):
    def __init__(self, name, speed, model):
        super().__init__(name, speed)  
        self.model = model  
    def show_model(self):
        print(f"Car Model: {self.model}")

# Created a instance of the parent class
vehicle = Vehicle("Bike", 80)
vehicle.show_info()  
print("------------------------------------")
# Created a instance of the child class
car = Car("kia", 200, "A6")
car.show_info()     
car.show_model()

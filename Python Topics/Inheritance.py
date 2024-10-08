# # Single inheritance
# class Vehicle:
#     def vehicle_type(self):
#         print("Vehicle type is car")

# class Car(Vehicle):
#     def car_color(self):
#         print("Car color is Red")

# v1=Vehicle()
# v1.vehicle_type()
# print("---------------------------------")
# c1=Car()
# c1.car_color()
# c1.vehicle_type()

#Multilevel inheritance
# class Vehicle:
#     def vehicle_type(self):
#         print("Vehicle type is car")

# class Car(Vehicle):
#     def car_color(self):
#         print("Car is the one of the vehicle type")

# class Engine(Car):
#     def engine_type(self):
#         print("engine is present inside the car")
# v1=Vehicle()
# v1.vehicle_type()
# print("---------------------------------")
# c1=Car()
# c1.car_color()
# c1.vehicle_type()
# print("---------------------------------")
# e1=Engine()
# e1.car_color()
# e1.vehicle_type()
# e1.engine_type()

# Multiple Inheritance
class Vehicle:
    def vehicle_type(self):
        print("Vehicle type is car")

class Car():
    def car_color(self):
        print("Car is the one of the vehicle type")

class Engine(Vehicle, Car):
    def engine_type(self):
        print("engine is present inside the car")
eng=Engine()
eng.car_color()
eng.engine_type()
eng.vehicle_type()
class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

    def show_vehicle(self):
        print(f"Vehicle type: {self.vehicle_type}")

    # Inner class 
    class Engine:
        def __init__(self, engine_type):
            self.engine_type = engine_type

        def show_engine(self):
            print(f"Engine type: {self.engine_type}")

# Created an instance of the outer class 
v1 = Vehicle("Car")
v1.show_vehicle()  

# Created instance of the inner class 
e1 = Vehicle.Engine("V8 Engine")
e1.show_engine() 

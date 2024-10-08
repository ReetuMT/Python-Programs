class Overload:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    #  __add__ method
    def __add__(self, second_object):
        return Overload(self.a + second_object.a, self.b + second_object.b)
    
    # __mul__ mehtod
    def __mul__(self, second_object):
        return Overload(self.a * second_object.a, self.b * second_object.b)

    def __str__(self):
        return f"({self.a}, {self.b})"

p1 = Overload(2, 3)
p2 = Overload(4, 5)


result = p1 + p2
res=p1*p2

print(res)
print(result) 

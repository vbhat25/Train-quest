class Circle:
    def __init__(self,radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius
    
radius = float(input("Enter the radius of the circle: "))
cir = Circle(radius)

print("Area of the circle: {}" .format(cir.area()))
print("Perimeter of the circle: {}" .format(cir.perimeter()))
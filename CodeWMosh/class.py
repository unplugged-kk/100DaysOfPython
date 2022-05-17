
# Class is a blueprint for creating new objects
# Object : instance of a class

# class : human
# objects : jhon , marry , jack

# to name classes use pascal naming convention Point is preferred  on point in this case. no underscore
class Point:
    def draw(self):
        print("draw")


point = Point()
print(type(point))

print(isinstance(point, Point))

class Point:
    default_color = "red"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x},{self.y})")

# class methods have first parameter as cls instead of self. it can be anything else too except cls. we use decorators to differentiate class methods and instance method
    @classmethod
    def zero(cls):
        return cls(0, 0)


point = Point.zero()
point.draw()

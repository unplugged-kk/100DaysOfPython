class Point:
    default_color = "red"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x},{self.y})")


point = Point(1, 2)
print(point.x)
point.draw()

# class reference
print(Point.default_color)
# obj reference
print(point.default_color)

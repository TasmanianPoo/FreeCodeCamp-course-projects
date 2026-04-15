class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, new_width):
        self.width = new_width

    def set_height(self, new_height):
        self.height = new_height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def get_diagonal(self):
        return math.sqrt((self.width ** 2 + self.height ** 2))

    def get_picture(self):

        if self.width >= 50 or self.height >= 50:
            return "Too big for picture."

        picture = ""
        for dot in range(self.height):
            picture += "*" * self.width + "\n"

        return picture

    def get_amount_inside(self, other):

        return (self.width*self.height)// (other.width*other.height)

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def set_width(self, new_width):
        self.width = new_width
        self.height = new_width

    def set_height(self, new_height):
        self.height = new_height
        self.width = new_height

    def set_side(self, new_side):
        self.height = new_side
        self.width = new_side

    def __str__(self):
        return f"Square(side={self.width})"


rect = Rectangle(50, 20)
print(rect.get_amount_inside(Rectangle(2,5)))
print(rect)
print(rect.set_width(10))
print(rect)

sqr = Square(5)
print(sqr.set_width(7))
print(sqr.get_picture())
print(sqr.set_side(9))
print(sqr)





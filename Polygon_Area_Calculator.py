class Rectangle:
    def __init__(self, width, height):
        self.name = 'Rectangle'
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        area = self.width * self.height
        return area

    def get_perimeter(self):
        perimeter = 2 * self.width + 2 * self.height
        return perimeter

    def get_diagonal(self):
        diagonal = (self.width ** 2 + self.height ** 2) ** .5
        return diagonal

    def get_picture(self):
        if self.width > 50 or self.height > 50:
          return 'Too big for picture.'
        picture = ''
        for i in range(self.height):
          picture = picture + '*'*self.width + '\n'
        return picture

    def __repr__(self):
        shape = self.name + '(width=' + str(self.width) + ', '  + 'height=' + str(self.height) + ')'
        return shape

    def get_amount_inside(self, shape):
        areaOutter = self.get_area()
        areaInner = shape.get_area()
        return areaOutter // areaInner

class Square(Rectangle):
    def __init__(self, side):
        self.name = 'Square'
        self.side = side
        self.width = side
        self.height = side

    def set_side(self, side):
        self.set_width(side)
        self.set_height(side)

    def __repr__(self):
        shape = self.name + '(side=' + str(self.width) + ')'
        return shape

rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))

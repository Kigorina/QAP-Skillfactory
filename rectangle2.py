from rectangle import Rectangle, Square, Circle
#создаем два прямоугольника#
rect_1 = Rectangle(3,4)
rect_2 = Rectangle(12,5)
# вывод площади наших двух прямоугольников
print(rect_1.get_area())
print(rect_2.get_area())

square_1 = Square(5)
square_2 = Square(10)
print(square_1.get_area(),
      square_2.get_area())
#площадь круга
circle_1 = Circle(5, 3.14)
circle_2 = Circle(10, 3.14)
print(circle_1.get_area())
print(circle_2.get_area())
figures = [rect_1, rect_2, square_1, square_2, circle_1, circle_2]
for figure in figures:
    if isinstance(figure, Square):
        print(figure.get_area_square())
    else:
        print(figure.get_area())

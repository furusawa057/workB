import math


class Circle:

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        area = self.radius ** 2 * math.pi
        return area

    def perimeter(self):
        perimeter = 2 * math.pi * self.radius
        return perimeter


def main():
    circle1 = Circle(radius=1)
    print('{:.2f}'.format(circle1.area()))  # 3.14
    print('{:.2f}'.format(circle1.perimeter()))  # 6.28

    circle3 = Circle(radius=3)
    print('{:.2f}'.format(circle3.area()))
    print('{:.2f}'.format(circle3.perimeter()))


if __name__ == '__main__':
    main()

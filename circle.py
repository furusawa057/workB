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
    print(f'{circle1.area():.2f}')
    print(f'{circle1.perimeter():.2f}')

    circle3 = Circle(radius=3)
    print(f'{circle3.area():.2f}')
    print(f'{circle3.perimeter():.2f}')


if __name__ == '__main__':
    main()

import math


class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        area = float(self.height * self.width)
        print(f'{area:.2f}')

    def diagonal(self):
        diag = math.sqrt(self.height ** 2 + self.width ** 2)
        print(f'{diag:.2f}')


def main():
    rectangle1 = Rectangle(height=5, width=6)
    rectangle1.area()
    rectangle1.diagonal()

    rectangle2 = Rectangle(height=3, width=3)
    rectangle2.area()
    rectangle2.diagonal()


if __name__ == '__main__':
    main()

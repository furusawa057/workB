class MyCounterV1:
    def __init__(self, val):
        self.value = val

    def count_up(self):
        self.value += 1


def main():
    counter1 = MyCounterV1(val=0)
    print(counter1.value)

    counter1.count_up()
    print(counter1.value)

    counter1.count_up()
    print(counter1.value)

    counter2 = MyCounterV1(val=7)
    print(counter2.value)

    counter2.count_up()
    print(counter2.value)

    counter2.count_up()
    print(counter2.value)


if __name__ == '__main__':
    main()

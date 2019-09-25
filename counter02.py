class MyCounterV2:
    def __init__(self, val, step):  # 前処理とか絶対毎回やる処理を書くところ
        self.value = val
        self.step = step
        # selfをつけることでclass内全体で使える変数になる

    def count_up(self):
        self.value += self.step


def main():
    counter1 = MyCounterV2(val=0, step=1)
    print(counter1.value)

    counter1.count_up()
    print(counter1.value)

    counter1.count_up()
    print(counter1.value)

    counter2 = MyCounterV2(val=0, step=3)
    print(counter2.value)

    counter2.count_up()
    print(counter2.value)

    counter2.count_up()
    print(counter2.value)


if __name__ == '__main__':
    main()

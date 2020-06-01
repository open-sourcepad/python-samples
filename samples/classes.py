class Base:
    def __init__(self):
        self.value = 3

class Base2:
    def run(self):
        print('base 2 print')

class Child1(Base):
    def run(self):
        print(self.value)

class Child2(Base, Base2):
    def run(self):
        super().run()
        print(self.value)


if __name__ == '__main__':
    Child1().run()

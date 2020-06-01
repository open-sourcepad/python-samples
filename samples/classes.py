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

class Child3:
    def run(self):
        self.test()

    @property
    def sample_property(self):
        print("this is a property")

    @classmethod
    def test(self):
        print('tester')


if __name__ == '__main__':
    Child3().sample_property

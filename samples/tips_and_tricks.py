class Test:
    pass


def attr(self):
    print('123')

setattr(Test, 'attr', attr)

Test().attr()

setattr(Test, 'test_data', 'sample test data')

print(getattr(Test, 'test_data1', None))

kwargs = {'a': 1}
print(kwargs.get('a', None))

dir(Test)
# ipython

# class explanation
# import pry; pry()

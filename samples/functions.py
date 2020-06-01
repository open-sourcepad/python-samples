# normal functions
def func1():
    print("this is function 1")

func1()

def func2(arg):
    print(f"this is function {arg}")

func2(2)

def func3(arg='default'):
    print(f"this is function 3 with {arg}")

func3()
func3('not so default value')

# args and kwargs
def func4(*args, **kwargs):
    print(args)
    print(kwargs)

args = (1,2,3)
kwargs = {'a':1, 'b':2, 'c':24}
func4(*args, **kwargs)

def func5(kwarg1='default'):
    print(kwarg1)

kwarg = {'kwarg1': 'not so default'}

func5(**kwarg)

# returns
def func6():
    return "return value"

# lambda
func5 = lambda var : var + 1
print(func5(1))

func6 =  lambda var1, var2 : var1 + var2
print(func6(2,8))

#*args:接受N个位置参数，转换成元组
def func1(*args):
    print(*args)

#**kwargs:接受N个关键字参数 转换车工字典的方式
def func2(name,age,**kwargs):
    print(name)
    print(age)
    print(kwargs)

func1(2,3)
func2('Songsa',18,hobby="game")

def test(name,age,*args,**kwargs):
    print(name)
    print(age)
    print(args)
    print(kwargs)
    logger("test2")

def logger(source):
     print("Test....%s" %source)

test('Songsa',age=27,sex='m',hobby="BMW")
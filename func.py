import time
time_format = '%Y-%m-%d %X'
time_current = time.strftime(time_format)
#函数
def func1():
    '''test1'''
    print("in the func1")
    print(time_current)
    return 0

#过程
def func2():
    '''test2'''
    print("in the func2...")
    print(time_current)

x = func1() #函数调用
y = func2()#过程调用
print(x,y)

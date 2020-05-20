# 、封装一个函数(无参，有返回值)：
# a.如果不是数字：则直接返回“不是数字，请重新输入”
# b.判断用户输入是否是数字，
#       如果是数字：则继续判断,输入数字是否是9的倍数
# I.如果是，返回结果“是”，
# II.否则返回结果“否”
def func():
    i = input('请输入数字:')
    if i is type(1):
        print('不是数字,请重新输入')
        return
    print('输入数字就对了')


def func_1():
    i = input('请输入数字:')
    if i is type(1):
        if i % 9 == 0:
            print('是')
        else:
            print('否')


func()
print(type(1))

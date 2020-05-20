# b.重新创建一个demo.py文件，引入tools模块，然后定义一个Dog类，
# 继承Animal，重写里面的eat()，在原有基础上（”狗吃骨头”）,
# 添加打印内容“吃完骨头瑶瑶头...”
import tools


class Animal:
    __age = 0
    type = "狗"

    def __init__(self, name):
        self.name = name

    def eat(self):
        print(tools)


class Dog(Animal):
    def eat(self):
        print('吃完骨头摇摇头')

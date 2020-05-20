# 20、带入random模块,生成1-100间所有整数的随机列表(列表中的数字不重复,长度为100)
import random
list = []
for i in range(101):
    list.append(random.randint(1,100))
print(list)
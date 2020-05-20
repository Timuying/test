# 编写一个函数，求1到100之间的奇数和？
i = 0
b = 0
while i <= 100:
    if i % 2 == 0:
        print('i:', i)
        b += i
    i += 1
print('奇数和:', b)
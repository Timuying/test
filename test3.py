# 使用while循环输出九九乘法表
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print(f'{i}*{j}={i*j}\t', end='')
        j += 1

    print()
    i += 1

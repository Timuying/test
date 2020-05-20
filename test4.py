# 18、通过循环创建十个文件，命名为1.txt，2.txt，3.txt....
#  然后将文件名修改为：副本1.txt，副本2.txt，副本3.txt..
import os


def some_file():
    os.mkdir('file')
    os.chdir('./file')
    i = 0
    while i <= 10:
        file = open('text' + str(i), 'w', encoding='utf-8')
        file.close()
        i += 1


def new_file():
    file_list = os.listdir()
    for name in file_list:
        os.rename(name, 'hello' + name)


some_file()
new_file()

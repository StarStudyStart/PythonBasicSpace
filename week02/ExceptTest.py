#ExceptTest
try:
    num = eval(input('请输入一个整数：'))
    print(num**2)
except NameError:
    print('输入不是整数，请重新运行程序')

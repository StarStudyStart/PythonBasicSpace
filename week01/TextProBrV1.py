#TextProBar.py
import time
scale = 10
print("执行开始".center(scale//2,'-'))
start = time.perf_counter()
for i in range(scale+1):
    a = '*'*i
    b = '.'* (scale - i)
    c = (i/scale)*100
    dur = time.perf_counter()
    print("\r{:^3.0f}%[{}->{}]".format(c,a,b),end = '')
    time.sleep(0.5)
print("\n"+"执行结束".center(scale//2,'-'))

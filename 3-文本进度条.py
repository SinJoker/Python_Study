"""
这是逐行刷新，也可以使用动态单行刷新
刷新的本质是新的一行覆盖掉旧行，又两个关键控制环节：
（1)不能换行：print()需要被控制；
（2）回退：打印后光标退回到之前的位置，使用\r完成
"""
import time
scale = 100
print("执行开始".center(scale//2, "-"))
start_time = time.perf_counter()
for i in range(scale + 1):
    time.sleep(0.1)
    a = '*' * i
    b = '.' * (scale-i)
    c = (i/scale) * 100
    # 这里的c是显示进度数据的核心数据，可以对其修正，产生不同的进度效果，具体可通过函数的方式进行，即d=f(c)，从而让其再一定时间里变得更快或者更慢
    dur = time.perf_counter() - start_time
    print("\r{:^3.0f}%[{}->{}] {:.2f}s".format(c, a, b, dur), end="")
    # print函数每次运行后会默认再最后增加换行符，这里使用end=“”可以修改增加的
print("\n"+"执行完成".center(scale//2, "-"))

from random import random
from time import perf_counter
"""
圆周率的计算
    -公式法
    pi= sigma[0,无穷]{[(4/(8k+1)-2/(8k+4)-1/(8k+5)-1/(8k+6))]/16^k}
    -蒙特卡罗方法
        pi=圆面积/外切正方形的面积，通过撒点的方法，用点的数量代替面积
"""
# 公式法
pi = 0
n = 200
for k in range(n):
    pi += (
            4/(8*k+1)
            - 2/(8*k+4)
            - 1/(8*k+5)
            - 1/(8*k+6)
          )\
          / pow(16, k)
#     想要代码换行，使用反斜杠
print("循环{0}次后，圆周率的计算结果为{1}".format(n, pi))

# 蒙特卡罗方法
darts = 1000*1000
hits = 0.0
start_time = perf_counter()
for i in range(1, darts+1):
    x, y = random(), random()
    distance = pow(pow(x, 2)+pow(y, 2), 0.5)
    if distance <= 1:
        hits += 1
pi = 4 * (hits/darts)
print("圆周率的数值为：{}".format(pi))
print("计算时间为:{:.5f}s".format(perf_counter()-start_time))
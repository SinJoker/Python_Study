"""
time库的引用及使用

time的引用: import time
time函数的种类：
（1）时间获取：time(),ctime(),gmtime()
（2）时间格式化：strftime(),strptime()
（3）程序计时：sleep(),perf_counter()

（1）时间获取：time(),ctime(),gmtime()
    time()使用，time.time()，返回浮点数
    ctime()使用，time.ctime()，返回可读字符串
    gmtime()使用，time.gmtime()，返回其他程序可以利用的的时间

（2）时间格式化：strftime(),strptime()
    strftime(tpl,ts),具体见实例
    其中%后可加很多：
    Y-m-d-H-M-S等等

    strptime(),字符串转换为时间格式，见实例

（3）程序计时：sleep(),perf_counter()测量程序开始结束的时间
    测量时间：perf_counter()以ns为单位进行计时；
    产生时间：
"""

import time

start_time = time.perf_counter()
print("开始计时")
print("（1）时间获取：time(),ctime(),gmtime()")
print(time.time())
print(time.ctime())
print(time.gmtime())

print("（2）时间格式化：strftime(),strptime()")
print(time.strftime("%Y年%m月%d日%H时%M分%S秒", time.gmtime()))
print(time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()))
print(time.strftime("%Y-%m-%d %H:%M:%S 星期%A", time.gmtime()))
print("字符串转换为时间格式")
timestring = '2018-12-26 11:10:26'
print(time.strptime(timestring, "%Y-%m-%d %H:%M:%S"))

print("（3）程序计时：sleep(),perf_counter()")
print("休眠开始")
time.sleep(5)
print("休眠结束")
# 开始时间在程序开始，语句为：start_time = time.perf_counter()
end_time = time.perf_counter()
print("计时结束", end_time - start_time)

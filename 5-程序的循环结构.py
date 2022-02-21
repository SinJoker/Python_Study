"""
程序的循环结构
（1）遍历循环 for
（2）无限循环 while
（3）循环控制保留字
（4）循环高级用法

（1）遍历循环
    1）语法
    for 循环变量 in 遍历结构：
        语句
    2）类型
        1 计数循环
            for i in range(n):
                语句
                # 产生案例1 ······························
        2 特定次数循环
            for i in range(m,n,k)
                语句
            其中k可以省略，省略时步长为1
                # 产生案例2 ······························
        3 字符串循环
            for c in “字符串”
                语句
            其中c可以被替换，但常用c
                # 产生案例3 ······························
        4 列表遍历循环
            for item in [ls]:
                语句
            其中ls为一个列表,格式为[a,b,c]
                # 产生案例4 ······························
        5 文件遍历循环
            for line in fi：
                语句
            其中fi为文件标识符，可以理解为一个文件
            后续学习，暂未介绍，不产生案例

（2） 无限循环
    当满足条件后才会停止
    产生案例5.1与5.2 ·····································

（3）循环控制保留字
    说明：用于控制循环过程的保留字符。共两个：break,continue
    break：跳出并结束当个循环，执行循环之后的语句；
    continue：结束当次的循环，进行下一次循环，可以理解为小break；
    1)单层循环
        产生案例6 ·······································
    2）多层循环
        产生案例7 ·······································

(4) 循环的高级用法
    循环与else组合,可以理解为对没有break的一种奖励,遇到continue都可以运行。
    在以上循环后+else，如：
    for i in range(n)：
        line1
    else：
        line2

    while 条件:
        line3
    else:
        line4
    产生案例8.1和8.2 ···········································
"""

# 案例1
for i in range(5):
    print("hello:", i)

# 案例2
for i in range(0, 50, 2):
    print("hello:", i)

# 案例3
for c in "Python":
    print(c)
for c in "Python":
    print(c, end=",")

# 案例4
for item in ["hello", "world", 123]:
    print(item, end=",")

# 案例5.1
a = 30
while a > 0:
    a -= 1
    print(a)

# 案例5.2
# a = 30
# while a > 0:
#     a += 1
#     print(a)

# 案例6
for c in "Python is good!":
    if c == "t":
        continue
    print(c, end="")

for c in "Python is good!":
    if c == "t":
        break
    print(c, end="")

# 案例7
s = "Python"
while s != "":  #第一层循环
    for c in s:  #第二层循环
        print(c, end=",")
    s = s[:-1]  # 字符串切片，去掉一个字符串

s = "Python"
while s != "":  # 第一层循环
    for c in s:  # 第二层循环
        if c == "t":
            break
        print(c, end=",")
    s = s[:-1]  # 字符串切片，去掉一个字符串

# 案例8.1
for c in "Python":
    if c == "t":
        continue
    print(c, end="")
else:
    print("正常退出！")

# 案例8.2
for c in "Python":
    if c == "t":
        break
    print(c, end="")
else:
    print("正常退出！")

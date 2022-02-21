"""
程序的分支结构
    根据判断条件结果，选择不同向前路径的运行方式。
    （1）单分支结构
    （2）二分支结构
    （3）多分支结构
    （4）条件判断及组合
    （5）程序的异常处理

（1）单分支结构
    例如if结构
（2）二分支结构
    如if else结构
    tips：可以使用紧凑形式
（3）多分支结构
    如if、elif、else
（4）条件判断及组合
    1）使用操作符进行判断：>、>=、<、<=、==、!=
    2）使用保留字进行判断：and、or、not
（5）程序的异常处理
    异常处理使用两个保留字：try、except，具体使用方法：
    try:
        语句1
    except：
        语句2
实例见代码，在之后还有
    else：
        语句3  在不发生异常时执行
    finally：
        语句4  一定会执行
"""

# （1）单分支结构
guess = eval(input())
if guess == 99:
    print("猜对了")

# （2-1）二分支结构
guess = eval(input())
if guess == 99:
    print("猜对了")
else:
    print("猜错了")
# （2-2）紧凑形式
guess = eval(input())
print("猜{}了".format("对"if guess == 99 else "错"))

# （3）多分支结构
score = eval(input())
grade = ""
if score >= 60:
    grade = "D"
elif score >= 70:
    grade = "C"
elif score >= 80:
    grade = "B"
elif score >= 90:
    grade = "A"
print("输入成绩为{}级别".format(grade))

# （4）条件判断及组合
guess = eval(input())
if guess > 99 or guess < 99:
    print("猜错了")
else:
    print("猜对了")

# （4）程序异常处理
num = eval(input("请输入一个整数："))
print(num*2)
# 异常处理的地方在于，如果用户没有输入整数，怎么处理
try:
    num = eval(input("请输入一个整数："))
    print(num**2)
except NameError:  # NameError为异常类型，
    print("输入不是整数！")

# 实例5，身体质量指数BMI=体重（kg)/身高^2（m^2)
# 如果BMI<18.5,则偏瘦；
# 18.5<BMI<24，则正常；
# 24<BMI<28，则偏胖；
# 如果BMI≥28,则肥胖；
# 双输入、双输出


height, weight = eval(input("请输入升高（m）体重（kg），请使用逗号（英文）隔开。"))
BMI = weight/pow(height, 2)
print("这人的BMI指数位{:.2f}". format(BMI))
# format前面使用.而不是，需要注意
who, nat = "", ""
if BMI < 18.5:
    who, nat = "偏瘦", "偏瘦"
elif 18.5 <= BMI < 24:
    who, nat = "正常", "正常"
elif 24 <= BMI < 25:
    who, nat = "正常", "偏胖"
elif 25 <= BMI < 28:
    who, nat = "偏胖", "偏胖"
elif 28 <= BMI < 30:
    who, nat = "偏胖", "肥胖"
else:
    who, nat = "肥胖", "肥胖"
print("BMI的国际、国内指标评价结果分别为：{0},{1}". format(who, nat))
# format前面使用.而不是，需要注意

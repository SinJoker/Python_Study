# 基本统计值，对一组数据的基本理解，例如平均值，最大最小值等等
"""
总个数：len()
求和：循环语句
平均值：求和/个数
方差：
中位数：排序
"""


# 定义函数，获得用户的每个输入，循环获得用户输入
def getnum():
    nums = []
    iNumStr = input("请输入数字（回车退出）：")
    while iNumStr != "":
        nums.append(eval(iNumStr))
        iNumStr = input("请输入数字（回车退出）：")
    return nums


# 平均值函数
def mean(numbers):
    s = 0.0
    for num in numbers:
        s = s + num
    return s/len(numbers)


# 方差函数
def dev(numbers, mean):
    sdev = 0.0
    for num in numbers:
        sdev = sdev + pow(num-mean, 2)
    return pow(sdev/(len(numbers)-1), 0.5)


# 中位数函数
def median(numbers):
    sorted(numbers)
    size = len(numbers)
    if size % 2 == 0:
        med = (numbers[size//2-1]+numbers[size//2])/2  # 整除
    else:
        med = numbers[size//2]
    return med


n = getnum()
m = mean(n)
print("平均值：{}，方差：{:.2}，中位数：{}".format(m, dev(n, m), median(n)))

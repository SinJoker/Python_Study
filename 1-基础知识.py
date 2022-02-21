"""可以说明么"""
"""
字符串切片的高级用法[M:N] [M:N:K]其中MN可以缺省，M缺省表示从开头，N缺省表示从结尾。
<字符串>[M:N]
<字符串>[M:N:K]其中K表示步长。距离如下：
“零一二三四五六七八”的[1:8:2]的输出结果就为一三五七
逆序字符串可以使用[::-1]的方式进行，表示步长为-1，即，从后向前。
转义符为\
"""
WeekStr = "一二三四五六七"
Str = eval(input("请输入今天星期几的数字（1-7）："))
print("星期"+WeekStr[Str-1])
"""字符串类型有：len(x)、str(x)、hex(x)、oct(x)、chr(x)、ord(x)
len(x)：返回字符串长度；
str(x)：将字符转换为字符串；
hex(x)：将字符转换为16进制；
oct(x)：将字符转换为8进制；
chr(u)：将Unicode编码转换为字符；
ord(x)：获得该字符的Unicode编码。
Unicode编码：统一字符编码，将世界上所有符号放进一个库中，从0-111411，每个编码对应一个字符。
Python使用的Unicode编码进行编程。
"""
# 星座编程,可以输出星座形状
for i in range(12):
    print(chr(9800+i), end="")

# 字符串处理方法

'''
str.lower() and str.upper()可改变字符大小写；
str.split(x)拆解字符串，其中x为拆解字符；若字符串里包含，则使用拆解字符将字符串拆解；
str.count(“y”)计数函数，计量str字符串里含有y的次数；
str.replace(old,new)替换函数；
str.center(width,fill_char),格式函数，比如“Python”.center(20,"=")，就会输出=======center====这样的
str.strip(chars)去掉在chars中列出的，左侧右侧的字符；
str.join(iter)在除str最后一个字符外的每一个字符后面加上iter，用于字符串分割。
'''

# 字符串格式化
'''
.format()
槽，在字符串之间使用，作为容器，例子：
”{number1：格式控制标记1}：计算机{number2：格式控制标记2}的CPU占用率为{number3：格式控制标记3}%“.format("2022-01-27","C",10)
number1、number2、number3，从0开始，可以为空，为空顺序按正常顺序，不为空时按照数字顺序；
格式控制标记有6中，分别为：
空：无特殊作用；
<>^分别为靠左靠右剧中；

'''
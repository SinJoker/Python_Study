# 组合数据类型：集合类型、序列类型（元组+列表）、字典类型

"""
(1)集合类型及操作
(2)集合操作符
(3)集合处理方法
(4)集合类型应用场景

(1)集合类型及操作
    0）集合与数学概念一致
    1）集合内不存在相同元素
    2）集合内元素不能改变（整数、浮点数、字符串等都是不可变的）
    3）集合是多个元素的无需组合
    4）集合用大括号{}表示，元素间用逗号分隔
    5）建立集合类型用{}或者set（）

(2)集合操作符
    1）运算操作符
        [S | T]为并集
        [S - T]为差集
        [S & T]为交集
        [S ^ T]为补集，两个集合中的非相同元素
    2）关系操作符
        另还有> >= = <= <关系操作符，返回true或者false
    3）增强操作符
        [S |= T] 更新S，更新内容是[S | T]
        其他增强同上

(3)集合处理方法
    1）S.add(x)  # 增加x
    2）S.discard(x)  # 减少x
    3）S.remove(x)  # 减少x，S没有x就报错（KeyError异常）
    4）S.clear(x)  # 清空
    5）S.pop(x)  # 随机返回一个元素，没有就报错（KeyError异常）
    6）S。copy()  # 复制S
    7）len(S)  # 返回S元素的个数
    8）x in S  # 判断x是不是在S里面，返回True或者False
    9）x not in S  # 判断x是不是在S里面，返回True或者False
    10）set(x)  # 把变量类型x转变为集合类型

(4)集合类型应用场景
    1)包含关系的比较
    2）数据去重。利用集合不重复的特点，最典型的运用场景


"""

# (1)集合类型及操作
A = {"Python", 123, ("Python", 123)}  # ()为元组

B = set("pypy123")  # 使用set（）建立函数，里面每个字符用逗号隔开,重复的数据被删除
print(B)

# (2)集合操作符
C = {"p", "y", 123}
D = set("pypy123")
print(C-D, D-C)

# (3)集合处理方法
E = {"p", "y", 123}
for item in A:
    print(item, end="")

try:
    while True:
        print(E.pop(), end="")
except:
    pass

# (4)集合类型应用场景
ls = ["p", "p", "y", "y", 123]
s = set(ls)  # 数据一步去重，但是列表类型 → 集合类型
lt = list(s)  # 数据类型转变list函数，集合类型 → 列表类型



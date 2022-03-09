"""
文本词频统计
需求：一篇文章，出现了哪些词，哪些词出现的最多
其他条件：中文文本与英文文本都可能存在。
"""
import jieba


# 1-英文词频统计，开始
def get_text():
    txt = open("Resurrection - Leo Tolstoy.txt", "r", encoding='UTF-8').read()
    txt = txt.lower()
    for ch in '|"!@#$%^&*+-[]{}~.,()':
        txt = txt.replace(ch, " ")
    return txt
# 归一化处理，将所有的大写字母变小写，将特殊字符全部转换为空格。
# 此段代码只支持读取相同文件夹下的文件。


ResurrectionTxt = get_text()
words = ResurrectionTxt.split()
# split将文本转化为列表，方便处理
counts = {}
# word为列表类型，counts为字典类型

for word in words:
    counts[word] = counts.get(word, 0) + 1
# 遍历、计数过程

items = list(counts. items())
# 将字典类型转换为列表类型
items.sort(key=lambda x: x[1], reverse=True)
#  列表的sort方法

for i in range(10):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word, count))
# 打印出前10出现率的单词
# 1-英文词频统计，结束

# 2-中文词频统计，开始
txt = open("三国演义.txt", "r", encoding="utf-8").read()
words = jieba.lcut(txt)
# 转换为列表
counts = {}
for word in words:
    if len(word) == 1:
        continue
    else:
        counts[word] = counts.get(word, 0) + 1
# 过滤掉一些介词，单字并完成统计结果

items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)
for i in range(15):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word, count))
print("11111111")
counts.clear()
# 2-中文词频统计，结束

# 3-中文词频统计-优化，开始
txt = open("三国演义.txt", "r", encoding="utf-8").read()
excludes = {"将军", "却说", "荆州", "二人", "不可", "不能", "如此", "如何", "左右",
            "军士", "商议", "军马", "引兵", "次日", "大喜","主公", "天下", "东吴",
            "于是", "今日", "不敢", "魏兵", "陛下", "人马"}
# 建立排除词库
words = jieba.lcut(txt)
# 转换为列表
counts = {}
for word in words:
    if len(word) == 1:
        continue
    elif word == "诸葛亮" or word == "孔明曰":
        r_word = "孔明"
    elif word == "关公" or word == "云长":
        r_word = "关羽"
    elif word == "玄德" or word == "玄德曰":
        r_word = "刘备"
    elif word == "孟德" or word == "丞相曰" or word == "丞相":
        r_word = "曹操"
    elif word == "都督" or word == "大都督" or word == "瑜" or word == "公瑾":
        r_word = "周瑜"
    else:
        r_word = word
    counts[r_word] = counts.get(r_word, 0) + 1
for word in excludes:
    del counts[word]
# 过滤掉一些介词，单字并完成统计结果
items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)
for i in range(10):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word, count))
# 3-中文词频统计-优化，结束

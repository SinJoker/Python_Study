"""
-中文文本需要通过分词获得单个的词语；
-jieba是优秀的中文分词第三方库，需要额外安装；
-jieba库提供三种分词模式，最简单只需要掌握一个函数。
"""

import jieba

jieba.add_word("曹曹")
print_text1 = jieba.lcut("不得不说，曹曹是一个可爱的女孩子")  # 一般模式
print_text2 = jieba.lcut("不得不说，曹曹是一个可爱的女孩子", cut_all=True)  # 全模式
print_text3 = jieba.lcut_for_search("春风不解风情，你我若只如初见")  # 搜索引擎模式

print("一般模式:", print_text1)
print("全模式:", print_text2)
print("搜索引擎模式:", print_text3)

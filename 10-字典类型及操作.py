# 字典类型定义(dictionary)

"""
(1)理解映射的概念
字典：数据组织与表达的新的形态

(2)定义（中英文输入法切换太麻烦了，后面尝试用英文直接写）
use {} or dict()to define a dict，for example:
{key1:value1,key2:value2...}

(3)kind and usage of dictionary
dict_variant = {key1:value1,key2:value2}
or
value1 = dict_variant{key1}
or
dict_variant{key1} = value
some kinds of valuation about dictionary
symbol [] is used to add element to a dictionary
more details in case1

(4)Definition and methods of dictionary handler functions.
functions:
    1) del d[k]    delete the corresponding value of index k.
    2) k in d   to judge k in dictionary d or not.
    3) d.keys()    it will give all keys in d
    4) d.values()  will give all values in d
    5) d.items()   will give all of key_value_couples in d.
    more details in case2
methods:
    1) d.get(k,default)    feedback the value of key if k in d, otherwise do nothing.
    2) d.pop(k,default)    feedback and remove the value of key if k in d, otherwise do nothing.
    3) d.popitem()   feedback a key_value_couple randomly by the form of tuple(元组).
    4) d.clear  to clear this dictionary.
    5) len(d)   feedback length of this dictionary.
    more details in case3

(5)Scenarios(应用场景)
Main scenarios: Expression of Mapping(映射)
"""
# case1
case1 = {"China": "BeiJing", "American": "Washington"}  # try to feedback the capital of country that we write.
print_text1 = case1["China"]
print(print_text1)  # try to run it here, ok, it can run successfully.

# case2
case2 = {"China": "BeiJing", "American": "Washington"}  # same to dictionary case1 in case1
print_text2 = "BeiJing" in case2  # example of function 2)
print(print_text2)  # try to run it here, ok, it can run successfully.
case2.keys()  # example of function 3)
case2.values()  # example of function 4)
case2.items()  # example of function 5)

# case3
case3 = {"China": "BeiJing", "American": "Washington"}  # same to dictionary case1 in case1
print_text3 = case3.get("China", "The key you write is not in this dictionary.")
# Python will give BeiJing.
print_text4 = case3.get("India", "The key you write is not in this dictionary.")
# Python can not find India,so it will print <default> line.
print_text5 = case3.popitem()
print(print_text3, print_text4, print_text5)  # try to run it here, ok, it can run successfully.

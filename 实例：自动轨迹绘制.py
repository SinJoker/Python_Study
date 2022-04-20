"""
Draw graphs by script file.
Mind map:
use turtle
(1) Define interface between data and program.
    a,b,c,d,e,f
    a: distance of run forward.
    b:direction of turn around (0 or 1), 0 means left, 1 means right.
    c:degree of turn around.
    d,e,f: 3 channels of RGB color expression(float 0~1).
(2) programing.
(3) Preparation of data file.

"""
import turtle as t

t.title("自动轨迹绘制")
t.setup(800, 600, 0, 0)
t.pencolor("red")
t.pensize(5)
# fundamental preparation

data_list = []
f = open("实例：自动轨迹绘制-数据参数文件.txt")
for line in f:
    line = line.replace("\n","")
    data_list.append(list(map(eval, line.split(","))))
    # split string to single element by line.split function
    # map(function_name, function's object). python's official function, no need import
    # eval. remove " symbol in string
f.close()

for i in range(len(data_list)):
    t.pencolor(data_list[i][3], data_list[i][4], data_list[i][5])
    t.fd(data_list[i][0])
    if data_list[i][1]:
        t.right(data_list[i][2])
    else:
        t.left(data_list[i][2])


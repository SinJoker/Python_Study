# 如数码闹钟上的那种，交通灯等
"""
步骤：
（1）绘制单个数字对应的数码管
（2）获得一串数字，绘制对应的数码管
（3）获得当前系统时间，绘制对应的数码管
"""

# （1）绘制单个数字对应的数码管

import turtle
import time


def draw_gap():
    turtle.penup()
    turtle.fd(10)


def draw_line(draw):  # 绘制单条数码管，其中draw控制海龟在移动过程中是否绘制线条
    draw_gap()
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(50)
    draw_gap()
    turtle.right(90)


def draw_digit(digit):  # 绘制七条线
    draw_line(True) if digit in [2, 3, 4, 5, 6, 8, 9] else draw_line(False)
    draw_line(True) if digit in [0, 1, 3, 4, 5, 6, 7, 8, 9] else draw_line(False)
    draw_line(True) if digit in [0, 2, 3, 5, 6, 8, 9] else draw_line(False)
    draw_line(True) if digit in [0, 2, 6, 8] else draw_line(False)
    turtle.left(90)
    draw_line(True) if digit in [0, 4, 5, 6, 8, 9] else draw_line(False)
    draw_line(True) if digit in [0, 2, 3, 5, 6, 7, 8, 9] else draw_line(False)
    draw_line(True) if digit in [0, 1, 2, 3, 4, 7, 8, 9] else draw_line(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(20)


def draw_date(date):  # 打印给出的一个日期字符串,date的形式为'%Y-%m=%d+'
    turtle.color("red")
    for i in date:
        if i == '-':
            turtle.write('年', font=("Arial", 18, "normal"))
            turtle.pencolor("green")
            turtle.fd(40)
        elif i == '=':
            turtle.write('月', font=("Arial", 18, "normal"))
            turtle.pencolor("blue")
            turtle.fd(40)
        elif i == '+':
            turtle.write('日', font=("Arial", 18, "normal"))
            turtle.fd(40)
        else:
            draw_digit(eval(i))


def main():
    turtle.setup(1000, 350, 200, 200)
    turtle.penup()
    turtle.fd(-420)
    turtle.pensize(10)
    draw_date(time.strftime('%Y-%m=%d+', time.gmtime()))
    turtle.hideturtle()
    turtle.done()


main()

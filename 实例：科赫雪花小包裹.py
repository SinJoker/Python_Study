# 介绍一种曲线，科赫曲线，是一种具有迭代关系的几何图形
# 雪花的边缘与雪花整体具有一定的相似性
# 用同一个操作，对一条曲线进行不断的迭代

# 递归+turtle

import turtle


def koch(size, n):
    if n == 0:
        turtle.fd(size)
    else:
        for angle in [0, 60, -120, 60]:
            turtle.left(angle)
            koch(size/3, n-1)  # 这里自己利用自己，实质上是递归思想


def main():
    turtle.setup(600, 600)
    turtle.penup()
    turtle.goto(-200, 100)
    turtle.pendown()
    turtle.pensize(2)

    level = 3

    koch(400, level)
    turtle.right(120)
    koch(400, level)
    turtle.right(120)
    koch(400, level)
    turtle.right(120)

    turtle.hideturtle()

main()

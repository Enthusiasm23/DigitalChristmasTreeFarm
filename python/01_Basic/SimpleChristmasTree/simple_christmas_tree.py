#!/usr/bin/env python
# -*- coding: utf-8 -*-
import turtle


def draw_star(n):
    """
    在圣诞树顶部绘制一个五角星。

    :param n 控制圣诞树大小的变量
    """
    turtle.color("orange", "yellow")
    for i in range(5):
        turtle.forward(n / 5)
        turtle.right(144)
        turtle.forward(n / 5)
        turtle.left(72)
        turtle.end_fill()


def draw_tree(d, s):
    """
    绘制分形圣诞树的函数。

    :param d: 递归的深度。
    :param s: 树枝的长度。
    """
    if d <= 0:
        return
    turtle.forward(s)
    draw_tree(d - 1, s * .8)
    turtle.right(120)
    draw_tree(d - 3, s * .5)
    turtle.right(120)
    draw_tree(d - 3, s * .5)
    turtle.right(120)
    turtle.backward(s)


def write_text(n):
    """
    在圣诞树下方写上祝福的文字。

    :param n 控制圣诞树整体大小的变量
    """
    turtle.penup()
    turtle.backward(n / 1.5)
    turtle.pendown()
    turtle.color("orange")
    turtle.write("Merry Christmas", align="center", font=("Comic Sans MS", 40, "bold"))


def main():
    # 设置窗口大小并将窗口居中
    turtle.setup(width=700, height=700, startx=None, starty=None)
    # 设置圣诞树大小的变量
    n = 100
    # 设置turtle模块的绘画速度为最快
    turtle.speed('fastest')
    # 使海龟（turtle）面朝上方，即默认方向（北）
    turtle.left(90)
    # 向前移动海龟，以定位到圣诞树的顶部位置
    turtle.forward(2.5 * n)
    # 调整海龟的朝向以便开始绘制星星
    turtle.left(126)
    # 调用函数绘制星星
    draw_star(n)
    # 将海龟方向调整回以便开始绘制圣诞树
    turtle.right(126)
    # 设置绘制圣诞树的颜色
    turtle.color("dark green")
    # 向后移动海龟，到达圣诞树的开始绘制位置
    turtle.backward(n * 4.8)
    # 调用函数绘制圣诞树
    draw_tree(15, n)
    # 调用函数写下祝福的文字
    write_text(n)
    # 隐藏海龟的箭头，完成绘图后不显示箭头
    turtle.hideturtle()
    # 结束turtle绘图
    turtle.done()


if __name__ == '__main__':
    main()

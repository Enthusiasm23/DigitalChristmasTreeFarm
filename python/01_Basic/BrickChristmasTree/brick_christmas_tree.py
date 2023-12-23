#!/usr/bin/env python
# -*- coding: utf-8 -*-
import turtle


def setup_screen(title, width, height):
    """设置画布的标题、宽度和高度。"""
    screen = turtle.Screen()
    screen.setup(width, height)
    screen.title(title)
    return screen


def create_turtle(shape, color):
    """创建并返回一个指定形状和颜色的turtle。"""
    t = turtle.Turtle()
    t.shape(shape)
    t.color(color)
    t.speed('fastest')
    t.penup()
    return t


def stamp_at_positions(t, positions, color):
    """在一系列位置上用指定颜色盖章。"""
    t.color(color)
    for pos in positions:
        t.goto(pos)
        t.stamp()


def write_greetings(message, y_pos):
    """在指定位置写下祝福的话。"""
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.color('black')
    pen.penup()
    pen.goto(0, y_pos)
    pen.write(message, align="center", font=("Arial", 23, "bold"))


def draw_tree():
    """绘制整个圣诞树，包括树干、树叶和装饰。"""
    # 创建画布
    screen = setup_screen("Brick Christmas Tree", 500, 600)

    # 初始化圆形和矩形turtle
    circle = create_turtle('circle', 'red')
    square = create_turtle('square', 'green')

    # 绘制树顶装饰
    circle.goto(0, 180)
    circle.stamp()

    # 绘制树叶和装饰
    k = 0  # 初始化装饰间隔变量
    for i in range(1, 13):
        y = 180 - (22 * i)
        positions = [(x, y) for j in range(i - k) for x in (-22 * j, 22 * j)]
        stamp_at_positions(square, positions, 'green')  # 绘制树叶

        # 每三层添加一个装饰
        if i % 4 == 3:
            ornament_positions = [(-22 * (i - k), y), (22 * (i - k), y)]
            stamp_at_positions(circle, ornament_positions, 'yellow')

        # 每四层添加顶部的装饰
        if i % 4 == 0:
            ornament_positions = [(-22 * (i - k), y), (22 * (i - k), y)]
            stamp_at_positions(circle, ornament_positions, 'red')
            k += 2  # 更新装饰间隔

    # 绘制树干
    trunk_positions = [(x, 180 - (22 * i)) for i in range(13, 17) for x in (-22, 0, 22)]
    stamp_at_positions(square, trunk_positions, 'brown')

    # 添加文字祝福
    write_greetings("Merry Christmas", -230)

    # 保存矢量图形EPS文件（Encapsulated PostScript）
    canvas = turtle.getcanvas()
    canvas.postscript(file="brick_christmas_tree.eps")

    # 结束绘图
    turtle.mainloop()


if __name__ == '__main__':
    draw_tree()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import turtle as t
import random as r


def draw_star(n):
    """
    绘制树顶的五角星。
    """
    t.color("orange", "yellow")
    t.begin_fill()
    t.left(126)

    for i in range(5):
        t.forward(n / 5)
        t.right(144)
        t.forward(n / 5)
        t.left(72)
    t.end_fill()
    t.right(126)


def draw_light():
    """
    随机在树上绘制彩灯。
    """
    if r.randint(0, 30) == 0:
        t.color('tomato')
        t.circle(6)
    elif r.randint(0, 30) == 1:
        t.color('orange')
        t.circle(3)
    else:
        t.color('dark green')


def tree(d, s):
    """
    递归绘制圣诞树的树枝。

    :param d: 递归的深度。
    :param s: 树枝的长度。
    """
    if d <= 0:
        return
    t.forward(s)
    tree(d - 1, s * .8)
    t.right(120)
    tree(d - 3, s * .5)
    draw_light()
    t.right(120)
    tree(d - 3, s * .5)
    t.right(120)
    t.backward(s)


def draw_decoration():
    """
    在圣诞树底部绘制装饰。
    """
    for i in range(200):
        a = 200 * 1.2 - 400 * 1.2 * r.random()
        b = 10 * 1.2 - 20 * 1.2 * r.random()
        t.up()
        t.forward(b)
        t.left(90)
        t.forward(a)
        t.down()
        if r.randint(0, 1) == 0:
            t.color('tomato')
        else:
            t.color('wheat')
        t.circle(2)
        t.up()
        t.backward(a)
        t.right(90)
        t.backward(b)


def write_text():
    """
    在屏幕上写下祝福的文字。
    """
    t.color("dark red", "red")
    t.write("Merry Christmas", align="center", font=("Comic Sans MS", 40, "bold"))


def draw_snow():
    """
    在屏幕上随机绘制雪花。
    """
    t.ht()
    t.pensize(2)
    for i in range(150):
        t.pencolor("white")
        t.pu()
        t.setx(r.randint(-350, 350))
        t.sety(r.randint(-100, 350))
        t.pd()
        dens = 6
        snow_size = r.randint(1, 10)
        for j in range(dens):
            t.fd(int(snow_size))
            t.backward(int(snow_size))
            t.right(int(360 / dens))


def main():
    screen = t.Screen()
    screen.setup(800, 800)
    screen.title('Merry Christmas')
    n = 100.0
    t.speed("fastest")
    t.pensize(4)
    t.screensize(bg="black")
    t.left(90)
    t.forward(3 * n)
    draw_star(n)
    t.color("dark green")
    t.backward(n * 4.8)
    tree(15, n)
    t.backward(n / 2)
    draw_decoration()
    write_text()
    draw_snow()
    t.done()


if __name__ == '__main__':
    main()

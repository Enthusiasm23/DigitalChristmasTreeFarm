#!/usr/bin/env python
# -*- coding: utf-8 -*-
import turtle as t

t.setup(500, 550)  # 页面大小
t.bgcolor('black')  # 背景颜色
t.speed(0)  # 画图速度
t.pencolor("green")  # 画笔颜色
t.pensize(10)  # 画笔大小
t.penup()  # 提笔
t.hideturtle()  # 隐藏画笔指针
t.goto(0, 150)  # 移动
t.showturtle()  # 显示画笔指针
t.pendown()  # 重新显示
t.shape(name="classic")  # 设置默认经典箭头形状

# 第一层树叶
t.seth(-120)  # 移动方向
for i in range(10):
    t.fd(12)  # 移动指定距离
    t.right(2)  # 向右转动指定角度
t.penup()
t.goto(0, 150)

t.seth(-60)
t.pendown()
for i in range(10):
    t.fd(12)
    t.left(2)  # 向左转动指定角度

t.seth(-150)
t.penup()
t.fd(10)
t.pendown()
for i in range(5):
    t.fd(10)
    t.right(15)

t.seth(-150)
t.penup()
t.fd(8)
t.pendown()
for i in range(5):
    t.fd(10)
    t.right(15)

t.seth(-155)
t.penup()
t.fd(5)
t.pendown()
for i in range(5):
    t.fd(7)
    t.right(15)

# 第二层树叶
t.penup()
t.goto(-55, 34)
t.pendown()
t.seth(-120)
for i in range(10):
    t.fd(8)
    t.right(5)

t.penup()
t.goto(50, 35)
t.seth(-60)
t.pendown()
for i in range(10):
    t.fd(8)
    t.left(5)

t.seth(-120)
t.penup()
t.fd(10)
t.seth(-145)
t.pendown()
for i in range(5):
    t.fd(10)
    t.right(15)

t.penup()
t.fd(10)
t.seth(-145)
t.pendown()
for i in range(5):
    t.fd(12)
    t.right(15)

t.penup()
t.fd(8)
t.seth(-145)
t.pendown()
for i in range(5):
    t.fd(10)
    t.right(15)

t.penup()
t.seth(-155)
t.fd(8)
t.pendown()
for i in range(5):
    t.fd(11)
    t.right(15)

# 第三层树叶
t.penup()
t.goto(-100, -40)
t.seth(-120)
t.pendown()
for i in range(10):
    t.fd(6)
    t.right(3)

t.penup()
t.goto(80, -39)
t.seth(-50)
t.pendown()
for i in range(10):
    t.fd(6)
    t.left(3)

t.seth(-155)
t.penup()
t.fd(10)
t.pendown()
for i in range(5):
    t.fd(8)
    t.right(10)

t.penup()
t.fd(8)
t.seth(-145)
t.pendown()
for i in range(7):
    t.fd(8)
    t.right(10)

t.penup()
t.fd(8)
t.seth(-145)
t.pendown()
for i in range(7):
    t.fd(7)
    t.right(10)

t.penup()
t.fd(8)
t.seth(-145)
t.pendown()
for i in range(7):
    t.fd(7)
    t.right(10)

t.penup()
t.fd(8)
t.seth(-140)
t.pendown()
for i in range(7):
    t.fd(6)
    t.right(10)

# 第四层树叶
t.penup()
t.goto(-120, -95)
t.seth(-130)
t.pendown()
for i in range(7):
    t.fd(10)
    t.right(5)

t.penup()
t.goto(100, -95)
t.seth(-50)
t.pendown()
for i in range(7):
    t.fd(10)
    t.left(5)

t.penup()
t.seth(-120)
t.fd(10)
t.seth(-155)
t.pendown()
for i in range(6):
    t.fd(8)
    t.right(10)

t.penup()
t.seth(-160)
t.fd(10)
t.seth(-155)
t.pendown()
for i in range(6):
    t.fd(8)
    t.right(10)

t.penup()
t.seth(-160)
t.fd(10)
t.seth(-155)
t.pendown()
for i in range(6):
    t.fd(8)
    t.right(10)

t.penup()
t.seth(-160)
t.fd(10)
t.seth(-160)
t.pendown()
for i in range(6):
    t.fd(8)
    t.right(10)

t.penup()
t.seth(-160)
t.fd(10)
t.seth(-160)
t.pendown()
for i in range(6):
    t.fd(8)
    t.right(10)

t.penup()
t.seth(-160)
t.fd(10)
t.seth(-165)
t.pendown()
for i in range(5):
    t.fd(10)
    t.right(11)

# 树干
t.penup()
t.goto(-70, -165)
t.seth(-85)
t.pendown()
t.pencolor("#592720")
for i in range(3):
    t.fd(5)
    t.left(3)

t.penup()
t.goto(70, -165)
t.seth(-95)
t.pendown()
for i in range(3):
    t.fd(5)
    t.right(3)

t.seth(-170)
t.penup()
t.fd(10)
t.pendown()
for i in range(10):
    t.fd(12)
    t.right(2)


# 树梢
def tree_plane(x, y, z):
    """树梢平面"""
    t.penup()
    t.goto(x, y)
    t.seth(-z)
    t.pendown()
    for _ in range(5):
        t.fd(10)
        t.right(10)


def tree_side(x, y, z):
    """树梢测面"""
    t.penup()
    t.goto(x, y)
    t.seth(-z)
    t.pendown()
    for _ in range(5):
        t.fd(10)
        t.left(10)


def tree_middle(x, y, z):
    """树叶中间"""
    t.penup()
    t.goto(x, y)
    t.seth(-z)
    t.pendown()
    for _ in range(5):
        t.fd(6)
        t.right(10)
    t.seth(-150)
    t.fd(20)


t.pencolor("#faf0be")  # 树梢颜色
t.penup()
t.goto(70, -165)
t.pendown()
t.seth(-90)
t.pensize(8)
t.circle(-20, 90)  # 绘制圆形

t.penup()
t.goto(30, -185)
t.pendown()
t.seth(-180)
t.pensize(8)
t.fd(40)

tree_plane(-70, -150, 160)
tree_plane(100, -150, 160)
tree_side(110, -110, 50)
tree_middle(80, -120, 180)
tree_plane(70, -85, 165)
tree_plane(-40, -85, 165)
tree_middle(80, -30, 180)
tree_middle(40, 10, 180)
tree_plane(-60, 30, 120)
tree_plane(-20, -20, 150)
tree_side(45, 40, 60)
tree_plane(-30, 40, 170)
tree_plane(-30, 110, 115)
tree_side(40, 90, 60)
tree_plane(80, 50, 160)


# 蝴蝶结
def hdj(x, y):
    t.penup()
    t.goto(x, y)
    t.seth(80)
    t.pendown()
    t.pensize(2)
    t.circle(5)
    t.seth(10)
    t.fd(15)
    t.seth(120)
    t.fd(20)
    t.seth(240)
    t.fd(20)
    t.seth(180)
    t.fd(20)
    t.seth(-60)
    t.fd(20)
    t.seth(50)
    t.fd(20)
    t.seth(-40)
    t.fd(30)
    t.seth(-130)
    t.fd(5)
    t.seth(135)
    t.fd(30)
    t.seth(-60)
    t.fd(30)
    t.seth(-150)
    t.fd(6)
    t.seth(110)
    t.fd(30)


def uit(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.pensize(2)
    t.circle(5)
    t.seth(-10)
    t.fd(15)
    t.seth(90)
    t.fd(15)
    t.seth(200)
    t.fd(15)
    t.seth(160)
    t.fd(15)
    t.seth(-90)
    t.fd(15)
    t.seth(10)
    t.fd(15)
    t.seth(-60)
    t.fd(20)
    t.seth(-180)
    t.fd(5)
    t.seth(110)
    t.fd(20)
    t.seth(-90)
    t.fd(20)
    t.seth(-180)
    t.fd(6)
    t.seth(70)
    t.fd(15)
    t.hideturtle()


def yut(x, y, z):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.seth(z)
    for po in range(5):
        t.fd(4)
        t.left(36)


def ytu(x, y, z):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.seth(z)
    for kk in range(5):
        t.fd(4)
        t.left(36)


def iou(x, y, z):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.seth(z)
    for po in range(10):
        t.fd(4)
        t.left(18)


# 小蝴蝶结
t.pencolor("pink")   # 小蝴蝶颜色
t.seth(0)
uit(40, -160)
hdj(-80, -120)
yut(-67, -115, 120)
yut(-86, -123, 150)
hdj(40, -50)
yut(52, -45, 130)
yut(34, -55, 160)
t.seth(0)
uit(-20, -60)
ytu(-4, -60, 100)
ytu(-20, -60, 120)
hdj(-30, 20)
yut(-15, 25, 130)
yut(-40, 20, 180)
uit(30, 70)
ytu(45, 70, 100)
ytu(30, 70, 120)

# 大蝴蝶结
t.pencolor("#e6b422")   # 大蝴蝶颜色
t.pensize(5)
t.penup()
t.seth(0)
t.goto(0, 150)
t.pendown()
t.circle(10)
t.seth(-15)
t.fd(40)
t.seth(90)
t.fd(40)
t.seth(200)
t.fd(40)
t.seth(160)
t.fd(40)
t.seth(-90)
t.fd(40)
t.seth(15)
t.fd(40)
t.seth(-70)
t.pensize(4)
t.fd(40)
t.seth(-180)
t.fd(10)
t.seth(100)
t.fd(40)
t.seth(-100)
t.fd(40)
t.seth(-180)
t.fd(10)
t.seth(70)
t.fd(40)
t.penup()
t.seth(0)
t.goto(0, 130)
t.pendown()
t.seth(0)
iou(35, 145, 100)
iou(-7, 145, 110)


# t.pencolor("red")
# t.pensize(7)
# t.penup()
# t.goto(-35, 135)
# t.pendown()

# 圣诞帽
t.pencolor("#f8f8ff")   # 圣诞帽颜色
t.seth(-20)
t.pensize(2)
t.penup()
t.goto(-30, -120)
t.pendown()
t.fillcolor("red")  # 圣诞帽填充颜色
t.fd(30)
t.circle(4, 180)
t.fd(30)
t.circle(4, 180)
t.penup()
t.goto(-25, -115)
t.seth(75)
t.pendown()
t.begin_fill()
for i in range(5):
    t.fd(6)
    t.right(20)
t.seth(-10)
for i in range(5):
    t.fd(8)
    t.right(15)
t.seth(145)
for i in range(5):
    t.fd(5)
    t.left(2)
t.seth(90)
for i in range(5):
    t.fd(1)
    t.left(2)
t.seth(-90)
for i in range(4):
    t.fd(4)
    t.right(6)
t.seth(161)
t.fd(30)
t.end_fill()


# 五角星
def koc(x, y, size):
    t.pensize(2)
    t.pencolor("black")     # 五角星颜色
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.fillcolor("yellow")   # 五角星填充颜色
    for i in range(5):
        t.left(72)
        t.fd(size)
        t.right(144)
        t.fd(size)
    t.end_fill()


t.seth(-15)
koc(-120, -70, 10)
t.seth(10)
koc(100, -20, 10)
t.seth(-10)
koc(10, 40, 10)
t.seth(30)
koc(-80, 60, 10)
koc(100, -150, 10)
koc(-140, -150, 10)
koc(20, 120, 10)

# 袜子
t.pencolor("#f8f8ff")   # 袜子颜色
t.seth(-20)
t.pensize(2)
t.penup()
t.goto(-20, 80)
t.pendown()
t.fd(25)
t.circle(4, 180)
t.fd(25)
t.circle(4, 180)
t.penup()
t.goto(-15, 80)
t.pendown()
t.begin_fill()
t.fillcolor("red")  # 袜子填充颜色
t.seth(-120)
t.fd(20)
t.seth(150)
t.fd(5)
t.circle(7, 180)
t.fd(15)
t.circle(5, 90)
t.fd(30)
t.seth(160)
t.fd(18)
t.end_fill()

# 文字祝福
t.penup()
t.goto(0, -250 + 10)
t.pendown()
t.write("Joyeux Noël", align="center", font=("Comic Sans MS", 26, "bold"))

# 画图结束
t.done()

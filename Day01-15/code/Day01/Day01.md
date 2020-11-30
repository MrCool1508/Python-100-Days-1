# My python day01
这是我的第一天python学习。安装了Jupyter Notebook。
## 注释
+ 单行注释：
    + 以“# ”开头。
+ 多行注释：
    + 以“'''....'''”开头结尾。
## 练习
### 1、输入以下代码：
```
import this
```


```python
import this
```

    The Zen of Python, by Tim Peters
    
    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    Special cases aren't special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than *right* now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let's do more of those!
    

译文如下：  
python之禅  
Tim Peters  
美丽好过丑陋。  
显性好过隐性。
简约好过复杂。  
复杂好过繁琐。  
平面好过网状。  
稀疏好过稠密。  
可读性强。  
特例不至于打破规则。  
尽管实用性胜过纯洁性。  
错误不应被无视。  
除非明确地沉默。  
面对模棱两可时，拒绝猜测的诱惑。  
那应该有且只有一种显而易见地方式对待它。  
尽管这种方式并不明显，除非你是荷兰人。  
当下永远比从未好。  
尽管，从未经常比正确的当下好。  
如果，实现很难解释，那就是个坏的点子。  
如果，实现很容易解释，那可能是个好方法。  
命名空间是一个伟大的点子——让我们完成更多的命名空间！  

### 2、学习'turtle'的用法


```python
import turtle
# 设画笔的大小为4
turtle.pensize(4)
# 设画笔的颜色为红色
turtle.pencolor("red")
# 向前100
turtle.forward(100)
# 方向，向右旋转90度
turtle.right(90)
turtle.forward(100)
# 试试向右旋转60度
turtle.right(60)
turtle.forward(100)
turtle.right(90)
turtle.forward(199)
turtle.mainloop()
```

#### 2.1绘制国旗


```python
import turtle
# 定义矩形函数
def draw_rectangle(x, y, width, height):
    turtle.goto(x, y)
    turtle.pencolor('red')
    turtle.fillcolor('red') # 填充红色
    turtle.begin_fill() # 填充区域
    for i in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill
# 绘制五角星
def draw_star(x, y, radius):
    turtle.setpos(x, y)
    pos_1 = turtle.pos()
    turtle.circle(-radius, 72)
    pos_2 = turtle.pos()
    turtle.circle(-radius, 72)
    pos_3 = turtle.pos()
    turtle.circle(-radius, 72)
    pos_4 = turtle.pos()
    turtle.circle(-radius, 72)
    pos_5 = turtle.pos()
    turtle.circle(-radius, 72)
    # 设置
    turtle.color('yellow', 'yellow')# 设置画笔颜色为黄色
    turtle.begin_fill()
    turtle.goto(pos_3)
    turtle.goto(pos_1)
    turtle.goto(pos_4)
    turtle.goto(pos_2)
    turtle.goto(pos_5)
    turtle.end_fill()

# 主程序
def main():
    turtle.speed(12)
    turtle.penup()
    x, y = -270, -180
    # 画国旗主体
    width, height = 540, 360
    draw_rectangle(x, y, width, height)
    # 画大星星
    '''
    pice = 22
    center_x, center_y = x + 5 * pice, y + height - pice * 5
    turtle.goto(center_x, center_y)
    turtle.left(90)
    turtle.forward(pice * 3)
    turtle.right(90)
    draw_star(turtle.xcor(), turtle.ycor(), pice * 3)
    x_poses, y_poses = [10, 12, 12, 10], [2, 4, 7, 9]
    # 画小星星
    for x_pos, y_pos in zip(x_poses, y_poses):
        turtle.goto(x + x_pos * pice, y + height - y_pos * pice)
        turtle.left(turtle.towards(center_x, center_y) - turtle.heading())
        turtle.forward(pice)
        turtle.right(90)
        draw_star(turtle.xcor(), turtle.ycor(), pice)
    '''
    # 隐藏海龟
    turtle.ht()
    # 显示绘图窗口
    turtle.mainloop()


if __name__ == '__main__':
    main()

```
#### 2.2绘制小猪佩奇


```python
"""
绘制小猪佩奇
"""
from turtle import *


def nose(x,y):
    """画鼻子"""
    penup()
    # 将海龟移动到指定的坐标
    goto(x,y)
    pendown()
    # 设置海龟的方向（0-东、90-北、180-西、270-南）
    setheading(-30)
    begin_fill()
    a = 0.4
    for i in range(120):
        if 0 <= i < 30 or 60 <= i <90:
            a = a + 0.08
            # 向左转3度
            left(3)
            # 向前走
            forward(a)
        else:
            a = a - 0.08
            left(3)
            forward(a)
    end_fill()
    penup()
    setheading(90)
    forward(25)
    setheading(0)
    forward(10)
    pendown()
    # 设置画笔的颜色(红, 绿, 蓝)
    pencolor(255, 155, 192)
    setheading(10)
    begin_fill()
    circle(5)
    color(160, 82, 45)
    end_fill()
    penup()
    setheading(0)
    forward(20)
    pendown()
    pencolor(255, 155, 192)
    setheading(10)
    begin_fill()
    circle(5)
    color(160, 82, 45)
    end_fill()


def head(x, y):
    """画头"""
    color((255, 155, 192), "pink")
    penup()
    goto(x,y)
    setheading(0)
    pendown()
    begin_fill()
    setheading(180)
    circle(300, -30)
    circle(100, -60)
    circle(80, -100)
    circle(150, -20)
    circle(60, -95)
    setheading(161)
    circle(-300, 15)
    penup()
    goto(-100, 100)
    pendown()
    setheading(-30)
    a = 0.4
    for i in range(60):
        if 0<= i < 30 or 60 <= i < 90:
            a = a + 0.08
            lt(3) #向左转3度
            fd(a) #向前走a的步长
        else:
            a = a - 0.08
            lt(3)
            fd(a)
    end_fill()


def ears(x,y):
    """画耳朵"""
    color((255, 155, 192), "pink")
    penup()
    goto(x, y)
    pendown()
    begin_fill()
    setheading(100)
    circle(-50, 50)
    circle(-10, 120)
    circle(-50, 54)
    end_fill()
    penup()
    setheading(90)
    forward(-12)
    setheading(0)
    forward(30)
    pendown()
    begin_fill()
    setheading(100)
    circle(-50, 50)
    circle(-10, 120)
    circle(-50, 56)
    end_fill()


def eyes(x,y):
    """画眼睛"""
    color((255, 155, 192), "white")
    penup()
    setheading(90)
    forward(-20)
    setheading(0)
    forward(-95)
    pendown()
    begin_fill()
    circle(15)
    end_fill()
    color("black")
    penup()
    setheading(90)
    forward(12)
    setheading(0)
    forward(-3)
    pendown()
    begin_fill()
    circle(3)
    end_fill()
    color((255, 155, 192), "white")
    penup()
    seth(90)
    forward(-25)
    seth(0)
    forward(40)
    pendown()
    begin_fill()
    circle(15)
    end_fill()
    color("black")
    penup()
    setheading(90)
    forward(12)
    setheading(0)
    forward(-3)
    pendown()
    begin_fill()
    circle(3)
    end_fill()


def cheek(x,y):
    """画脸颊"""
    color((255, 155, 192))
    penup()
    goto(x,y)
    pendown()
    setheading(0)
    begin_fill()
    circle(30)
    end_fill()


def mouth(x,y):
    """画嘴巴"""
    color(239, 69, 19)
    penup()
    goto(x, y)
    pendown()
    setheading(-80)
    circle(30, 40)
    circle(40, 80)


def setting():
    """设置参数"""
    pensize(4)
    # 隐藏海龟
    hideturtle()
    colormode(255)
    color((255, 155, 192), "pink")
    setup(840, 500)
    speed(10)


def main():
    """主函数"""
    setting() 
    nose(-100, 100)
    head(-69, 167)
    ears(0, 160)
    eyes(0, 140)
    cheek(80, 10)
    mouth(-20, 30)
    done()


if __name__ == '__main__':
    main()

```

#### 2.3比较二者不同
+ 'import'的方式不同，相当于是否需要输入'turtle.'

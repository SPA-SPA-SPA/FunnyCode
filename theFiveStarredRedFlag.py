import turtle
def draw_recursive_pentagram(size):
    # 画五角星的函数
    count=1
    # 设置填充颜色为黄色
    turtle.fillcolor('yellow')
    # 设置画笔颜色为黄色
    turtle.pencolor('yellow')
    # 开始填充，因为要开始画五角星了
    turtle.begin_fill()
    # 画五角星的一个循环
    while count<=5:
            turtle.forward(size)
            turtle.right(144)
            count=count+1
    # 填充完毕
    turtle.end_fill()
    # 设置画笔颜色为红色
    turtle.pencolor('red')

# 设置画笔的笔头不可见
turtle.hideturtle()
# 设置填充颜色为红色，这里是准备填充一个矩形
turtle.fillcolor('red')
# 开始填充
turtle.begin_fill()
# 设置画笔颜色为红色
turtle.pencolor('red')
# 移动笔头到点(x, y)
turtle.setpos(-40, 40)
turtle.pencolor('red')
turtle.setpos(350, 40)
turtle.setpos(350, -200)
turtle.setpos(-40, -200)
turtle.setpos(-40, 40)
turtle.pencolor('red')
# 填充完毕
turtle.end_fill()

# 0 画最大的那个五角星
# 首先移动笔头到(0, 0)位置
turtle.setpos(0, 0)
# 调用画五角星的函数，给参数70像素
draw_recursive_pentagram(70)

# 1 画右边上面数起第一个小五角星，以下同理
turtle.setpos(120, 0)
draw_recursive_pentagram(30)

# 2
turtle.setpos(100, -60)
draw_recursive_pentagram(30)

# 3
turtle.setpos(60, -100)
draw_recursive_pentagram(30)

# 4
turtle.setpos(0, -110)
draw_recursive_pentagram(30)

# 这里要去掉最大五角星的一条红色横线，已达到美观要求。
# 移动笔头到(0, 0)，注意此时的笔头是红色。然后操作如下，前面均有解释。
turtle.setpos(0,0)
turtle.pencolor('yellow')
turtle.forward(70)

# 防止图像显示后自动消失
turtle.done()

# 参考资料：
# 1. https://blog.csdn.net/Jamesjjjjj/article/details/80850669
# 2. https://blog.csdn.net/ameng001/article/details/81182388
# 3. https://docs.python.org/3.3/library/turtle.html?highlight=turtle#turtle.forward
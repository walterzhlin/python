"""
請使用turtle模組以及for印出以下圖形
t0_turtle_stamp.jpg
提示：
turtle.home()是讓烏龜回到原點的指令
"""
import turtle

turtle.shape('triangle')
for i in range(0, 8):
    turtle.penup()
    turtle.home()
    turtle.right(45 * i)
    turtle.forward(100)
    turtle.stamp()
turtle.home()
turtle.stamp()
turtle.done()
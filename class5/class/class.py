import turtle
# turtle.forward()
# turtle.backward()
# turtle.right()
# turtle.left()
# turtle.done()
# for i in range(4):
#     turtle.forward(100)
#     turtle.right(90)
# turtle.done()
# turtle.color('red') # 設顏色
# turtle.shape('turtle')# 設烏龜形'arrow','turtle','circle','square','triangle','classic'.
# turtle.stamp() # 蓋章
# turtle.penup() # 提筆
# turtle.pendown() # 下筆
# turtle.shape('classic')
# turtle.penup()
# for i in range(2, 1000, 1):
#     turtle.forward(i)
#     turtle.stamp()
#     turtle.right(35)
# turtle.done()
# turtle.pensize(5) #線徑寬度1~10
# turtle.pencolor("yellow") #線的顏色
# turtle.fillcolor("yellow") #區域填滿顏色
# turtle.begin_fill() #填滿區域設定開始
# turtle.end_fill() #填滿區域設定結束

turtle.pensize(5)
turtle.pencolor("yellow")
turtle.fillcolor("yellow")
turtle.begin_fill()
for i in range(5):
    turtle.forward(50)
    turtle.left(144)
turtle.end_fill()
turtle.done()
#SevenDigitsDraw.py
import turtle
import time
def drawGap():
    turtle.penup()
    turtle.fd(5)
    turtle.pendown()
def drawLine(draw):
    drawGap()
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    drawGap()
    turtle.left(90)
def drawDigit(digit):
    drawLine(True) if digit in [2,3,4,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,1,2,3,4,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,3,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,4,5,6,8,9] else drawLine(False)
    turtle.right(90)
    drawLine(True) if digit in [0,2,6,8] else drawLine(False)
    drawLine(True) if digit in [0,2,3,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,1,3,4,5,6,7,8,9] else drawLine(False)
    turtle.penup()
    turtle.right(180)
    turtle.fd(20)
def drawDate(date):
    turtle.pencolor("red")
    for c in date:
        if c == '+':
            turtle.write("年",font=('Arial',18,'normal'))
            turtle.pencolor('green')
            turtle.fd(40)
        elif c == '-':
            turtle.write("月", font=('Arial', 18, 'normal'))
            turtle.pencolor('blue')
            turtle.fd(40)
        elif c == '=':
            turtle.write("日", font=('Arial', 18, 'normal'))
            turtle.pencolor('purple')
            turtle.goto(-250,-100)
        elif c == ':':
            turtle.write("：", font=('Arial', 18, 'normal'))
            turtle.fd(40)
        else:
            drawDigit(eval(c))
def main():
    turtle.setup(900,600,200,100)
    turtle.penup()
    turtle.goto(-300,100)
    turtle.pendown()
    turtle.pensize(5)
    turtle.pencolor("red")
    date = time.strftime('%Y+%m-%d=%H:%M:%S',time.localtime())
    drawDate(date)
    turtle.fd(10)
    turtle.right(90)
    turtle.fd(50)
    turtle.write("--by YabinLi",font=('Arial',18,'bold'))
    turtle.hideturtle()
    turtle.done()
main()

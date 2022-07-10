from turtle import*
from textwrap import fill
rt(45)
bgcolor('white')
color('pink')
penup()
goto(-50,50)
lt(90)
pendown()
begin_fill()
for i in range(180):
    fd(1)
    rt(1)
penup()
goto(-50,50)
rt(90)
pendown()
for i in range(180):
    fd(1)
    lt(1)

fd(115.5)
lt(90)
fd(115.5)
end_fill()

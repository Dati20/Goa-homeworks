from turtle import*

# we want paint a house

# step 1: draw a square

shape("turtle")
width(7)
color("purple")
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)

#end of square


# drawing a door

forward(70)

color("yellow")

begin_fill()



left(90)

forward(120)

right(90)
forward(60)
right(90)
forward(120)

end_fill()
penup()
goto(200,200)
pendown()

color("red")
begin_fill()
right(150)

forward(200)
left(120)
forward(200)
end_fill()


# drawing a window

color("blue")
penup()
begin_fill()
left(120)
goto(0,130)
pendown()
forward(45)
left(90)
forward(45)
left(90)
forward(45)
end_fill()

#drawing a second window

color("blue")
begin_fill()
penup()

right(90)
goto(200,130)
pendown()
forward(45)
left(90)
forward(45)
left(90)
forward(45)
left(90)
forward(45)
end_fill()



exitonclick()





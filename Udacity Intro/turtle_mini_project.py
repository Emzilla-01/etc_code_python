import turtle

def draw_square(a_turtle):	
	for i in range(0,4):
		a_turtle.forward(100)
		a_turtle.right(90)
		
def draw_circle_of_squares(a_turtle, size, steps):
	degrees=360
	step_degrees = 360/steps
	for step in range(steps):
		draw_square(a_turtle)
		a_turtle.fd(size/steps)
		a_turtle.rt(step_degrees)
		
def draw_petal(a_turtle):
	"""Let's try to make a teardrop shape."""
	a_turtle.fd(50)
	for i in range(6):
		a_turtle.lt(180/(i+1))
		a_turtle.fd(5)
	#a_turtle.lt(45)
	
		
def draw_flower(a_turtle):
	a_turtle.seth(90)
	a_turtle.fd(100)

	for i in range(36):
		draw_petal(a_turtle)
		a_turtle.lt(10)

window = turtle.Screen()
window.bgcolor("black")

joe = turtle.Turtle()
joe.shape("turtle")
joe.color("pink")
joe.speed(100)
	
#draw_circle_of_squares(joe, 1000, 36)
draw_flower(joe)

window.exitonclick()
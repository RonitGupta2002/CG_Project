#Import the turtle module which allows for unique graphics
import turtle

#Set the background color of the turtle window to white.
turtle.bgcolor('white')

#Vegeta's Hair
hair = turtle.Turtle()       # Create a new turtle instance called 'hair'
hair.speed(20)  # Set the drawing speed of the 'hair'
#Pick up the pen to prevent drawing while the turtle is moved to the start position
hair.penup()  
hair.goto((189.15, -42.93))  # Move the turtle to the specified position
hair.pendown()               # Put down the pen to start drawing
hair.begin_fill()            # Begin filling the shape
hair.lt(105)                 # Turn the turtle left by 105 degrees
hair.fd(80)                  # Move the turtle forward by 80 units
hair.left(25)                # Turn the turtle left by 25 degrees
hair.back(20)                # Move the turtle backward by 20 units
hair.rt(50)                  # Turn the turtle right by 50 degrees
hair.fd(30)                  # Move the turtle forward by 30 units
hair.rt(25)                  # Turn the turtle right by 25 degrees
hair.fd(100)                 # Move the turtle forward by 100 units
hair.lt(35)                  # Turn the turtle left by 35 degrees
hair.back(40)                # Move the turtle backward by 40 units
hair.rt(35)                  # Turn the turtle right by 35 degrees
# Draw a circle with a radius of 200 units in the clockwise direction for 30 degrees
hair.circle(-200, extent=30)  
hair.lt(45)                  # Turn the turtle left by 45 degrees
hair.back(35)                # Move the turtle backward by 35 units
hair.rt(25)                  # Turn the turtle right by 25 degrees
# Draw a circle with a radius of 100 units in the clockwise direction for 20 degrees
hair.circle(-100, extent=20) 
# Draw a circle with a radius of 100 units in the counterclockwise direction for 30 degrees
hair.circle(100, extent=30)  
hair.left(35)                # Turn the turtle left by 35 degrees
hair.back(310)               # Move the turtle backward by 310 units
hair.lt(90)                  # Turn the turtle left by 90 degrees
hair.fd(100)                 # Move the turtle forward by 100 units
hair.goto((189.15, -42.93))  # Move the turtle to the start position
hair.end_fill()              # End filling the shape
hair.hideturtle()            # Hide the turtle



#Vegeta's Neck
neck = turtle.Turtle()
neck.speed(20)  # Set the drawing speed of the 'neck'
neck.color("black", "#FFE1CD")  # Set the pen color and fill color for the 'neck'
# Pick up the pen to prevent drawing while the turtle is moved to the start position
neck.penup()  
neck.goto(243.28, -169.45)  # Move the turtle to the specified position
neck.pendown()  # Put down the pen to start drawing
neck.begin_fill()  # Begin filling the shape
neck.rt(85)  # Turn the turtle right by 85 degrees
neck.fd(30)  # Move the turtle forward by 30 units
neck.rt(45)  # Turn the turtle right by 45 degrees
neck.bk(40)  # Move the turtle backward by 40 units
neck.fd(70)  # Move the turtle forward by 70 units
t = neck.pos()  # Store the current position of the turtle in the variable 't'
neck.lt(130)  # Turn the turtle left by 130 degrees
 # Draw a circle with a radius of 300 units in the clockwise direction for 32 degrees
neck.circle(300, extent=32) 
neck.lt(90)  # Turn the turtle left by 90 degrees
end = neck.pos()  # Store the current position of the turtle in the variable 'end'
# Draw a circle with a radius of 300 units in the clockwise direction for 30 degrees
neck.circle(300, extent=30)  
neck.goto(243.28, -169.45)  # Move the turtle to the start position
neck.end_fill()  # End filling the shape
neck.hideturtle()  # Hide the turtle


# Create a new turtle instance called 'vegeta'
vegeta = turtle.Turtle()
vegeta.speed(20)  # Set the drawing speed of 'vegeta'
vegeta.color("black", "#FFE1CD")  # Set the pen color and fill color for 'vegeta'
vegeta.penup()  
vegeta.goto(180, -85)  # Move 'vegeta' to the specified position
vegeta.pendown()  # Put down the pen to start drawing
vegeta.begin_fill()  # Begin filling the shape

# Draw the shape of 'vegeta' to represent his armor and suit
vegeta.rt(140)
vegeta.fd(30)
vegeta.lt(110)
vegeta.fd(20)
vegeta.rt(60)
vegeta.forward(7)
vegeta.lt(45)
vegeta.fd(10)
v = vegeta.pos()  # Store the current position of 'vegeta' in the variable 'v'
vegeta.lt(55)
vegeta.fd(20)
vegeta.lt(25)
vegeta.fd(10)
vegeta.penup()
vegeta.goto(v)
vegeta.pendown()
vegeta.rt(105)
vegeta.fd(10)
vegeta.lt(45)
vegeta.fd(10)
vegeta.back(5)
vegeta.rt(45)
vegeta.fd(35)

# Draw additional details on 'vegeta' to enhance the appearance
vegeta.speed(20)
for i in range(5):
    vegeta.lt(17)
    vegeta.fd(3)
vegeta.fd(30)
g = vegeta.pos()  # Store the current position of 'vegeta' in the variable 'g'
vegeta.fd(70)
vegeta.lt(70)
vegeta.fd(40)
vegeta.rt(150)
vegeta.circle(5, extent=110)
vegeta.fd(30)
vegeta.lt(70)
vegeta.circle(200, extent=7)
vegeta.circle(10, extent=100)
vegeta.fd(25)
vegeta.rt(100)
vegeta.fd(30)
vegeta.rt(145)
vegeta.fd(10)
vegeta.circle(5, extent=140)
vegeta.forward(70)
vegeta.circle(20, extent=65)
vegeta.fd(5)
vegeta.circle(45, extent=65)
vegeta.fd(35)
vegeta.fd(35)
vegeta.goto(180, -85)  # Move 'vegeta' to the start position
vegeta.end_fill()  # End filling the shape
vegeta.hideturtle()  # Hide 'vegeta'



blue = turtle.Turtle()  # Create a new turtle instance called 'blue'
blue.speed(20)  # Set the drawing speed of 'blue'
blue.color("blue")  # Set the pen color for 'blue' to blue
blue.penup()  # Pick up the pen to prevent drawing while the turtle is moved to the start position
blue.goto(t)  # Move 'blue' to the specified position stored in 't'
blue.pendown()  # Put down the pen to start drawing
blue.begin_fill()  # Begin filling the shape

# Draw a partial circle with a radius of 20 units in the counterclockwise direction for 40 degrees
blue.rt(160)
blue.circle(20, extent=40)
blue.fd(110)  # Move 'blue' forward by 110 units
blue.lt(120)  # Turn 'blue' left by 120 degrees
blue.fd(250)  # Move 'blue' forward by 250 units
blue.goto(end)  # Move 'blue' to the position stored in 'end'
blue.end_fill()  # End filling the shape
blue.hideturtle()  # Hide 'blue'

#Vegaeta's Armour
suit = turtle.Turtle()  # Create a new turtle instance called 'suit'
suit.speed(20)  # Set the drawing speed of 'suit'
suit.color("#F3A903")  # Set the pen color for 'suit' to a shade of yellow (#F3A903)
suit.penup()  # Pick up the pen to prevent drawing while the turtle is moved to the start position
suit.goto(end)  # Move 'suit' to the specified position stored in 'end'
suit.pendown()  # Put down the pen to start drawing
suit.begin_fill()  # Begin filling the shape
# Draw a partial circle with a radius of 120 units in the clockwise direction for 75 degrees
suit.rt(180)
suit.circle(120, extent=75)
suit.lt(100)  # Turn 'suit' left by 100 degrees
suit.fd(50)  # Move 'suit' forward by 50 units
s = suit.pos()  # Store the current position of 'suit' in 's'
suit.lt(100)  # Turn 'suit' left by 100 degrees
# Draw a partial circle with a radius of -70 units in the counterclockwise direction for 95 degrees
suit.circle(-70, extent=95)
suit.goto(end)  # Move 'suit' to the position stored in 'end'
suit.end_fill()  # End filling the shape
suit.penup()  # Pick up the pen
suit.goto(s)  # Move 'suit' to the position stored in 's'
suit.pendown()  # Put down the pen
suit.color("black", "#707070")  # Set the pen color to black and the fill color to a dark gray (#707070)
suit.pensize(2)  # Set the pen size to 2
suit.begin_fill()  # Begin filling the shape
suit.rt(182)  # Turn 'suit' right by 182 degrees
suit.fd(70)  # Move 'suit' forward by 70 units
suit.circle(10, extent=90)  # Draw a quarter circle with a radius of 10 units
suit.fd(5)  # Move 'suit' forward by 5 units
suit.rt(90)  # Turn 'suit' right by 90 degrees
suit.fd(50)  # Move 'suit' forward by 50 units
suit.circle(18, extent=70)  # Draw a partial circle with a radius of 18 units
suit.fd(35)  # Move 'suit' forward by 35 units
suit.lt(110)  # Turn 'suit' left by 110 degrees
suit.fd(250)  # Move 'suit' forward by 250 units
suit.lt(90)  # Turn 'suit' left by 90 degrees
suit.fd(63)  # Move 'suit' forward by 63 units
suit.goto(s)  # Move 'suit' to the position stored in 's'
suit.end_fill()  # End filling the shape
suit.hideturtle()  # Hide 'suit'


eye = turtle.Turtle() # Create a new turtle instance for drawing the left eye of Vegeta
eye.speed(20)    # Set the drawing speed of the turtle
eye.penup()    # Pick up the pen to prevent drawing while the turtle is moved to the start position
eye.goto(185, -75)   # Move the turtle to the specified position
eye.pendown()     # Put down the pen to start drawing
eye.right(35)     # Turn the turtle right by 35 degrees
eye.forward(5)      # Move the turtle forward by 5 units
e2 = eye.pos()      # Save the current position of the turtle as 'e2'
eye.lt(70)       # Turn the turtle left by 70 degrees
eye.begin_fill()     # Begin filling the shape
eye.forward(60)     # Move the turtle forward by 60 units
eye.rt(70)     # Turn the turtle right by 70 degrees
eye.forward(10)    # Move the turtle forward by 10 units
eye.rt(115)     # Turn the turtle right by 115 degrees
eye.forward(17)    # Move the turtle forward by 17 units
e3 = eye.pos()     # Save the current position of the turtle as 'e3'
eye.forward(40)    # Move the turtle forward by 40 units
eye.goto(e2)    # Move the turtle to position 'e2'
eye.end_fill()    # End filling the shape
eye.goto(e3)     # Move the turtle to position 'e3'
eye.color("black", "white")# Set the color of the turtle to draw the white part of the eye
eye.begin_fill()           # Begin filling the shape
eye.lt(70)    # Turn the turtle left by 70 degrees
eye.forward(17)    # Move the turtle forward by 17 units
eye.rt(85)    # Turn the turtle right by 85 degrees
eye.forward(37)    # Move the turtle forward by 37 units
eye.end_fill()    # End filling the shape
eye.begin_fill()     # Begin filling the shape
eye.color("black")     # Set the color of the turtle to draw the pupil of the eye
eye.circle(-5)    # Draw a circle with a radius of 5 units in the clockwise direction
eye.end_fill()      # End filling the shape
eye.hideturtle()           # Hide the turtle


mouth = turtle.Turtle() # Create a new turtle instance for drawing the mouth of Vegeta
mouth.speed(20)      # Set the drawing speed of the turtle
mouth.penup() # Pick up the pen to prevent drawing while the turtle is moved to the start position
mouth.goto(180, -130)   # Move the turtle to the specified position
mouth.pendown()     # Put down the pen to start drawing
mouth.color("black")    # Set the color of the turtle to draw the mouth
mouth.begin_fill()    # Begin filling the shape
mouth.setheading(320)    # Set the orientation of the turtle
# Draw a simple curved smile by drawing a partial circle with a radius of 15 units 
# in the counterclockwise direction for 120 degrees
mouth.circle(15, extent=120)     
mouth.end_fill()    # End filling the shape
mouth.hideturtle()     # Hide the turtle

# Function to write text vertically with increased letter spacing
def write_vertical(turtle, text, font, spacing):
    for character in text:
        turtle.write(character, font=font, align="center")
        turtle.penup()
        turtle.right(90)
        turtle.forward(spacing)
        turtle.left(90)
        turtle.pendown()

# Create a turtle to write "VEGETA"
text_turtle = turtle.Turtle()  # Create a new turtle instance for writing text
text_turtle.speed(20)  # Set the drawing speed of the turtle
text_turtle.penup()  # Pick up the pen to prevent drawing while the turtle is moved to the start position
text_turtle.goto(-300, 45)  # Adjust the coordinates to place the text on the left side of the character
text_turtle.pendown()  # Put down the pen to start drawing
text_turtle.color("blue")  # Set the color of the turtle to blue

# Define font style and size
vertical_font_style = ("Arial", 30, "bold")  # Set the font to Arial, larger size, and bold

# Increased spacing between the letters
letter_spacing = 40  # Set the spacing between letters

# Call the function to write text vertically with spacing
write_vertical(text_turtle, "VEGETA", vertical_font_style, letter_spacing)
text_turtle.hideturtle()  # Hide the turtle

# Function to draw a light ray from Vegeta's eye to a specific letter
def draw_light_ray(turtle, start_pos, end_pos):
    turtle.penup()
    turtle.goto(start_pos)
    turtle.pendown()
    turtle.goto(end_pos)

# Coordinates of Vegeta's eye (where the light ray will start)
eye_position = (185, -75)  # Set the coordinates of Vegeta's eye

# Create a turtle for drawing the light rays
ray_turtle = turtle.Turtle()  # Create a new turtle instance for drawing rays
ray_turtle.speed(20)  # Set the drawing speed of the turtle
ray_turtle.color("yellow")  # Set the color of the turtle to yellow

# Coordinates for the top of the 'V' and the bottom of the 'A' in "VEGETA"
v_position = (-250, 75)  # Set the coordinates for the top of the 'V'
a_position = (-250, -150)  # Set the coordinates for the bottom of the 'A'

# Draw the light rays to the 'V' and the 'A'
draw_light_ray(ray_turtle, eye_position, v_position)
draw_light_ray(ray_turtle, eye_position, a_position)

ray_turtle.hideturtle()  # Hide the turtle

# Function to draw a beam from Vegeta's eye to the letters 'V' and 'A'
def draw_beam(turtle, start_pos, v_pos, a_pos):
    turtle.penup()
    turtle.goto(start_pos)
    turtle.pendown()
    turtle.color("yellow")
    turtle.begin_fill()
    turtle.goto(v_pos)
    turtle.goto(a_pos)
    turtle.goto(start_pos)
    turtle.end_fill()

# Create a turtle for drawing the beam
beam_turtle = turtle.Turtle()  # Create a new turtle instance for drawing the beam
beam_turtle.speed(20)  # Set the drawing speed of the turtle
beam_turtle.hideturtle()  # Hide the turtle

# Draw the beam to the 'V' and the 'A'
draw_beam(beam_turtle, eye_position, v_position, a_position)

turtle.mainloop()  # Keep the turtle graphics window open
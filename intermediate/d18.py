# Day 18 - The Hirst Painting Project - 15/03/2025

import colorgram
import turtle as Turtle
import random
import os

print("Current working directory:", os.getcwd())

# Extract colors from the image (if needed, you can replace the image with a different jpg for different colors)
image_path = '.\\100-Days-of-Code\\intermediate\\packages\\d18\\hirst.jpg'

# Check if the file exists
if not os.path.exists(image_path):
    print(f"File not found: {image_path}")
else:
    colors = colorgram.extract(image_path, 30)
    rgb_colors = []
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        new_color = (r, g, b)
        rgb_colors.append(new_color)

    # Turtle setup
    Turtle.colormode(255)
    tim = Turtle.Turtle()
    tim.speed("fastest")
    tim.penup()
    tim.hideturtle()

    # Screen setup
    screen = Turtle.Screen()
    screen.title("Hirst Painting")

    # Calculate the starting position to center the dots
    num_dots_per_row = 10
    dot_size = 20
    spacing = 50
    total_width = (num_dots_per_row - 1) * spacing
    total_height = (num_dots_per_row - 1) * spacing
    start_x = -total_width // 2
    start_y = -total_height // 2
    tim.goto(start_x, start_y)

    # Draw dots
    for dot_count in range(1, 101):
        tim.dot(dot_size, random.choice(rgb_colors))
        tim.penup()
        tim.forward(spacing)

        if dot_count % num_dots_per_row == 0:
            start_y += spacing
            tim.goto(start_x, start_y)

    screen.exitonclick()
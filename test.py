# from turtle import Turtle, Screen

# timmy = Turtle()
# print(timmy)

# my_screen = Screen()
# my_screen.title("Turtle Graphics")
# my_screen.bgcolor("black")

# timmy.shape("turtle")
# timmy.color("pink")
# for i in range(8):
#     timmy.forward(100)
#     timmy.right(45)



# print(my_screen.canvheight)

# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander", "Bulbasaur"])
table.add_column("Type", ["Electric", "Water", "Fire", "Grass"])
table.align = "l"
print(table)
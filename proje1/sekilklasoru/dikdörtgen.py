import turtle

def draw_rectangle(width, height):
     width = int(input("Genişliği girin: "))
     height = int(input("Yüksekliği girin: "))
     draw_rectangle(width, height)
     for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
turtle.done() 
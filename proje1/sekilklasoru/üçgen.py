import turtle

def draw_triangle(side_length):
    side_length = int(input("Kenar uzunluğunu girin: "))
    draw_triangle(side_length)
    for _ in range(3):
        turtle.forward(side_length)
        turtle.left(120)
    turtle.done()
import turtle

def draw_square(side_length):
        side_length = int(input("Kenar uzunluğunu girin: "))
        draw_square(side_length)
        for _ in range(4):
            turtle.forward(side_length)
            turtle.left(90)
        turtle.done()
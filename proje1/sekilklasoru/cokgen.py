import turtle  

def draw_polygon(sides, side_length):
    sides = int(input("Çokgenin kenar sayısını girin: "))
    side_length = int(input("Kenar uzunluğunu girin: "))
    draw_polygon(sides, side_length)
    angle = 360 / sides
    for _ in range(sides):
        turtle.forward(side_length)
        turtle.left(angle)

    turtle.done()
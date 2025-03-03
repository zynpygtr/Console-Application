import turtle

def draw_star(size):
    size = int(input("Yıldızın boyutunu girin: "))
    draw_star(size)
    for _ in range(5):
        turtle.forward(size)
        turtle.right(144)
    turtle.done()
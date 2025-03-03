import turtle

def draw_circle(radius):
        radius = int(input("Yarıçapı girin: "))
        draw_circle(radius)
        turtle.penup()
        turtle.goto(0, -radius)  # Çevreyi düzgün çizmek için pozisyonu ayarla
        turtle.pendown()
        turtle.circle(radius)

        turtle.done()
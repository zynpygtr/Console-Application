import turtle

def sekilciz():

    # Şekil çizme fonksiyonları
    def draw_circle(radius):
        turtle.penup()
        turtle.goto(0, -radius)  # Çevreyi düzgün çizmek için pozisyonu ayarla
        turtle.pendown()
        turtle.circle(radius)

    def draw_square(side_length):
        for _ in range(4):
            turtle.forward(side_length)
            turtle.left(90)

    def draw_triangle(side_length):
        for _ in range(3):
            turtle.forward(side_length)
            turtle.left(120)

    def draw_rectangle(width, height):
        for _ in range(2):
            turtle.forward(width)
            turtle.left(90)
            turtle.forward(height)
            turtle.left(90)

    def draw_star(size):
        for _ in range(5):
            turtle.forward(size)
            turtle.right(144)

    def draw_polygon(sides, side_length):
        angle = 360 / sides
        for _ in range(sides):
            turtle.forward(side_length)
            turtle.left(angle)

    def main():
        turtle.speed(1)  # Çizim hızını ayarla
        
        # Kullanıcıdan şekil türü ve parametreler al
        print("Çizmek istediğiniz şekli seçin:")
        print("1. Daire")
        print("2. Kare")
        print("3. Üçgen")
        print("4. Dikdörtgen")
        print("5. Yıldız")
        print("6. Çokgen")
        
        choice = input("Seçiminizi yapın (1-6): ")

        if choice == "1":
            radius = int(input("Yarıçapı girin: "))
            draw_circle(radius)
        elif choice == "2":
            side_length = int(input("Kenar uzunluğunu girin: "))
            draw_square(side_length)
        elif choice == "3":
            side_length = int(input("Kenar uzunluğunu girin: "))
            draw_triangle(side_length)
        elif choice == "4":
            width = int(input("Genişliği girin: "))
            height = int(input("Yüksekliği girin: "))
            draw_rectangle(width, height)
        elif choice == "5":
            size = int(input("Yıldızın boyutunu girin: "))
            draw_star(size)
        elif choice == "6":
            sides = int(input("Çokgenin kenar sayısını girin: "))
            side_length = int(input("Kenar uzunluğunu girin: "))
            draw_polygon(sides, side_length)
        else:
            print("Geçersiz seçim!")

        # Çizimi bitir
        turtle.done()

    # Ana programı çalıştır
    if __name__ == "__main__":
        main()

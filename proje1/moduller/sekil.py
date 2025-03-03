import turtle
import sekilklasoru
import sekilklasoru.cokgen
import sekilklasoru.daire
import sekilklasoru.dikdörtgen
import sekilklasoru.kare
import sekilklasoru.yıldız
import sekilklasoru.üçgen


def sekilmenu():

    print("\033[1;32;40m")
    #print("╔"+"═"*20+"╗")
    print("╔═════════════════════╗")
    print("║\033[1;31;40m   Çizmek istediğiniz şekli seçin:   \033[1;32;40m  ║")
    print("║                     ║")
    print("║  1- Daire           ║")
    print("║  2- Kare            ║")
    print("║  3- Üçgen           ║")
    print("║  4- Dikdörtgen      ║")
    print("║  5- Yıldız          ║")
    print("║  6- Çokgen          ║")
    print("║                     ║")
    print("║    Seçimiz nedir?   ║")
    print("╚═════════════════════╝")
    # Şekil çizme fonksiyonları


    
      # Çizim hızını ayarla
        
        # Kullanıcıdan şekil türü ve parametreler al
       
        
    choice = input("Seçiminizi yapın (1-6): ")

    if choice == "1":
        sekilklasoru.daire()
    elif choice == "2":
        sekilklasoru.kare()   
    elif choice == "3":
        sekilklasoru.üçgen()
    elif choice == "4":
        sekilklasoru.dikdörtgen()
    elif choice == "5":
        sekilklasoru.yıldız()
    elif choice == "6":
        sekilklasoru.cokgen()
    else:
            print("Geçersiz seçim!")

        # Çizimi bitir
        

    # Ana programı çalıştır
    if __name__ == "__main__":
        sekilmenu()

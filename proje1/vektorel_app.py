import moduller.oyunlar
import moduller.hesapmenu
from moduller.oyunlar import *
# import moduller.hesapmenu as hm
#from moduller.hesapmenu import hmmenu
from moduller.hesapmenu import * # tüm fonksiyonlar.
import oyunlarklasoru.yilanoyunu

def anamenu():
    print("\033[1;32;40m")
    #print("╔"+"═"*20+"╗")
    print("╔═════════════════════╗")
    print("║\033[1;31;40m   VEKTOREL APP    \033[1;32;40m  ║")
    print("║                     ║")
    print("║  1-Oyunlar          ║")
    print("║  2-Hesap mak.       ║")
    print("║  3-Şekil Çizdirme   ║")
    print("║  4-Takvim           ║")
    print("║  5-Çarpım Tablosu   ║")
    print("║  6-Ritmik Sayma     ║")
    print("║  7-Not Hesaplama    ║")
    print("║  8-İdeal Kilo Hesap ║")
    print("║  9-Döviz Uygulaması ║")
    print("║  10-Sıcaklık Çevir  ║")
    print("║  11-Çıkış           ║")
    print("║                     ║")
    print("║    Seçimiz nedir?   ║")
    print("╚═════════════════════╝")
    secim = input()
    if secim == "1" : moduller.oyunlar.oyunmenu()
    # if secim == "2" : moduller.hesapmenu.hmmenu() # import moduller.hesammakinesi şeklinde kullanım için idi.
    # if secim == "2" : moduller.hesapmenu.hmmenu() # import moduller.hesammakinesi şeklinde kullanım için idi.
    if secim == "2" : moduller.hesapmenu.hmmenu()
    if secim == "9" : exit()
    else : anamenu()

# print(dir(moduller.oyunlar)) 
#print(dir(moduller.hesapmenu)) # modüllerin içindeki fonksiyonlar.
#help(moduller.hesapmenu.hmmenu
anamenu()
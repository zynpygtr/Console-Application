import hesapla.hesapmenu
import oyunlar.oyun
# import doviz.doviz_uygulamasi

def anamenu():
    
    print("╔═══════════════════════╗")
    print("║     Uygulamalar       ║")
    print("║                       ║")
    print("║  1-Hesap makinesi     ║")
    print("║  2-Oyunlar            ║")
    print("║  3-Alan Hesaplama     ║")
    print("║  4-Not Hesaplama      ║")
    print("║  5-Çarpım Tablosu     ║")
    print("║  6-Takvim             ║")
    print("║  7-Döviz Kurları      ║")
    print("║  8-Çıkış              ║")
    print("║                       ║")
    print("║    Seçimiz nedir?     ║")
    print("╚═══════════════════════╝")
    secim = input()
    if secim == "1":
        hesapla.hesapmenu.hmenu()
    elif secim == "2":
        oyunlar.oyun.oyunmenu()
    #elif secim == "3":
   #     alnhesaplama.alan_hesaplama.alan_hesapla()
    #elif secim == "4":
    #    nothesaplamamnu.nothp.not_hesapla()
    #elif secim == "5":
     #   carpımtb.carpim_tablosu.carpim_tablosu()
    #elif secim == "6":
     #   takvim.takvim_uygulamasi.takvim_goster()
    #elif secim == "7":
      #  doviz.doviz_uygulamasi.doviz_goster()
    #elif secim == "8":
     #   print("Çıkış yapılıyor...")
    #    return
    else:
        print("Geçersiz seçim, lütfen tekrar deneyin.")
    anamenu()

anamenu()
# ...
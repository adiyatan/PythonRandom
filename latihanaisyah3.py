print("Hai Selamat datang di KEI COOPERATION AND FOUNDATION")
pembeli = input("Masukkan nama Pembeli: ")
print ("Nama Pembeli :", pembeli) 

total1=0
jenis1=""
porsi=0
gelas=0

def fungsimakanan():
   global total1
   global porsi
   global jenis1
   print ("\n--Menu Makanan--")
   print("1. Magelangan - Rp9500")
   print("2. Mie Dok Dok - Rp8000")
   print("3. Omelet - Rp7000")
   nomor=int(input("Masukan Pilihan: "))
   porsi= int(input("Berapa Porsi: "))
   
   if nomor==1:
       total1=porsi*9500
       print (porsi," porsi Magelangan = Rp", total1)
       jenis1=("Magelangan")
   elif nomor==2:
       total1=porsi*8000
       print (porsi," porsi Mie Dok Dok = Rp", total1)
       jenis1=("Mie Dok Dok")
   elif nomor==3:
       total1=porsi*7000
       print (porsi, " porsi Omelet = Rp", total1)
       jenis1=("Omelet")
   else:
      print("Pilihan tidak ada, silakan masukkan lagi!")
      fungsimakanan()


fungsimakanan()

total2=0
jenis2=""

def fungsiminuman():
   global total2
   global jenis2
   global gelas
   print("\n--Menu Minuman--")
   print("1. Es teh - Rp2500")
   print("2. Es Susu - Rp3500")
   print("3. Es Jahe - Rp5000")
   nomor=int(input("Masukan Pilihan: "))
   gelas= int(input("Berapa Gelas: "))

   if nomor==1:
       total2=gelas*2500
       print (gelas," Es Teh = Rp", total2)
       jenis2=(" Gelas Es Teh")
   elif nomor==2:
       total2=gelas*3500
       print (gelas, " Gelas Es Susu = Rp", total2)
       jenis2=("Es Susu")
   elif nomor==3:
       total2=gelas*5000
       print (gelas, " Gelas Es Jahe = Rp", total2)
       jenis2=("Es Jahe")
   else:
      print("Pilihan tidak ada, silahkan masukan lagi!!")
      fungsiminuman()


fungsiminuman()
    
totalsemua=0
totalsemua=total1+total2
print("\nTotal harus Dibayar: Rp",totalsemua)
uang=int(input("Uang Tunai Pembeli: Rp."))
kembalian=int(uang-totalsemua)
print("Kembalian :",kembalian)


na1 = (" Nama         :",pembeli, "\n")
na2 = (" Beli         :",str(porsi),str(jenis1),"-", str(total1),"\n")
na3 = ("               ",str(gelas),str(jenis2),"-", str(total2),"\n")
na4 = (" Tagihan      : Rp.",str(totalsemua),"\n")
na5 = (" Uang         : Rp.",str(uang),"\n")
na6 = (" Kembalian    : Rp.",str(kembalian),"\n")

import _pickle as pickle
with open ('invoice.txt', 'w') as file:
    
    file.write ("=================================\n") 
    file.write("======= S T R U K   B E L I =====\n")
    file.write("=================================\n")
    file.write (" ".join(na1))
    file.write (" ".join(na2))
    file.write (" ".join(na3))
    file.write (" ".join(na4))
    file.write (" ".join(na5))
    file.write (" ".join(na6))
    file.write("=================================\n")
    file.write("=================================")


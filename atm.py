judul = "ATM".center(20,'=')
print(""+ judul +"")

print(r""" PILIH OPTION :
1 = 1. check uang saya
2 = 2. ambil uang saya
3 = 3. tabung uang saya
""")

option = int(input("silahkan pilih option :"))
if option==1:
    print("uang kamu berjumlah Rp.200.000")
elif option==2:
    print("uang kamu berjumlah Rp.200.000, berapakah uang yang akan anda ambil")
    print("1. Rp.50.000")
    print("2. Rp.100.000")
    uang_kamu = 200000
    option2 = int(input("option :"))
    if option2==1:
        hasil = uang_kamu - 50000
        print("uang kamu sekarang berjumlah:  Rp.", hasil)
    elif option2==2:
        hasil = uang_kamu - 100000
        print("uang kamu sekarang berjumlah:  Rp.", hasil)
elif option==3:
    uang_kamu = 200000
    print("uang berjumlah Rp.200.000,berapakah uang yang anda ingin tabungkan?")
    option5 =int(input("masukan jumlah uang :"))
    hasil3 = uang_kamu + option5
    print("jumlah uang kamu sekarang adalah: Rp.", hasil3)
else:
    print("keyword anda salah, mohon coba lagi")
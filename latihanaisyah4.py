# APlIKASI FISIKA BAB ENERGI POTENSIAL
# fungsi yang tersedia :
# 1. Menghitung Energi Potensial
# 2. Menghitung Massa
# 3. Menghitung Percepatan Gravitasi
# 4. Menghitung Ketinggian
# 5. Kembali ke Menu
# 6. Keluar
#
# by A710200104 Huda Aisyah Khoirunissa 

rumus = 'EPoten = m*g*h'
class EPoten :
    def menu(self):
        menu = '''
        <<< ENERGI POTENSIAL >>>
        haloo amigos!!, kalian bakal cerdas EP bersama Physton, yuk pilih salah satu
        [1] Menghitung Energi Potensial
        [2] Menghitung massa benda
        [3] Menghitung percepatan gravitasi
        [4] Menghitung ketinggian
        [5] EXIT
        '''
        return menu
    def menghitung_Ep(self, massa, gravitasi, ketinggian):
        hasil = int(massa)*int(gravitasi)*int(ketinggian)
        return hasil
    def menghitung_massa(self, EP, gravitasi, ketinggian):
        hasil = int(EP)/(int(gravitasi)*int(ketinggian))
        return hasil
    def menghitung_gravitasi(self, EP, massa, ketinggian):
        hasil = int(EP)/(int(massa)*int(ketinggian))
        return hasil
    def menghitung_tinggi(self, EP, massa, gravitasi):
        hasil = int(EP)/(int(massa)*int(gravitasi))
        return hasil

while True :
    print(EPoten().menu())
    pilih = input('Pilih nomor sesuai kebutuhan : ')
    if pilih == '1' :
        print('Siap, Physton akan menghitung Energi Potensial')
        while True :
            benda = input('Masukkan nama benda : ')
            massa = input('Masukkan nilai massa (dalam kg) : ')
            gravitasi = input('Masukkan nilai gravitasi   : ')
            ketinggian = input('Masukkan nilai ketinggian (dalam meter) : ')
            hasil_energi = f'besar energi Energi Potensial {benda} tersebut yang memiliki {massa} kg kemudiann percepatan gravitasi {gravitasi} dalam {ketinggian}meter adalah {EPoten().menghitung_Ep(massa=massa, gravitasi=gravitasi, ketinggian=ketinggian)} Joule'
            print(hasil_energi)
            print('[1] Lagi \n[2] Kembali')
            pilih2 = input('Saya pilih : ')
            if pilih == '1' : continue
            else : break

    elif pilih == '2':
        print('Siap, Physton akan menghitung massa')
        while True:
            benda = input('Masukkan nama benda : ')
            EP = input('Masukkan nilai energi potensial (dalam Joule) : ')
            gravitasi = input('Masukkan nilai gravitasi   : ')
            ketinggian = input('Masukkan nilai ketinggian (dalam meter) : ')
            hasil_massa = f'besar massa {benda} tersebut yang memiliki energi potensial {EP} Joule kemudian percepatan gravitasi {gravitasi} dalam {ketinggian}meter adalah {EPoten().menghitung_massa(EP=EP, gravitasi=gravitasi, ketinggian=ketinggian)} Kg'
            print(hasil_massa)
            print('[1] Lagi \n[2] Kembali')
            pilih2 = input('Saya pilih : ')
            if pilih2 == '1': continue
            else : break
    elif pilih == '3' :
        print('Siap, Physton akan menghitung percepatan gravitasi')
        while True:
            benda = input('Masukkan nama benda : ')
            EP = input('Masukkan nilai energi potensial (dalam Joule) : ')
            massa = input('Masukkan massa   : ')
            ketinggian = input('Masukkan nilai ketinggian (dalam meter) : ')
            hasil_gravitasi = f'besar gravitasi {benda} tersebut yang memiliki energi potensial {EP} Joule kemudian massanya {massa} dalam {ketinggian}meter adalah {EPoten().menghitung_gravitasi(EP=EP, massa=massa, ketinggian=ketinggian)}'
            print(hasil_gravitasi)
            print('[1] Lagi \n[2] Kembali')
            pilih2 = input('Saya pilih : ')
            if pilih3 == '1': continue
            else : break
    elif pilih == '4' :
        print('Siap, Physton akan menghitung ketinggian benda')
        while True:
            benda = input('Masukkan nama benda : ')
            EP = input('Masukkan nilai energi potensial (dalam Joule) : ')
            massa = input('Masukkan massa   : ')
            gravitasi = input('Masukkan nilai gravitasi  : ')
            hasil_ketinggian = f'besar ketinggian {benda} tersebut yang memiliki energi potensial {EP} Joule kemudian massanya {massa} dan memiliki percepatan gravitasi {gravitasi} adalah {EPoten().menghitung_tinggi(EP=EP, massa=massa, gravitasi=gravitasi)}meter'
            print(hasil_ketinggian)
            print('[1] Lagi \n[2] Kembali')
            pilih2 = input('Saya pilih : ')
            if pilih4 == '1': continue
            else : break
    else : break


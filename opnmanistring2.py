#UPPER
salam = "hey"
print("normal " + salam)
salam = salam.upper()
print("upper " + salam)
#LOWER
alay = "AKU KECE ABIEZZZ"
print("normal " + alay)
alay = alay.lower()
print("lower " + alay) 
#isX
salam = "sis"
apakah_lower = salam.islower()
print(salam + " is lower = " + str(apakah_lower))
apakah_upper = salam.isupper()
print(salam + " is upper = " + str(apakah_upper))

#isalpha = huruf
#isnum = huruf dan angka
#isdecimal = angka 
#isspace = spasi,tab,newline,\n
#istitle = semua kata dimulai dengan hrf besar

judul = "Attack On Titan"
cek_judul = judul.istitle()
print(judul + " is title = " + str(cek_judul))

# startwith n endwith
cek_start = "Sangjangnim Oppa".startswith("Sangjangnim")
print("start = " + str(cek_start))

cek_end = "Sangjangnim Oppa".endswith("Oppa")
print("end = " + str(cek_end))

pisah = ['aku','sayang','kamu']
gabung = ",".join(pisah)
print(pisah)
print(gabung)

gabung = ' '.join(pisah)
print(gabung)

gabung = 'tos'.join(pisah)
print(gabung)

gabung = "akutossayangtoskamu"
print(gabung.split('tos'))

#alokasi rjust,ljust,xebter
print(5*"=" + "data" + "="*5)

kanan = "kanan".rjust(10)
print("'"+kanan+"'")
kiri = "kiri".ljust(10)
print("'"+kiri+"'")
tengah = "tengah".center(20)
print("'"+tengah+"'")
tengah = "tengah".center(20,"-")
print("'"+tengah+"'")

#STRIP
tengah = tengah.strip("-")
print("'"+tengah+"'")
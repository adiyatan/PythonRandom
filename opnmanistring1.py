nama_awal = "rakean"
nama_tengah = "tanaya"
nama_akhir = "permana"
nama_lengkap = nama_awal + " " + nama_tengah + " " + nama_akhir
print(nama_lengkap)

panjang = len(nama_lengkap)
print("panjang dari " + nama_lengkap + " = " + str(panjang))

a = "a"
status = a in nama_lengkap
print(a + " ada di" + " " + nama_lengkap + " = " + str(status))


A = "A"
status = A not in nama_lengkap
print(A + " tidak ada di " + " " + nama_lengkap + " = " + str(status))

print("index ke-0 : " + nama_lengkap[0])
print("index ke-0 : " + nama_lengkap[14])
print("index ke-0 : " + nama_lengkap[8])
print("index ke-(-1) : " + nama_lengkap[-1])
print("index ke-(-1) : " + nama_lengkap[-14])
print("index ke-(0:9) : " + nama_lengkap[0:10])
print("index ke-(2:3) : " + nama_lengkap[2:4])
print("index ke-(0,2,4,6,8,10) : " + nama_lengkap[0:11:2])

print("paling kecil : " + min(nama_lengkap))
print("paling besar : " + max(nama_lengkap))

ascii_code = ord(" ")
print("ascii code untuk spasi adalah " + str(ascii_code))
ascii_code = ord(",")
print("ascii code untuk koma adalah " + str(ascii_code))
data = 117
print("char untuk ascii 117 adalah " + chr(data))

data = "gaylang adalah gilang"
jumlah = data.count("a")
print("jumlah a pada " + data + " = " + str(jumlah))


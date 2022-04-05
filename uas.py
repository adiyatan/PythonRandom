judul = "UAS".center(20,'=')
print(""+ judul +"")

print("\nLIST PROGRAM PRAKDASPRO\n")
print(r"""
1 = 1.program luas dan keliling lingkaran
2 = 2.Program pengurutan menaik
3 = 3.Program pencarian data dengan sequential search
""")

program_luas_dan_keliling_lingkaran = float(input('masukan jari jari lingkaran untuk mencari No.1: '))
print("jari jari adalah",program_luas_dan_keliling_lingkaran, "cm")

luas_lingkaran = (22/7) * program_luas_dan_keliling_lingkaran * program_luas_dan_keliling_lingkaran
print("luas lingkaran = ",luas_lingkaran, "cm")
keliling_lingkaran = 2 * (22/7) * program_luas_dan_keliling_lingkaran
print("keliling lingkaran = ",keliling_lingkaran, "cm")
try:
    bil = int(input("masukkan bilangan : "))

    # jika bilangan genap
    if (bil % 2 == 0):

        # jika bilangan diantara 2-5
        if (bil < 5):
            print("angka tidak keramat")

        # jika bilangan diantara 6-20
        elif (bil == 6 and bil < 20):
            print("angka keramat")
        elif (bil > 20) :
            print('angka keramat')

        else:
            print("angka keramat")

    # jika bilangan ganjil
    else:
       if(bil <= 3 and bil <= 5) :
           print('angka keramat')
       elif(bil > 6 and bil < 20):
           print('angka keramat')
       elif(bil > 20) :
           print('angka keramat')
       else :
           print('angka tidak keramat')
except:
    print("angka  keramat")

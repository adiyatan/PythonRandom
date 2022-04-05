# ++++++++3------10+++++++++
inputuser = float(input("masukan angka yang bernilai\nkurang dari 3 \natau lebih \nbesar dari 10\n="))

iskurangdari = (inputuser < 3)
print("kurang dari 3 =", iskurangdari)

islebihdari = (inputuser > 10)
print("lebih dari 10 =", islebihdari)

iscorrect = iskurangdari or islebihdari
print("angka yang anda masukan; ", iscorrect)

#--------3++++++++10--------
print("\n",10*"=","\n")
inputuser = float(input("masukan angka yang bernilai\nlebih dari 3 \ndan \nkurang dari 10\n="))
islebihdari = inputuser > 3
print("lebih dari 3 = ", islebihdari)

iskurangdari = (inputuser < 10)
print("kurang dari 10 =", iskurangdari)

iscorrect = islebihdari and iskurangdari
print("angka yang anda masukan; ", iscorrect)
















def kabisat(a):
  if a % 400 == 0:
    return True
  elif a % 100 == 0:
    return False
  elif a % 4 == 0:
    return True
  else:
    return False

tahun = int(input("masukkan tahun :"))

if kabisat(tahun):
  print("true")
else:
  print("false")
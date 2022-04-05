#tipe : int,float,str,bool


#INT
print("========int========")
data_int = 9;
print("data =", data_int, ",type=",type(data_int))

data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int) #akan false bia int = 0
print("data =", data_float, ",type=",type(data_float))
print("data =", data_str, ",type=",type(data_str))
print("data =", data_bool, ",type=",type(data_bool))


#float
print("=========float===========")
data_float = 9.9;
print("data =", data_float, ",type=",type(data_float))

data_int = int(data_float)#bulat ke bwh
data_str = str(data_float)
data_bool = bool(data_float) #akan false bia float = 0
print("data =", data_int, ",type=",type(data_int))
print("data =", data_str, ",type=",type(data_str))
print("data =", data_bool, ",type=",type(data_bool))

#boolean
print("=========bolean===========")
data_bool = False;
print("data =", data_bool, ",type=",type(data_bool))

data_int = int(data_bool)#bulat ke bwh
data_str = str(data_bool)
data_float = float(data_bool) #akan false bia float = 0
print("data =", data_int, ",type=",type(data_int))
print("data =", data_str, ",type=",type(data_str))
print("data =", data_float, ",type=",type(data_float))


#str

print("=========str===========")
data_str = "10";
print("data =", data_str, ",type=",type(data_str))

data_int = int(data_str)# harus angka
data_bool = bool(data_str)
data_float = float(data_str)#Flse klo kosong
print("data =", data_int, ",type=",type(data_int))
print("data =", data_bool, ",type=",type(data_bool))
print("data =", data_float, ",type=",type(data_float))
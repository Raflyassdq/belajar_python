# #VARIABEL adalah tempat menyimpan data

# # Menaruh/assigment nilai
# a =10
# x=5
# panjang =10

# #Pemanggilan
# print("nilai a =", a)
# print("nilai x =", x)
# print("nilai panjang =", panjang)

# #penamaan
# nilai_y = 15 #dengan menggunakan underscore
# juta10 = 1000000 #ini boleh, yang ga boleh pake spasi
# nilaiZ = "sda" #ini boleh 

# #pemanggilan kedua 
# print("nilai y =", nilai_y)
# print("nilai juta10 =", juta10)
# print("nilai Z =", nilaiZ)

# #assigment indirect
# b = a
# print ("nilai b = ", b)


#TIPE DATA

# 1.) Integer, Angka yang tidak ada komanya
# data_integer = 32424
# print("data integer:", data_integer)
# print("bertipe:", type(data_integer))

# # 2.) Float, Angka yang ada titiknya, kalau ada koma nya berarti tuple
# data_float = 3.5
# print("data float:", data_float)
# print("bertipe:", type(data_float))

# # 3.) String, Angka yang ada hurufnya
# data_string = "belajar dasar"
# print("data string:", data_string)
# print("bertipe:", type(data_string))

# # 4.) Boolean, Angka biner dengan trua/false
# data_bool = False
# print("data boolean:", data_bool)
# print("bertipe:", type(data_bool))


#CASTING
# merubah dari satu data ke tipe data lain
# tipe data = int, float, str, bool

# #INTEGER 
# print('======INTEGER======')
# data_int = 9;
# print("data=", data_int, "tipe=", type(data_int))

# data_float = float(data_int)
# data_str = str(data_int)
# data_bool = bool(data_int) #akan false jika nilainya = 0
# print("data:", data_float, ",type:",type(data_float))
# print("data:", data_str, "type:", type(data_str))     
# print("data:", data_bool, "type:", type(data_bool))

#FLOAT
print('======FLOAT======')
data_float = 0;
print("data=", data_float, ",type=", type(data_float))

data_int = int(data_float) #akan dibulatkan kebawah
data_str = str(data_float)
data_bool = bool(data_float) #akan false jika nilai 0
print("data", data_int, "type=", type(data_int))
print("data", data_str, "type=", type(data_str))
print("data", data_bool, "type=", type(data_bool))

#BOOLEAN
print ('======BOOLEAN======')
data_bool = True
print("data=", data_bool, "type", type(data_bool))

data_int = int(data_bool)
data_float = float(data_bool)
data_str = str(data_bool)
print("data=", data_int, "type", type(data_int))
print("data=", data_float, "type", type(data_float))
print("data=", data_str, "type", type(data_str))

#STRING
print ('======STRING======')
data_str = "10"
print("data=", data_str, "type", type(data_str))

data_int = int(data_str)
data_float = float(data_str)
data_bool = bool(data_str)
print("data=", data_int, "type", type(data_int))
print("data=", data_float, "type", type(data_float))
print("data=", data_bool, "type", type(data_bool))

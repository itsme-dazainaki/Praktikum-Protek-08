def dataStat(x): 
    a = sum(x) / len(x) #hitung rata rata
    b = max(x) #hitung nlai paling besar
    c = min(x) #hitung nilai paling kecil

    print("Rata-rata, Nilai Maksimal, Nilai minimal") 
    datadef = [a,b,c] #panggil function
    return datadef #kembalikan untuk simpan nilai datadef

try: #tandai box yang akan dicek exception
   inputan = int(input("Berapa data yang ingin diinput ? : ")) #inputkan data bertype int

    bil = 0 #nilai awal bil
    data = [] #bahwa data adalah list
    while bil < inputan : #ini untuk perulangan
        angka = int(input("Masukkan bilangan ke {} : ".format(bil+1))) #inputkan urutan data
        data.append(angka) #tambahkan angka ke list data
        bil += 1 #increment

    data.sort(reverse=True)#mengurutkan secara descending
    print("Berikut hasil pengurutannya dari yang terbesar : ", data) #print hasilnya

except ValueError:  #exception handling jika terjadi valueerror
    print("Maaf ! tipe data yang anda inputkan salah") #tampilkan pesan error 

printData = dataStat(data)
print(printData)
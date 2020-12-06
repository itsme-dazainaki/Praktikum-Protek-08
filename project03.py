try : #tandai blok yang akan dicek exception
    inputan = int(input("Berapa data yang ingin diinput ? : ")) #untuk menginput jumlah nama 

    bil = 0 #niali awal bil
    data = [] #bahwa data adalah list
    while bil < inputan :
        nama = str(input("Masukkan Nama ke {} : ".format(bil+1))) #inputkan urutan data
        data.append(nama) #tambahkan angka ke list data
        bil += 1 #increment

    data.sort() #mengurutkan secara ascending
    
    print("Berikut Data Nama Mahasiswa dan banyaknya karakter penyusunnya : ")
    for nama in data : 
        print("{} ({} karakter)".format(nama,len(tuple(nama)))) #tampilkan huruf penyusun data nama

except ValueError:  #exception handling jika terjadi valueerror
    print("Maaf ! tipe data yang anda inputkan salah") #tampilkan pesan error 

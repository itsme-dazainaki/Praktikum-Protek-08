def a(): #deklarasikan function
    tmbhsayur = input("Masukkan Nama Sayur :  ").lower() #inputkan data 
    datasayur.append(tmbhsayur) #tambahkan data ke list datasayur
    print (datasayur) #tampilkan data yg telah ditambah

def b(): #deklarasikan function
    hpssayur = input("Masukkan Nama Sayur yang ingin dihapus : ").lower()
    try: #tandai blok yang akan dicek exception
            datasayur.remove(hpssayur) #hapus data yg dimasukkan dari list data sayur
            print("Data berhasil dihapus ({})".format(hpssayur)) #konfirmasi bahwa data berhasil dihapus
    except ValueError: #exception handling jika terjadi valueerror
            print("Maaf ! Data tidak tidak ditemukan ({})".format(hpssayur)) #tampilkan pesan error
    print(datasayur) #tampilkan data yg telah dikurangi

def c(): #deklarasikan function
    print(datasayur) #tampilkan isi list

datasayur = ['bayam', 'kangkung', 'wortel', 'selada'] #list data

try : #tandai blok yang akan dicek exception
    lagi = "y" #nilai awal lagi untukp perulangan
    while lagi =="y" : #perulangan 
        print("--------------------------")
        print("Menu : ")
        print("a : Tambah Data Sayur")
        print("b : Hapus Data Sayur ")
        print("c : Lihat Data Sayur")
        print("--------------------------")
        inputan = str(input("Pilihan anda : ")) #input data
        print("--------------------------")
        
        if(inputan == 'a'): #cek inputan
            a() #panggil function a
        elif (inputan == 'b'):
            b() #panggil function b
        elif(inputan == 'c'):
            c() #panggil function c
            
        print("---------------------------------")
        lagi = str(input("Pilih lagi (y/n) ? : ")) #konfirmasi apakah ingin mengulang 

except ValueError: #exception handling jika terjadi valueerror
    print("Maaf ! Inputan anda salah") #tampilkan pesan error 
try :
    buah = {"apel" : 5000, "jeruk" : 8500, "mangga" : 7800, "duku" : 6500}
    print("------------------------------")
    print("Kami Menyediakan Buah : ")
    for a,b in buah.items():
        print('-',a,':',b)
    print("------------------------------")

    def jumlah(namabuah) :        
        jumlah = int(input("Berapa Kg ? : ")) 
        harga = buah.get(namabuah, 0)*jumlah
        return harga

    def beli(buahdict) :       
        hargasemua = []
        lanjut = True
            
        while(lanjut==True) :    
            print(" ")            
            namabuah = input("Nama Buah Yang Ingin dibeli : ").lower()                
            if(namabuah not in buahdict.keys()) :
                print("Maaf ! Buah yang anda masukkan tidak ada")
                continue                        
            else :
                try :
                    harga = jumlah(namabuah)
                    hargasemua.append(harga)                        
                    lagi = input("Apakah Anda Ingin Membeli Buah Lain (y/n) ? ").lower()
                    if(lagi=="y") :
                        lanjut = True                        
                    elif(lagi=="n") :
                        lanjut = False
                    else :
                        print("Maaf ! Pilihan yang anda masukkan invalid")
                        break                    
                except ValueError :
                        print("Maaf ! Inputan yang anda masukkan invalid")
                        continue              
        print("-------------------------------------------")
        print("Total Harga : ", sum(hargasemua))

    def tambah(buahdict) :
        namabaru = input("Masukkan nama buah yang ingin ditambahkan : ").lower()
        while True :
            try : 
                if(namabaru in buahdict.keys()) :
                    print("Buah ", namabaru, "sudah ada di dalam data. Anda bisa mengubah harganya, silahkan beri harga yg baru !")
                    hargabaru = int(input("Masukkan harga per Kg : "))                    
                    dictbaru = {namabaru : hargabaru}
                    buahdict.update(dictbaru)
                    
                    print("Data Buah : ")
                    for x,y in buahdict.items() :
                        print("- ", x, "(harga : ", y, ")")
                else :
                    hargabaru = int(input("Masukkan harga per Kg : "))
                    buah[namabaru] = hargabaru
                    
                    print("Data Buah : ")
                    for x,y in buahdict.items() :
                        print("- ", x, "(harga : ", y, ")")
                break

            except ValueError :
                print("Maaf ! Harga yang anda masukkan invalid")
                continue

    def hapus(buahdict) :
        print(" ")
        hapusbuah = input("Masukkan nama buah yang ingin anda hapus : ").lower()
        if(hapusbuah in buahdict.keys()) :
            del buahdict[hapusbuah]
            print("Buah ", hapusbuah, "berhasil dihapus !")
            
            print("Data Buah : ")
            for x,y in buahdict.items() :
                print("- ", x, "(harga : ", y, ")")

        else :
            print("Maaf ! Buah yang anda masukkan tidak ditemukan")


    print("Menu: ")
    print("a. Tambah data buah")
    print("b. Beli buah")  
    print("c. Hapus data buah")
    while True :
        print("------------------------------")
        pilih = input("Masukkan Pilihan Anda : ").lower()        
        if(pilih == 'a') :
            tambah(buah)                        
        elif(pilih == 'b') :
            beli(buah)
        elif(pilih == 'c') :
            hapus(buah)           
        else :
            print("Inputan Invalid")
            continue

except ValueError : 
    print("Maaf ! Tipe Data yang anda masukkan salah")
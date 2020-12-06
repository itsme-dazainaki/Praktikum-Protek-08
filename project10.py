try :
    buah = {"apel" : 5000, "jeruk" : 8500, "mangga" : 7800, "duku" : 6500}
    print("------------------------------")
    print("Kami Menyediakan Buah : ")
    for a,b in buah.items():
        print('-',a,':',b)
    print("------------------------------")

    hargasemua = 0
    while True :
        nama = str(input("Nama Buah Yang Ingin dibeli : "))
        if nama in buah:            
            banyak = float(input("Berapa Kg ? : "))
            harga = buah.get(nama,0)
            total = banyak*harga
            hargasemua += total
            lagi = str(input("Apakah Anda Ingin Membeli Buah Lain (y/n) ? "))
            print(" ")

            if (lagi == "y"):
                continue
            print("------------------------------")
            print("Total Harga Buah : ", hargasemua)
            print("------------------------------")
            break
        else :
            print("Maaf ! Buah yang anda  inginkan belum tersedia")
   
except ValueError : 
    print("Maaf ! Tipe Data yang anda masukkan salah")
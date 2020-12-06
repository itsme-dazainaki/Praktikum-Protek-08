try :
    buah = {"apel" : 5000, "jeruk" : 8500, "mangga" : 7800, "duku" : 6500}
    print("------------------------------")
    print("Kami Menyediakan Buah : ")
    for a,b in buah.items():
        print('-',a,':',b)
    print("------------------------------")

    nama = str(input("Nama Buah Yang Ingin dibeli : "))
    
    ada = nama in buah
    a = True
    if ada:
        while(a==True):
            banyak = float(input("Berapa Kg ? : "))
            harga = buah.get(nama,0)
            total = banyak*harga
            print("------------------------------")
            print("Total Harga Buah : ", total)
            print("------------------------------")
            break
    else :
        print("Maaf ! Buah yang anda  inginkan belum tersedia")
   
except ValueError : 
    print("Maaf ! Tipe Data yang anda masukkan salah")
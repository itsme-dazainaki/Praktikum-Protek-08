def kuadrat(bil): #deklarasikan function
    for i in range(len(bil)): #untuk bilangan 
        bil[i] **=2 #ini rumus kuadrat
    return bil #kembalikan agar bisa simpan nilai

try : #tandai blok yang akan dicek exception
    inputan = int(input("Berapa data yang ingin diinput ? : "))
        
    data = [] #bahwa data adalah sebuah list
    jum = 0 #nilai awal jum
    for i in range(inputan): #untuk data sejumlah angka yg tadi diinputkan
        angka = int(input("Masukkan bilangan ke {} : ".format(jum+1))) #inputkan angka, dan nomor bilangan
        data.append(angka) #masukkan angka ke list data
        jum += 1 #increment

    print("Kuadrat dari data tersebut : ") 
    print(kuadrat(data)) #tampilkan hasil angka yang telah dikuadratkan
except ValueError: #exception handling jika terjadi valueerror
    print("Maaf ! Tipe data yang anda masukkan salah") #tampilkan pesan error 
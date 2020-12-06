def sortStringByChar(myData): #deklarasikan function
    myData.sort(reverse=True) #urutkan data dalam list secara descending
    return myData #kembalikan untuk menyimpan nilai

myData=["apel","rambutan","jeruk"] #ini list
buah = sortStringByChar(myData) #urutkan berdasar jumlah karakter penyusun

print("Data baru yang telah diurutkan : ", buah) #tampilkan data yang telah disortir

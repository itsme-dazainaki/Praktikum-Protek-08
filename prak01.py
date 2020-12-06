a = [1, 5, 6, 3, 6, 9, 11, 20, 12] #ini adalah isi data yang ada di list
b = [7, 4, 5, 6, 7, 1, 12, 5, 9] #ini adalah isi data yang ada di list
#no 2
a.insert(3,10) #untuk menyisipkan ke indeks ke 3 nilai 10
b.insert(2,15) #untuk menyisipkan ke indeks ke 3 nilai 15
#no 3
a.append(4) #untuk menambahkan nilai 4 setalah data terakhir
b.append(8) #untuk menambahkan nilai 8 setalah data terakhir
#no 4
a.sort() #untuk mengurutkan data secara ascending
b.sort() #untuk mengurutkan data secara ascending
#no 5
c = a[0:7] #membuat list baru (c) dengan nilai berasal dari list sebelumnya (a)
d = b[2:9] #membuat list baru (d) dengan nilai berasal dari list sebelumnya (b)
#no 6
e = [] #mari membuat list
for i in range(len(d)): #ini buat perulangan data dari c dan d yang mau diolah
    e += [c[i]+d[i]] #ini rumusnya
#no 7
e = tuple(e) #mengubah data menjadi tuple
#no 8
minim = min(e) #mencari nilai min
maks = max (e) #mancari nilai maksimal
jdata = sum(e) #mencari jumlad dari seluruh data di e
#no 9
myString = "python adalah bahasa pemrograman yang menyenangkan"
#no 10
myStringSet = set(myString) #tentukan karakter penyusun string
#no 11
myStringSetList = list(myStringSet) #untuk menjadikan myStringSet ke list


print(a,b,c,d,e)
print("Nilai minimal : ", minim) #no 8
print("Nilai maksimal : ", maks) #no 8
print("Jumlah seluruh data : ", jdata ) #no 8
print("Kalimat : ", myString) #no 9
print("Disusun dari huruf : ", myStringSet) #no 10
print("List dari myStringSet : ", myStringSetList)
#no 11
myStringSetList.sort()
print("Berikut urutannya setelah disorting : ", myStringSetList) 
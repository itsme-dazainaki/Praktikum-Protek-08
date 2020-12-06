def rata(dicti):
     harga = tuple(dicti.values())
     rata = sum(harga)/len(harga)
     return rata

buah = {"apel" : 5000, "jeruk" : 8500, "mangga" : 7800, "duku" : 6500}
print("Rata-rata harga satuan dari seluruh buah : ", rata(buah))

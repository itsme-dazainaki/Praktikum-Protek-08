def mahalsangat(dicti):
    listDicti = list(dicti.values())
    listDicti.sort(reverse=True)

    for a,b in dicti.items():
        if(listDicti[0]==b):
            return a

buah = {"apel" : 5000, "jeruk" : 8500, "mangga" : 7800, "duku" : 6500}
print("Buah yang harganya paling mahal : ", mahalsangat(buah))

def nilaitertinggi(listnilai) :
    mid = []
    uas = []
    nilaiAkhir = []
    tertinggi = {}
    for hasil in listnilai :
        hasil = (hasil['mid'] + (2 * hasil['uas'])) / 3
        nilaiAkhir.append(hasil)

    tertinggi = nilaiAkhir.index(max(nilaiAkhir))    
    a = {'nim' : listnilai[tertinggi]['nim'],'nama' : listnilai[tertinggi]['nama']}    
    print("Mahasiswa dengan nilai tertinggi yaitu", a['nama'], "NIM", a['nim'])

nilaiMhs = [{'nim' : 'A01', 'nama' : 'Amir', 'mid' : 50, 'uas' : 80},
            {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90},
            {'nim' : 'A03', 'nama' : 'Cici', 'mid' : 50, 'uas' : 50},
            {'nim' : 'A04', 'nama' : 'Dedi', 'mid' : 20, 'uas' : 30},
            {'nim' : 'A05', 'nama' : 'Fifi', 'mid' : 70, 'uas' : 40}]

nilaitertinggi(nilaiMhs)


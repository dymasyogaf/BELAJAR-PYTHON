tagihan = [50000, 75000, -150000,12500, 300000, -50000, 200000]
i = 0
jumlah_tagihan = len(tagihan)
total_tagihan = 0
while i < jumlah_tagihan:
    if tagihan[i] < 0:
        total_tagihan = -1
        print(" terdapat angka minus dalam tagihan, perhitungan dihentikan!")
        break
    total_tagihan += tagihan [i]
    i += 1
print(total_tagihan)
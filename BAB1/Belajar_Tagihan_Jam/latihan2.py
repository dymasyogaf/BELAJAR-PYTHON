# Data
uang_jalan = 1500000  # Biaya per mobil per hari
jumlah_hari = 31  # Jumlah hari dalam sebulan
list_plat_nomor = [8993, 2198, 2501, 2735, 3772, 4837, 9152]

# Pengecekan kendaraan dengan nomor pelat ganjil atau genap
# Deklarasikan kendaraan_genap dan kendaraan_ganjil
kendaraan_genap = 0
kendaraan_ganjil = 0

for plat_nomor in list_plat_nomor:
    if plat_nomor % 2 == 0:
        kendaraan_genap += 1  # Hitung jumlah kendaraan genap
    else:
        kendaraan_ganjil += 1  # Hitung jumlah kendaraan ganjil

# Total pengeluaran untuk kendaraan dengan nomor pelat ganjil dan genap dalam 1 bulan
i = 1  # Hari dimulai dari 1
total_pengeluaran = 0

while i <= jumlah_hari:
    if i % 2 == 0:  # Hari genap
        total_pengeluaran += kendaraan_genap * uang_jalan
    else:  # Hari ganjil
        total_pengeluaran += kendaraan_ganjil * uang_jalan
    i += 1

# Cetak total pengeluaran
print('Jumlah Kendaraan Genap', kendaraan_genap)
print('Jumlah Kendaraan Ganjil', kendaraan_ganjil)
print('Total Pengeluaran dalam 1 Bulan:', total_pengeluaran)
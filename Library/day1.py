## 📚 Studi Kasus Pandas: "Film Favorit Lintas Generasi"
#🎯 Latar Belakang:
# Kamu bekerja sebagai data analyst di sebuah platform streaming film.
# Atasanmu ingin tahu film-film terbaik berdasarkan dekade rilis dan 
# bagaimana preferensi genre berubah dari tahun ke tahun.
# 📝 Pertanyaan yang Harus Kamu Jawab:
# Berapa jumlah total film dalam dataset?
# Genre apa yang paling banyak muncul?
# Film dengan rating tertinggi dalam dataset ini?
# Film dengan durasi terpanjang?
# Berapa rata-rata rating film per dekade?
# Apa genre paling dominan dalam film yang dirilis setelah tahun #2010?
# Berapa banyak film genre “Drama” yang dirilis sebelum tahun #2000?


import pandas as pd

file_path = "c:/Users/ThinkPad/Belajar Python/Library/oscar_age_male.csv"
df = pd.read_csv(file_path)

print(df.head())
# 1
total_film = len(df)
print("1. Total film dalam dataset:", total_film)


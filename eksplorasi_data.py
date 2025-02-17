import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset Titanic dari seaborn
df = sns.load_dataset('titanic')

# 1️⃣ --- INFO DATA ---
print("\n🔍 Info Data:")
print(df.info())

# 2️⃣ --- CEK MISSING VALUES ---
print("\n📌 Missing Values:")
print(df.isnull().sum())

# 3️⃣ --- STATISTIK DESKRIPTIF ---
print("\n📊 Statistik Deskriptif:")
print(df.describe())

# 4️⃣ --- VISUALISASI DISTRIBUSI UMUR ---
plt.figure(figsize=(10,5))
sns.histplot(df['age'], bins=30, kde=True, color='blue')
plt.title("Distribusi Usia Penumpang Titanic")
plt.xlabel("Usia")
plt.ylabel("Jumlah Penumpang")
plt.show()

# 5️⃣ --- VISUALISASI KELAS TIKET ---
plt.figure(figsize=(8,5))
sns.countplot(x="class", data=df, palette="coolwarm", order=['First', 'Second', 'Third'])
plt.title("Jumlah Penumpang Berdasarkan Kelas Tiket")
plt.show()

# 6️⃣ --- SURVIVAL RATE BERDASARKAN JENIS KELAMIN ---
plt.figure(figsize=(8,5))
sns.barplot(x="sex", y="survived", data=df, palette="Set2")
plt.title("Rata-rata Survival Rate Berdasarkan Jenis Kelamin")
plt.ylabel("Persentase Bertahan Hidup")
plt.show()

# 7️⃣ --- HEATMAP KORELASI ANTAR VARIABEL ---
plt.figure(figsize=(10,6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm", linewidths=0.5)
plt.title("Heatmap Korelasi Antar Variabel Titanic")
plt.show()

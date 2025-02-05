import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import streamlit as st

# Tambahkan Toggle untuk Dark Mode
dark_mode = st.sidebar.checkbox("Aktifkan Dark Mode")

# Konfigurasi Tema
if dark_mode:
    st.markdown(
        """
        <style>
        body, .stApp {
            background-color: #2E2E2E;
            color: white !important;
        }
        .css-1d391kg {
            background-color: #444;
        }
        .stTextInput > div > div > input,
        .stTextArea > div > textarea,
        .stSelectbox > div > div {
            color: white !important;
        }
        .stDataFrame, .stTable {
            background-color: #333 !important;
            color: white !important;
        }
        h1, h2, h3, h4, h5, h6, p, label {
            color: white !important;
        }
        .stButton>button {
            background-color: #555 !important;
            color: white !important;
            border: 1px solid white !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    color_map = 'coolwarm'
    text_color = "white"
else:
    color_map = 'viridis'
    text_color = "black"

# Judul Dashboard
st.title('Dashboard Analisis Data Penjualan')

# Buat data secara manual
np.random.seed(42)  # Untuk hasil yang konsisten
data = pd.DataFrame({
    'Sales': np.random.randint(100, 1000, 100),  # Penjualan antara 100 dan 1000
    'Advertising': np.random.randint(10, 200, 100),  # Biaya iklan antara 10 dan 200
    'Price': np.random.uniform(10, 50, 100),  # Harga produk antara 10 dan 50
    'Competitor_Price': np.random.uniform(10, 50, 100)  # Harga kompetitor antara 10 dan 50
})

# Tampilkan 5 baris pertama
st.header('Data Awal')
st.markdown(f"<p style='color:{text_color};'>Berikut adalah 5 data pertama:</p>", unsafe_allow_html=True)
st.write(data.head())

# Deskripsi statistik
st.header('Analisis Deskriptif')
st.markdown(f"<p style='color:{text_color};'>Statistik ringkasan data:</p>", unsafe_allow_html=True)
st.write(data.describe())

# Visualisasi distribusi penjualan
st.subheader('Distribusi Penjualan')
fig, ax = plt.subplots()
sns.histplot(data['Sales'], bins=30, kde=True, ax=ax)
ax.set_facecolor("#2E2E2E" if dark_mode else "white")
ax.spines['bottom'].set_color(text_color)
ax.spines['top'].set_color(text_color)
ax.spines['left'].set_color(text_color)
ax.spines['right'].set_color(text_color)
ax.xaxis.label.set_color(text_color)
ax.yaxis.label.set_color(text_color)
ax.title.set_color(text_color)
st.pyplot(fig)

# Visualisasi hubungan antara variabel
st.subheader('Hubungan Antar Variabel')
fig = sns.pairplot(data)
st.pyplot(fig)

# Korelasi antara variabel
st.header('Analisis Diagnostik')
st.subheader('Matriks Korelasi')
fig, ax = plt.subplots()
correlation_matrix = data.corr()
sns.heatmap(correlation_matrix, annot=True, cmap=color_map, ax=ax)
ax.set_facecolor("#2E2E2E" if dark_mode else "white")
st.pyplot(fig)

# Analisis penyebab penjualan rendah
low_sales = data[data['Sales'] < data['Sales'].quantile(0.25)]
st.subheader('Data Penjualan Rendah')
st.markdown(f"<p style='color:{text_color};'>Data penjualan dengan kuartil terendah:</p>", unsafe_allow_html=True)
st.write(low_sales.describe())

# Persiapan data untuk model prediktif
X = data[['Advertising', 'Price', 'Competitor_Price']]
y = data['Sales']

# Bagi data menjadi training dan testing set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Buat model regresi linear
model = LinearRegression()
model.fit(X_train, y_train)

# Prediksi penjualan
y_pred = model.predict(X_test)

# Evaluasi model
mse = mean_squared_error(y_test, y_pred)
st.header('Analisis Prediktif')
st.subheader('Evaluasi Model')
st.markdown(f"<p style='color:{text_color};'>Mean Squared Error: {mse}</p>", unsafe_allow_html=True)

# Visualisasi prediksi vs aktual
st.subheader('Aktual vs Prediksi Penjualan')
fig, ax = plt.subplots()
ax.scatter(y_test, y_pred, color='cyan' if dark_mode else 'blue')
ax.set_xlabel('Aktual', color=text_color)
ax.set_ylabel('Prediksi', color=text_color)
ax.set_title('Aktual vs Prediksi Penjualan', color=text_color)
ax.set_facecolor("#2E2E2E" if dark_mode else "white")
st.pyplot(fig)

# Rekomendasi berdasarkan prediksi
data['Predicted_Sales'] = model.predict(X)
data['Action'] = np.where(data['Predicted_Sales'] < data['Sales'].quantile(0.25), 'Tingkatkan Iklan', 'Pertahankan Strategi')

# Tampilkan rekomendasi
st.header('Analisis Preskriptif')
st.subheader('Rekomendasi Tindakan')
st.markdown(f"<p style='color:{text_color};'>Rekomendasi berdasarkan hasil prediksi:</p>", unsafe_allow_html=True)
st.write(data[['Sales', 'Predicted_Sales', 'Action']].head())

# Visualisasi rekomendasi
st.subheader('Distribusi Rekomendasi Tindakan')
action_counts = data['Action'].value_counts()
fig = px.pie(names=action_counts.index, values=action_counts.values, title='Rekomendasi Tindakan')
st.plotly_chart(fig)

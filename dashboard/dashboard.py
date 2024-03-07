import os
import streamlit as st
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.dates import MonthLocator, DateFormatter
# from matplotlib.dates import mdates

# Membaca data
current_directory = os.path.dirname(__file__)
csv_path = os.path.join(current_directory, 'main_data.csv')
df = pd.read_csv(csv_path)



# Judul dashboard
st.title('Dashboard tren kualitas udara')

# Pertanyaan pertama
st.write('1. Bagaimana tren konsentrasi PM2.5 pada stasiun Aotizhongxin dalam jangka waktu dari tanggal 2013-03-01 sampai 2014-01-01 ?')
# Rentang tanggal
start_date = '2013-03-01'
end_date = '2014-01-01'
# Filter data berdasarkan rentang tanggal
filtered_df = df[(df['date'] >= start_date) & (df['date'] <= end_date)]
# Membuat plot
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(filtered_df['date'], filtered_df['PM2.5'], color='blue', linestyle='-')  # Plot tren PM2.5
ax.set_title('Tren Konsentrasi PM2.5')
ax.set_xlabel('Tanggal')
ax.set_ylabel('Konsentrasi PM2.5')
ax.grid(True)

# Menampilkan plot pada Streamlit
st.pyplot(fig)

st.write('Conclution : Analisis tren konsentrasi PM2.5 dari Maret 2013 hingga Januari 2014 mengungkapkan fluktuasi yang signifikan. Dalam rentang waktu tersebut, terlihat peningkatan bertahap sejak sebelum Oktober 2013 hingga awal tahun 2014, meskipun mengalami penurunan pada akhir tahun. Puncak konsentrasi PM2.5 tercatat pada bulan Mei.')



# pertanyaan kedua
st.write('2. Bagaimana tren konsentrasi PM10 pada stasiun Aotizhongxin dalam jangka waktu dari tanggal 2013-03-01 sampai 2014-01-01 ?')
# Rentang tanggal
start_date = '2013-03-01'
end_date = '2014-01-01'
# Filter data berdasarkan rentang tanggal
filtered_df = df[(df['date'] >= start_date) & (df['date'] <= end_date)]
# Membuat plot
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(filtered_df['date'], filtered_df['PM10'], color='red', linestyle='-')  # Plot tren PM10
ax.set_title('Tren Konsentrasi PM10')
ax.set_xlabel('Tanggal')
ax.set_ylabel('Konsentrasi PM10')
ax.grid(True)

# Menampilkan plot pada Streamlit
st.pyplot(fig)

st.write('Conclution : Tren konsentrasi PM10 menunjukkan pola serupa dengan PM2.5, menampilkan fluktuasi yang sejalan. Pada bulan-bulan menjelang akhir tahun, teramati konsentrasi PM10 yang meningkat secara signifikan.')




st.write('3. Jumlah curah hujan pada stasiun Aotizhongxin dalam jangka waktu dari tanggal 2013-03-01 sampai 2014-01-01 ?')
# Rentang tanggal
start_date = '2013-03-01'
end_date = '2014-01-01'
# Filter data berdasarkan rentang tanggal
filtered_df = df[(df['date'] >= start_date) & (df['date'] <= end_date)]
# Membuat plot
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(filtered_df['date'], filtered_df['RAIN'], color='green', linestyle='-')  # Plot tren curah hujan
ax.set_title('Tren Hujan')
ax.set_xlabel('Tanggal')
ax.set_ylabel('Curah hujan')
ax.grid(True)

# Menampilkan plot pada Streamlit
st.pyplot(fig)

st.write('Conclution : Dalam visualisasi tren curah hujan dari Maret 2013 hingga Januari 2014, mencatatkan titik tertinggi curah hujan menjelang bulan Juli sedangkan pada bulan-bulan menjelang akhir tahun memiliki tingkat frekuensi hujan yang rendah.')
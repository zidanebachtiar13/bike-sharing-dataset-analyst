import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

day = pd.read_csv('../data/day.csv')
hour = pd.read_csv('../data/hour.csv')

st.header('Analisis Data Bike Sharing Dataset')

st.subheader('Pertanyaan 1: Pada musim apa customer terbanyak melakukan rental sepeda?')

musim_terbanyak = day[['season','cnt']].groupby(by='season').sum().reset_index()

colors = ["#D3D3D3", "#D3D3D3", "#72BCD4", "#D3D3D3"]
musim = ['Musim Semi', 'Musim Panas', 'Musim Gugur', 'Musim Dingin']

plt.figure(figsize=(10, 5))

sns.barplot(
    x="season",
    y="cnt",
    data=musim_terbanyak,
    palette=colors
)
plt.title("Customer Terbanyak Berdasarkan Musim", loc="center", fontsize=15)
plt.xlabel(None)
plt.ylabel(None)
plt.xticks([0,1,2,3], musim)
plt.tick_params(axis='x', labelsize=12)

st.pyplot(plt)

st.write('Pada diagram diatas bisa dilihat bahwa customer lebih banyak memilih musim gugur untuk melakukan rental sepeda.')

st.subheader('Pertanyaan 2: Bagaimana performa peminjaman sepeda pada masing-masing bulan?')

bulan_terbanyak = day[['mnth','cnt']].groupby(by='mnth').sum().reset_index()

bulan = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']

plt.figure(figsize=(10, 5))

plt.plot(bulan_terbanyak['mnth'], bulan_terbanyak['cnt'], marker='o', linewidth=2, color="#72BCD4")
plt.title("Banyaknya Peminjaman Sepeda Berdasarkan Bulan", loc="center", fontsize=15)
plt.xlabel(None)
plt.ylabel(None)
plt.xticks(range(1, 13), bulan, rotation=15)

st.pyplot(plt)

st.write('Pada diagram diatas bisa dilihat bahwa bulan Agustus merupakan bulan pilihan customer untuk melakukan rental sepeda. Namun hanya terdapat sedikit perbedaan antara bulan Mei, Juni, Juli, Agustus, dan September sehingga bulan tersebut juga dijadikan pilihan oleh customer.')

st.subheader('Pertanyaan 3: Pada jam berapa biasanya rental dijadikan pilihan customer?')

jam_terbanyak = hour[['hr', 'cnt']].groupby(by='hr').sum().reset_index()

plt.figure(figsize=(12, 5))

plt.plot(jam_terbanyak['hr'], jam_terbanyak['cnt'], marker='o', linewidth=2, color="#72BCD4")
plt.title("Banyaknya Peminjaman Sepeda Berdasarkan Jam", loc="center", fontsize=15)
plt.xlabel(None)
plt.ylabel(None)
plt.xticks(range(0, 24))

st.pyplot(plt)

st.write('Pada diagram diatas bisa dilihat bahwa customer terbanyak melakukan peminjaman sepeda pada sore hari jam 16 dan 19 Namun customer lain juga banyak melakukan peminjaman sepeda di jam 8 pagi.')

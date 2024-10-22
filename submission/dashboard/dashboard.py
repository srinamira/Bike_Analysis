import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Konfigurasi halaman
st.set_page_config(page_title="Dashboard Penggunaan Sepeda", layout="wide")

# Memuat dataset
day_data = pd.read_csv('day.csv')
hour_data = pd.read_csv('hour.csv')

# Sidebar untuk filter
st.sidebar.header("Filter")
selected_weather = st.sidebar.selectbox("Pilih Kondisi Cuaca:", day_data['weathersit'].unique())
selected_hour_range = st.sidebar.slider("Rentang Jam:", 0, 23, (0, 23))
selected_day = st.sidebar.selectbox("Pilih Hari:", day_data['weekday'].unique())

# Halaman utama
st.title("Dashboard Penggunaan Sepeda 🚲")

# 1. Tren Penggunaan Sepeda Harian
st.subheader("1. Tren Penggunaan Sepeda Harian")
fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(data=day_data, x='dteday', y='cnt', ax=ax)
ax.set_title("Penggunaan Sepeda Harian")
st.pyplot(fig)

# 2. Penggunaan per Jam (Berdasarkan Rentang Jam)
st.subheader("2. Penggunaan Sepeda per Jam")
filtered_data = hour_data[(hour_data['hr'] >= selected_hour_range[0]) & (hour_data['hr'] <= selected_hour_range[1])]
hour_summary = filtered_data.groupby('hr')['cnt'].mean().reset_index()

fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(data=hour_summary, x='hr', y='cnt', ax=ax)
ax.set_title(f"Rata-rata Penggunaan per Jam (Jam {selected_hour_range[0]} - {selected_hour_range[1]})")
st.pyplot(fig)

# 3. Pengaruh Cuaca terhadap Penggunaan Sepeda
st.subheader("3. Pengaruh Cuaca terhadap Penggunaan")
weather_data = hour_data[hour_data['weathersit'] == selected_weather]

fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(data=weather_data, x='hr', y='cnt', ax=ax)
ax.set_title(f"Penggunaan Sepeda Berdasarkan Cuaca: {selected_weather}")
st.pyplot(fig)

# 4. Pola Penggunaan di Hari Terpilih
st.subheader("4. Pola Penggunaan di Hari Terpilih")
filtered_day = hour_data[hour_data['weekday'] == selected_day]

fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(data=filtered_day, x='hr', y='cnt', ax=ax)
ax.set_title(f"Penggunaan Sepeda di Hari: {selected_day}")
st.pyplot(fig)

# Footer
st.sidebar.markdown("---")
st.sidebar.text("Dibuat dengan ❤️ menggunakan Streamlit")

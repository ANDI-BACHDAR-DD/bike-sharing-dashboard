import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Konfigurasi halaman
st.set_page_config(
    page_title="Bike Sharing Dashboard",
    layout="wide"
)

# Load data
day_df = pd.read_csv("day.csv")
day_df["dteday"] = pd.to_datetime(day_df["dteday"])

# Mapping kategori
day_df["season"] = day_df["season"].map({
    1: "Spring",
    2: "Summer",
    3: "Fall",
    4: "Winter"
})

day_df["workingday"] = day_df["workingday"].map({
    0: "Weekend/Holiday",
    1: "Working Day"
})

# Sidebar filter
st.sidebar.header("Filter Data")

season_filter = st.sidebar.multiselect(
    "Pilih Musim",
    options=day_df["season"].unique(),
    default=day_df["season"].unique()
)

workingday_filter = st.sidebar.multiselect(
    "Pilih Jenis Hari",
    options=day_df["workingday"].unique(),
    default=day_df["workingday"].unique()
)

filtered_df = day_df[
    (day_df["season"].isin(season_filter)) &
    (day_df["workingday"].isin(workingday_filter))
]

# Title
st.title("Dashboard Analisis Bike Sharing")

# KPI
total_rentals = int(filtered_df["cnt"].sum())
avg_rentals = int(filtered_df["cnt"].mean())

col1, col2 = st.columns(2)
col1.metric("Total Peminjaman", f"{total_rentals:,}")
col2.metric("Rata-rata Peminjaman Harian", f"{avg_rentals:,}")

# Visualisasi
sns.set_theme(style="whitegrid")

col3, col4 = st.columns(2)

with col3:
    st.subheader("Rata-rata Peminjaman Berdasarkan Musim")
    season_avg = filtered_df.groupby("season")["cnt"].mean().reset_index()
    fig1, ax1 = plt.subplots()
    sns.barplot(data=season_avg, x="season", y="cnt", ax=ax1)
    ax1.set_xlabel("Musim")
    ax1.set_ylabel("Rata-rata Peminjaman")
    st.pyplot(fig1)

with col4:
    st.subheader("Rata-rata Peminjaman: Hari Kerja vs Akhir Pekan")
    workingday_avg = filtered_df.groupby("workingday")["cnt"].mean().reset_index()
    fig2, ax2 = plt.subplots()
    sns.barplot(data=workingday_avg, x="workingday", y="cnt", ax=ax2)
    ax2.set_xlabel("Jenis Hari")
    ax2.set_ylabel("Rata-rata Peminjaman")
    st.pyplot(fig2)

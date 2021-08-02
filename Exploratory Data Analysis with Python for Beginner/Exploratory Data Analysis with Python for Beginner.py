#!/usr/bin/env python
# coding: utf-8

# # Memanggil Library di Python
# 

# In[1]:


import numpy as np
import pandas as pd


# # Membaca file dari Excel atau CSV sebagai data frame

# In[2]:


import pandas as pd
order_df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/order.csv")


# # Melihat struktur kolom dan baris dari data frame

# In[4]:


print(order_df.shape)


# # Melihat preview data dari data frame

# In[7]:


print(order_df.head(10))


# # Quick summary  dari segi kuantitas, harga, freight value, dan weight# 

# In[8]:


print(order_df.describe())


# # Median median dari total pembelian konsumen per transaksi kolom price

# In[9]:


print(order_df.loc[:, "price"].median())


# # Import Library Chart

# In[11]:


import matplotlib.pyplot as plt


# Tugas Praktek
# Baru saja aku menyimak beberapa halaman isi modul, Andra sudah kembali ke kantor dari rapat lanjutannya. Tampaknya Andra sosok yang begitu sibuk di kantor. Ketika tahu langkahnya berbelok menuju tempatku, aku dengan sigap menyiapkan laptop untuk menunjukkan hasil kerjaku padanya. 
# 
# “Pekerjaan tadi sudah selesai, Ndra. Bagaimana?” 
# 
# “Udah lebih rapi, ini nanti saya kasih ke kepala cabang untuk pertimbangan performa saat rapat,” ujar Andra cepat. Kulihat ia masih sibuk karena sesekali mengecek notifikasi ponselnya. 
# 
# Baru saja aku mau menutup program dan pergi ke pantry, Andra kembali memanggilku, “Satu lagi, Aksara.”
# 
# “Ada data tambahan lagi?” tebakku.
# 
# “Kamu buatkan price distributionnya juga ya dari pembelian produk di cabang tadi. Saya rasa itu penting untuk diberitahu ke mereka. Bikin saja dalam bentuk histogram price,” saran Andra. 
# 
# Aku pun kembali merebahkan diri di bangku dan mengutak-atik dataset order_df dengan jumlah bins=10:

# In[12]:


# plot histogram kolom: price
order_df[["price"]].hist(figsize=(4, 5), bins=10, xlabelsize=8, ylabelsize=8)
plt.show()  # Untuk menampilkan histogram plot


# “Aksara, dapat kabar terbaru dari kepala cabang. Tolong tampilkan data persebaran dari product_weight_gram penjualan cabang tadi ya,” ujar Andra kembali.
# 
# Wah, sehari bersama Andra adalah hari penuh pekerjaan beruntun. “Siap, Bos!” candaku. 
# 
# “Enggak, hahaha. Sudah tahu bukan caranya bagaimana?” Baru pertama kali aku mendengar Andra tertawa! Kupikir ia tipe yang serius sekali. 
# 
# Aku pun menunjukkan layar laptopku yang sedang menggunakan standar deviasi dan variance untuk menganalisis lebar persebaran distribusi tersebut. Andra tersenyum puas melihat pilihanku yang ini:|

# In[13]:


# Standar variasi kolom product_weight_gram
print(order_df.loc[:, "product_weight_gram"].std())
# Varians kolom product_weight_gram
print(order_df.loc[:, "product_weight_gram"].var())


# Setelah mendapatkan persebaran dari dataset order_df ("https://storage.googleapis.com/dqlab-dataset/order.csv") dan siap memberikannya pada Andra, aku terhenti sesaat.
# 
# Sepertinya aku perlu  menemukan batas IQR agar bisa menentukan outliers bagi kolom product_weight_gram.
# 
# Kalau begitu, hasilnya jadi lebih lengkap. Aku pun kembali mengecek dan mengerjakan kode:

# In[14]:


# Hitung quartile 1
Q1 = order_df[["product_weight_gram"]].quantile(0.25)
# Hitung quartile 3
Q3 = order_df[["product_weight_gram"]].quantile(0.75)
# Hitung inter quartile range dan cetak ke console
IQR = Q3 - Q1
print(IQR)


# Cobalah untuk mengubah kolom freight_value menjadi shipping_cost dalam data frame order_df, dengan menggunakan fungsi rename()

# In[15]:


# Ganti nama kolom freight_value menjadi shipping_cost
order_df.rename(columns={"freight_value": "shipping_cost"}, inplace=True)
print(order_df)


# Cobalah untuk mencari rata rata dari price per payment_type dari dataset order_df

# In[16]:


# Hitung rata rata dari price per payment_type
rata_rata = order_df["price"].groupby(order_df["payment_type"]).mean()
print(rata_rata)


# Tepat ketika kukira sudah selesai, ternyata masih ada tambahan! Lagi-lagi dari Andra. Aku tampaknya harus lebih terbiasa dengan cara bekerja seperti ini. 
# 
# “Aksara, ini sudah menyeluruh dan lengkap. Tambahin satu lagi saja, tolong cari berapa harga maksimum pembelian customer di dataset order_df.”
# 
# “Oke.”
# 
#  
# 
# Aku mulai mengerjakan rikues dari Andra dengan cara ini:

# In[17]:


# Hitung harga maksimum pembelian customer
sort_harga = order_df.sort_values(by="price", ascending=False)
print(sort_harga)


# Tugas dari Andra
# Aksara, bisa tolong bantu mengurus beberapa data penjualan dari dataset oder.csv? Saya sedang rapat dan bahan ini ditunggu dalam pembahasan cabang supermarket kita. Berikut ya detailnya:
# 
# Median price yang dibayar customer dari masing-masing metode pembayaran.
# Tentukan metode pembayaran yang memiliki basket size (rataan median price) terbesar.
# Ubah freight_value menjadi shipping_cost dan cari shipping_cost termahal dari data penjualan tersebut menggunakan sort.
# Untuk product_category_name, berapa rata-rata weight produk tersebut dan standar deviasi mana yang terkecil dari weight tersebut,
# Buat histogram quantity penjualan dari dataset tersebut untuk melihat persebaran quantity penjualan tersebut dengan bins = 5 dan figsize= (4,5)
# Khusus poin 4, tolong diperhatikan lebih ya, Aksara karena hasil analisisnya akan digunakan kepala cabang dalam menyusun strategi free ongkir.
# 
# Kubalas email itu segera, OK! Hasilnya akan selesai sebelum makan siang ya. You can count on me, hehehe.
# 
# Perhatian: Semua string dinyatakan dalam kutipan "...".

# In[20]:


# Median price yang dibayar customer dari masing-masing metode pembayaran. 
median_price = order_df["price"].groupby(order_df["payment_type"]).median()
print(median_price)
# Ubah freight_value menjadi shipping_cost dan cari shipping_cost 
# termahal dari data penjualan tersebut menggunakan sort.
order_df.rename(columns={"freight_value": "shipping_cost"}, inplace=True)
sort_value = order_df.sort_values(by="shipping_cost", ascending=0)
print(sort_value)
# Untuk product_category_name, berapa  rata-rata weight produk tersebut 
# dan standar deviasi mana yang terkecil dari weight tersebut, 
mean_value = order_df["product_weight_gram"].groupby(order_df["product_category_name"]).mean()
print(mean_value.sort_values())
std_value = order_df["product_weight_gram"].groupby(order_df["product_category_name"]).std()
print(std_value.sort_values())
# Buat histogram quantity penjualan dari dataset tersebutuntuk melihat persebaran quantity 
# penjualan tersebut dengan bins = 5 dan figsize= (4,5)
order_df[["quantity"]].hist(figsize=(4, 5), bins=5)
plt.show()


# Hasil Belajarku :)
# Walau harus lembur, aku cukup puas dengan hasil kerjaku hari ini. Aku memandangi kode final yang sudah selesai kukerjakan. Diam-diam ada perasaan bangga menyelip di benakku! YES!
# 
# Tidak terasa, aku telah menyelesaikan modul Exploratory Data Analysis with Python for Beginner. Dari materi-materi yang telah kupelajari dan praktekkan dalam modul ini aku telah mendapatkan pengetahuan (knowledge) dan praktek (skill) untuk:
# 
# Memahami library Pandas, NumPy, dan Matplotlib dari Python.
# Mengetahui jenis - jenis tipe data dalam data frame Python
# Mampu membaca datasets dari Excel dan CSV
# Membuat summary data sederhana, mencakup distribusi, varians, dan mendeteksi outliers dari dataset.
# Latihan dalam membuat laporan bisnis sederhana menggunakan Python

# In[ ]:





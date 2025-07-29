# -------------------------
# Load Libraries

library('ggvis')
library('tidyverse')
library('ggplot2')

# -------------------------
# Load Data

data_perpustakaan = read.csv('D:/VIDEO/Belajar/DATA ANALYST/dataset/Data Perpustakaan.csv', header=T, na.strings='')
head(data_perpustakaan)

# -------------------------
# Descriptive Statistics

class(data_perpustakaan)

colSums(is.na(data_perpustakaan))

str(data_perpustakaan)

summary(data_perpustakaan)

# -------------------------
# Plotting

# Perbandingan Predikat Perpustakaan Khusus
df_predikat <- data.frame(
  Predikat = c("A", "B", "C"),
  Jumlah = c(21, 11, 5)
)

# Plot pie chart
ggplot(df_predikat, aes(x = "", y = Jumlah, fill = Predikat)) +
  geom_bar(stat = "identity", width = 1, color = "white") +
  coord_polar("y") +
  labs(title = "Perbandingan Predikat Perpustakaan Khusus")


# Perbandingan Predikat Perpustakaan Sekolah
df_predikat_sekolah <- data.frame(
  Predikat = c("A", "B", "C"),
  Jumlah = c(9, 4, 0)
)

# Plot bar chart
ggplot(df_predikat_sekolah, aes(x = Predikat, y = Jumlah, fill = Predikat)) +
  geom_bar(stat = "identity", color = "white") +
  labs(title = "Perbandingan Predikat Perpustakaan Sekolah", x = "Predikat", y = "Jumlah")

# Perbandingan Predikat Perpustakaan Perguruan Tinggi
df_predikat_pt <- data.frame(
  Predikat = c("A", "B", "C"),
  Jumlah = c(11, 3, 4)
)

# Plot bar chart
ggplot(df_predikat_pt, aes(x = Predikat, y = Jumlah, fill = Predikat)) +
  geom_bar(stat = "identity", color = "white") +
  labs(title = "Perbandingan Predikat Perpustakaan Perguruan Tinggi", x = "Predikat", y = "Jumlah")

# Perbandingan Predikat Perpustakaan Umum
df_predikat_umum <- data.frame(
  Predikat = c("A", "B", "C"),
  Jumlah = c(17, 2, 0)
)

# Plot bar chart
ggplot(df_predikat_umum, aes(x = Predikat, y = Jumlah, fill = Predikat)) +
  geom_bar(stat = "identity", color = "white") +
  labs(title = "Perbandingan Predikat Perpustakaan Umum", x = "Predikat", y = "Jumlah")

# Perbandingan Jumlah Perpustakaan Terakreditasi
df_terakreditasi <- data.frame(
  Kategori = c("Khusus", "Sekolah", "Perguruan Tinggi", "Umum"),
  Jumlah = c(3, 0, 1, 0)
)

# Plot bar chart
ggplot(df_terakreditasi, aes(x = Kategori, y = Jumlah, fill = Kategori)) +
  geom_bar(stat = "identity", color = "white") +
  labs(title = "Perbandingan Jumlah Perpustakaan Terakreditasi", x = "Kategori", y = "Jumlah")


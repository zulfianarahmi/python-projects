install.packages(rpart)
install.packages("rpart.plot")

library(rpart)
library(rpart.plot)

#model Decision Tree
tree_model <- rpart(y ~ ., data = train_data, method = "class")

# Cek hasil modelnya
print(tree_model)

rpart.plot(tree_model)

predictions_tree <- predict(tree_model, newdata = test_data, type = class)
Oke, gaskeun! Kita coba bikin model nomor 1 (Decision Tree) dan 2 (Random Forest).

Tapi sebelum itu, kita lurusin dulu soal "regresi logistik tree".

Sebenarnya, Regresi Logistik dan Decision Tree (Pohon Keputusan) itu adalah dua jenis model yang berbeda, meskipun tujuannya sama-sama buat klasifikasi (nebak 0 atau 1).

Regresi Logistik: Ini model statistik. Dia nyari sebuah "rumus" matematis buat misahin data. Hasilnya itu probabilitas (peluang) antara 0 sampai 1.

Decision Tree: Ini model yang lebih intuitif. Dia bikin serangkaian aturan "jika-maka" yang bentuknya kayak pohon. Dia nggak ngasih rumus, tapi alur keputusan.

Jadi, kemungkinannya lo salah denger atau mungkin yang dimaksud adalah "pakai Decision Tree untuk masalah yang sama dengan Regresi Logistik". Sekarang, kita coba bikin modelnya ya.

## 1. Bikin Model Pohon Keputusan (Decision Tree) 🌳
Ini model yang asyik karena kita bisa "liat" cara dia mikir.

Langkah 1: Siapin Library
Kita butuh paket rpart buat bikin modelnya dan rpart.plot buat gambarin pohonnya biar cakep.

R

# Install dulu kalau belum ada
# install.packages("rpart")
# install.packages("rpart.plot")

library(rpart)
library(rpart.plot)
Langkah 2: Bikin & Latih Modelnya
Kita pakai fungsi rpart(). Sintaksnya mirip kayak glm() kemarin. method = "class" itu buat ngasih tau R kita lagi ngerjain masalah klasifikasi.

R

# Latih model Decision Tree
# y ~ . artinya prediksi 'y' berdasarkan semua fitur lain
tree_model <- rpart(y ~ ., data = train_data, method = "class")

# Cek hasil modelnya
print(tree_model)
Langkah 3: Visualisasi Pohonnya!
  Ini bagian paling serunya. Kita gambar pohon keputusan yang udah dibuat model.

R

# Gambar pohonnya
rpart.plot(tree_model)
Dari gambar ini, lo bisa liat persis gimana modelnya ngambil keputusan. Misalnya, dia bakal cek Glucose, kalau nilainya di atas sekian, dia belok ke cabang "kemungkinan diabetes", dan seterusnya.

Langkah 4: Evaluasi Performa
Sekarang kita tes performa "pohon" kita pake data testing.


# Bikin prediksi di data testing
predictions_tree <- predict(tree_model, newdata = test_data, type = "class")

# Bikin confusion matrix
confusionMatrix(predictions_tree, factor(test_data$y))
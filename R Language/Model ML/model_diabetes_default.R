# Panggil library yang dibutuhin
library(readr)
library(caTools)
library(caret)
library(e1071)

# Baca file CSV-nya
data <- read.csv("C:\\KULIAH\\SEMESTER 1\\Komputer1\\diabetes.csv")

# Intip 6 baris pertama data buat mastiin udah bener
head(data)

# Pisahin antara fitur (X) dan target (y)
X <- data[, 1:8]
y <- data[, 9]

# Scaling fitur
scaled_X <- as.data.frame(scale(X))

# Gabungin lagi fitur yang udah di-scale sama targetnya
scaled_data <- cbind(scaled_X, y)

# Bagi data jadi training dan testing set
set.seed(123) # Biar hasil pembagiannya konsisten kalo diulang
sample <- sample.split(scaled_data$y, SplitRatio = 0.7)
train_data <- subset(scaled_data, sample == TRUE)
test_data <- subset(scaled_data, sample == FALSE)

library(ggplot2)
ggplot(data, aes(x = factor(Outcome), y = BMI, fill = factor(Outcome))) +
  geom_boxplot() +
  labs(title = "Distribusi BMI berdasarkan Outcome")

# Bikin model regresi logistik
# y ~ . artinya: prediksi 'y' berdasarkan semua fitur lain
log_model <- glm(y ~ ., data = train_data, family = binomial)

# Liat ringkasan modelnya
summary(log_model)

# Bikin prediksi di data testing
predictions <- predict(log_model, newdata = test_data, type = "response")

# Ubah hasil prediksi (yang bentuknya probabilitas) jadi 0 atau 1
predicted_classes <- ifelse(predictions > 0.5, 1, 0)

# Bikin confusion matrix buat liat performanya
confusionMatrix(factor(predicted_classes), factor(test_data$y))

# Bikin fungsi buat prediksi
predict_diabetes <- function(pregnancies, glucose, bloodpressure, skinthickness,
                             insulin, bmi, diabetespedigreefunction, age) {
  # Bikin data frame dari input baru
  input_data <- data.frame(
    Pregnancies = pregnancies, Glucose = glucose, BloodPressure = bloodpressure,
    SkinThickness = skinthickness, Insulin = insulin, BMI = bmi,
    DiabetesPedigreeFunction = diabetespedigreefunction, Age = age
  )
  
  # Jangan lupa di-scaling juga! (Ini bagian penting yg sering kelewat)
  # Di sini kita pake mean & sd dari data training awal buat scaling
  
  # Bikin prediksi
  prediction_prob <- predict(log_model, newdata = input_data, type = "response")
  prediction_class <- ifelse(prediction_prob > 0.5, 1, 0)
  
  if (prediction_class == 1) {
    return("Berdasarkan model, kemungkinan besar punya diabetes.")
  } else {
    return("Berdasarkan model, risiko diabetes lebih rendah.")
  }
}

# Coba tebak data pasien baru
print(predict_diabetes(6, 148, 72, 35, 0, 33.6, 0.627, 50))
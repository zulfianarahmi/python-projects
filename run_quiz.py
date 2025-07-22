# --- Bank Soal Teori Programming ---
questions = [
    {
        "question": "Apa itu variabel dalam pemrograman?",
        "options": ["A. Perintah untuk mencetak", "B. Tempat menyimpan data", "C. Jenis data khusus", "D. Fungsi logika"],
        "answer": "B"
    },
    {
        "question": "Bahasa pemrograman manakah yang termasuk low-level language?",
        "options": ["A. Python", "B. C", "C. Assembly", "D. Java"],
        "answer": "C"
    },
    {
        "question": "Apa fungsi dari perulangan (loop) dalam pemrograman?",
        "options": ["A. Menghentikan program", "B. Menyimpan data", "C. Menjalankan perintah berulang", "D. Menghapus variabel"],
        "answer": "C"
    },
    {
        "question": "Struktur kontrol if-else digunakan untuk?",
        "options": ["A. Pengulangan", "B. Penyimpanan data", "C. Pengambilan keputusan", "D. Menampilkan output"],
        "answer": "C"
    },
    {
        "question": "Apa yang dimaksud dengan ‘bug’ dalam pemrograman?",
        "options": ["A. Bahasa pemrograman", "B. Error dalam program", "C. Versi software", "D. Fitur tambahan"],
        "answer": "B"
    },
    {
        "question": "Manakah di bawah ini yang merupakan tipe data primitif?",
        "options": ["A. Array", "B. List", "C. Integer", "D. Class"],
        "answer": "C"
    },
    {
        "question": "Apa kepanjangan dari OOP?",
        "options": ["A. Object Oriented Programming", "B. Open Operation Process", "C. Overloaded Output Procedure", "D. Original Object Pattern"],
        "answer": "A"
    },
    {
        "question": "Fungsi dari komentar dalam kode program adalah?",
        "options": ["A. Menjalankan program", "B. Menambah error", "C. Memberi penjelasan", "D. Meningkatkan kecepatan"],
        "answer": "C"
    },
    {
        "question": "Apa yang dimaksud dengan 'array'?",
        "options": ["A. Fungsi untuk input", "B. Variabel tunggal", "C. Struktur data berisi kumpulan nilai", "D. Perintah looping"],
        "answer": "C"
    },
    {
        "question": "Apa hasil dari operasi logika True AND False?",
        "options": ["A. True", "B. False", "C. Error", "D. Null"],
        "answer": "B"
    }
]



def run_quiz(questions):
    score = 0

    for item in questions:
        print("------------------------------")
        print(item["question"])
    
        for option in item["options"]:
            print(option)

        answer = input("Enter your answer: ")

        if answer.upper() == item["answer"]:
            score += 1

    print(f"\n==============================")
    print(f"Skor akhir Anda: {score} dari {len(questions)} pertanyaan.")

    percentage = (score / len(questions)) * 100
    print(f"Anda benar {percentage:.2f}%")

    if percentage == 100:
        print("Sempurna! Anda jenius! 🧠")
    elif percentage >= 75:
        print("Luar biasa! Pengetahuan Anda luas! 👍")
    elif percentage >= 50:
        print("Bagus! Terus belajar, ya! 😊")
    else:
        print("Tidak apa-apa, coba lagi lain kali! 💪")

# Panggil fungsi
run_quiz(questions)








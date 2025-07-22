def tambah_tugas(tasks):
    tugas_baru = input("Masukkan tugas baru: ")
    tasks.append(tugas_baru)
    print(f"Tugas {tugas_baru} berhasil ditambahkan")

def hapus_tugas(tasks):
    if not tasks:
        print("Tidak ada tugas yang ingin dihapus")
        return
    tampilkan_tugas(tasks)
    try:
        nomor_hapus = int(input("Pilih nomor tugas yang ingin dihapus: "))
        if 1 <= nomor_hapus <= len(tasks):
            hapus = tasks.pop(nomor_hapus - 1)
            print(f"Tugas {hapus} berhasil dihapus")
        else:
            print("Nomor tugas tidak valid")
    except ValueError:
        print("Masukkan nomor tugas yang valid")

def tampilkan_tugas(task):
    print("---------- Ini Daftar Tugas Rahmiii, kerjain yaa ------------")
    for i, tugas in enumerate(task, 1):
        print(f"{i}. {tugas}")

def tampilkan_menu():
    print("------------- Ini adalah To do list app untuk Zulfiana Rahmi -------------")
    print("1. Tampilkan task")
    print("2. Tambahkan task")
    print("3. Hapus task")
    print("4. Keluar")

def ucapan_selesai():
    print("Terima kasih telah menggunakan aplikasi ini")

def main():
    tasks = []
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu: ")
        if pilihan == "1":
            tampilkan_tugas(tasks)
        elif pilihan == "2":
            tambah_tugas(tasks)
        elif pilihan == "3":
            hapus_tugas(tasks)
        elif pilihan == "4":
            print("Terima kasih telah menggunakan aplikasi ini")
            break
        else:
            ucapan_selesai()

if __name__ == "__main__":
    main()
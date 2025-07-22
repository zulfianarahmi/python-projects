task = []

#loop agar program terus berulang
while True:
    print("------------- Ini adalah To do list app untuk Zulfiana Rahmi -------------")
    print("1. Tampilkan task")
    print("2. Tambahkan task")
    print("3. Hapus task")
    print("4. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        print("---------- Ini Daftar Tugas Rahmiii, kerjain yaa ------------")
        if not task:
            print("Tidak ada tugas yang ditemukan")
        else:
            for i, tugas in enumerate(task, 1):
                print(f"{i}. {tugas}")
                
    elif pilihan == "2":
        tugas_baru = input("Masukkan tugas baru: ")
        task.append(tugas_baru)
        print(f"Tugas {tugas_baru} berhasil ditambahkan")
    elif pilihan == "3":
        if not task:
            print("Tidak ada tugas yang ingin dihapus")
        else:
            print("---------- Ini Daftar Tugas Rahmiii, kerjain yaa ------------")
            for i, tugas in enumerate(task, 1):
                print(f"{i}. {tugas}")
            try:
                nomor_hapus =(int(input("Pilih nomor tugas yang ingin dihapus: ")))
                if 1 <= nomor_hapus <= len(task):
                    hapus_tugas = task.pop(nomor_hapus - 1)
                    print(f"Tugas {hapus_tugas} berhasil dihapus")
                else:
                    print("Nomor tugas tidak valid")
            except ValueError:
                print("Masukkan nomor tugas yang valid")
    elif pilihan == "4":
        print("Terima kasih telah menggunakan aplikasi ini")
        break
    else:
        print("Pilihan tidak valid")
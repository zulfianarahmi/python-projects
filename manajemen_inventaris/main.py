inventory = {}

def tambah_barang():
    id_barang = input("Masukkan ID barang : ")
    nama_barang = input("Masukkan nama barang: ")

    try:
        jumlah_barang = int(input("Masukkan jumlah barang: "))
    except ValueError:
        print("⚠️ Jumlah barang harus berupa angka!")
        return

    inventory[id_barang] = {
        "nama": nama_barang,
        "jumlah": jumlah_barang
    }

def tampilkan_barang():
    print("======== Ini adalah list barang ========")
    for id_barang, info in inventory.items():
        print(f"{id_barang}: {info['nama']} (Stok: {info['jumlah']})")

# Eksekusi
tambah_barang()
tampilkan_barang()